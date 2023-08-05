
import numpy as np
import pandas as pd
from typing import List, Union, Tuple
import random
from macrosynergy.management.simulate_quantamental_data import make_qdf

def difference(list_1: List[str], list_2: List[str]):
    """
    Helper method used to display possible missing categories or cross-sections.

    :param <List[str]> list_1: first list.
    :param <List[str]> list_2: second list.

    """

    missing = sorted(set(list_1) - set(list_2))
    if len(missing) > 0:
        list_1 = [elem for elem in list_1 if elem not in missing]
    return list_1

def reduce_df(df: pd.DataFrame, xcats: List[str] = None,  cids: List[str] = None,
              start: str = None, end: str = None, blacklist: dict = None,
              out_all: bool = False, intersect: bool = False):
    """
    Filter DataFrame by xcats and cids and notify about missing xcats and cids.

    :param <pd.Dataframe> df: standardized dataframe with the necessary columns:
        'cid', 'xcats', 'real_date'.
    :param <List[str]> xcats: extended categories to be checked on. Default is all in the
        dataframe.
    :param <List[str]> cids: cross sections to be checked on. Default is all in the
        dataframe.
    :param <str> start: string representing earliest date. Default is None.
    :param <str> end: string representing the latest date. Default is None.
    :param <dict> blacklist: cross sections with date ranges that should be excluded from
        the data frame. If one cross section has several blacklist periods append numbers
        to the cross-section code.
    :param <bool> out_all: if True the function returns reduced dataframe and selected/
        available xcats and cids.
        Default is False, i.e. only the dataframe is returned
    :param <bool> intersect: if True only retains cids that are available for all xcats.
        Default is False.

    :return <pd.Dataframe>: reduced DataFrame that also removes duplicates or
        (for out_all True) DataFrame and available and selected xcats and cids.
    """

    dfx = df[df['real_date'] >= pd.to_datetime(start)] if start is not None else df
    dfx = dfx[dfx['real_date'] <= pd.to_datetime(end)] if end is not None else dfx

    if blacklist is not None:
        for key, value in blacklist.items():
            filt1 = dfx['cid'] == key[:3]
            filt2 = dfx['real_date'] >= pd.to_datetime(value[0])
            filt3 = dfx['real_date'] <= pd.to_datetime(value[1])
            dfx = dfx[~(filt1 & filt2 & filt3)]

    xcats_in_df = dfx['xcat'].unique()
    if xcats is None:
        xcats = sorted(xcats_in_df)
    else:
        xcats = difference(xcats, xcats_in_df)

    dfx = dfx[dfx['xcat'].isin(xcats)]

    if intersect:
        df_uns = dict(dfx.groupby('xcat')['cid'].unique())
        df_uns = {k: set(v) for k, v in df_uns.items()}
        cids_in_df = list(set.intersection(*list(df_uns.values())))
    else:
        cids_in_df = dfx['cid'].unique()

    if cids is None:
        cids = sorted(cids_in_df)
    else:
        cids = [cids] if isinstance(cids, str) else cids
        cids = difference(cids, cids_in_df)

        cids = set(cids).intersection(cids_in_df)
        dfx = dfx[dfx['cid'].isin(cids)]

    if out_all:
        return dfx.drop_duplicates(), xcats, sorted(list(cids))
    else:
        return dfx.drop_duplicates()

def reduce_df_by_ticker(df: pd.DataFrame, ticks: List[str] = None,  start: str = None,
                        end: str = None, blacklist: dict = None):
    """
    Filter dataframe by xcats and cids and notify about missing xcats and cids

    :param <pd.Dataframe> df: standardized dataframe with the following columns:
        'cid', 'xcats', 'real_date'.
    :param <List[str]> ticks: tickers (cross sections + base categories)
    :param <str> start: string in ISO 8601 representing earliest date. Default is None.
    :param <str> end: string ISO 8601 representing the latest date. Default is None.
    :param <dict> blacklist: cross sections with date ranges that should be excluded from
        the dataframe. If one cross section has several blacklist periods append numbers
        to the cross section code.

    :return <pd.Dataframe>: reduced dataframe that also removes duplicates
    """

    dfx = df.copy()
    dfx = dfx[dfx["real_date"] >= pd.to_datetime(start)] if start is not None else dfx
    dfx = dfx[dfx["real_date"] <= pd.to_datetime(end)] if end is not None else dfx

    # Blacklisting by cross-section.
    if blacklist is not None:
        for key, value in blacklist.items():
            filt1 = dfx["cid"] == key[:3]
            filt2 = dfx["real_date"] >= pd.to_datetime(value[0])
            filt3 = dfx["real_date"] <= pd.to_datetime(value[1])
            dfx = dfx[~(filt1 & filt2 & filt3)]

    dfx["ticker"] = dfx["cid"] + '_' + dfx["xcat"]
    ticks_in_df = dfx["ticker"].unique()
    if ticks is None:
        ticks = sorted(ticks_in_df)
    else:
        ticks = difference(ticks, ticks_in_df)

    dfx = dfx[dfx["ticker"].isin(ticks)]

    return dfx.drop_duplicates()

def aggregation_helper(dfx: pd.DataFrame, xcat_agg: str):
    """
    Helper method to down-sample each category in the DataFrame by aggregating over the
    intermediary dates according to a prescribed method.

    :param <List[str]> dfx: standardised DataFrame defined exclusively on a single
        category.
    :param <List[str]> xcat_agg: associated aggregation method for the respective
        category.

    """

    dfx = dfx.groupby(['xcat', 'cid', 'custom_date'])
    dfx = dfx.agg(xcat_agg).reset_index()

    if 'real_date' in dfx.columns:
        dfx = dfx.drop(['real_date'], axis=1)
    dfx = dfx.rename(columns={"custom_date": "real_date"})

    return dfx

def categories_df(df: pd.DataFrame, xcats: List[str], cids: List[str] = None,
                  val: str = 'value', start: str = None, end: str = None,
                  blacklist: dict = None, years: int = None, freq: str = 'M',
                  lag: int = 0, fwin: int = 1, xcat_aggs: List[str] = ('mean', 'mean')):

    """
    Create custom two-categories dataframe with appropriate frequency and lags
    suitable for analysis.

    :param <pd.Dataframe> df: standardized dataframe with the following necessary columns:
        'cid', 'xcats', 'real_date' and at least one column with values of interest.
    :param <List[str]> xcats: exactly two extended categories whose relationship is to be
        analyzed. It must be noted that the first category is the explanatory variable
        and the second category the explained, dependent, variable.
    :param <List[str]> cids: cross sections to be included. Default is all in the
        dataframe.
    :param <str> start: earliest date in ISO 8601 format. Default is None, i.e. earliest
        date in data frame is used.
    :param <str> end: latest date in ISO 8601 format. Default is None, i.e. latest date
        in data frame is used.
    :param <dict> blacklist: cross sections with date ranges that should be excluded from
        the data frame. If one cross section has several blacklist periods append numbers
        to the cross section code.
    :param <int> years: Number of years over which data are aggregated. Supersedes the
        "freq" parameter and does not allow lags, Default is None, i.e. no multi-year
        aggregation.
    :param <str> val: name of column that contains the values of interest. Default is
        'value'.
    :param <str> freq: letter denoting frequency at which the series are to be sampled.
        This must be one of 'D', 'W', 'M', 'Q', 'A'. Default is 'M'.
    :param <int> lag: lag (delay of arrival) of first (explanatory) category in periods
        as set by freq. Default is 0.
    :param <int> fwin: forward moving average window of first category. Default is 1,
        i.e no average.
        Note: This parameter is used mainly for target returns as dependent variables.
    :param <List[str]> xcat_aggs: Exactly two aggregation methods. Default is 'mean' for
        both.

    :return <pd.Dataframe>: custom data frame with two category columns
    """

    assert freq in ['D', 'W', 'M', 'Q', 'A']
    assert not (years is not None) & (lag != 0), 'Lags cannot be applied to year groups.'
    if years is not None:
        assert isinstance(start, str), "Year aggregation requires a start date."

    df, xcats, cids = reduce_df(df, xcats, cids, start, end, blacklist, out_all=True)

    col_names = ['cid', 'xcat', 'real_date', val]

    sum_clause = 'sum' in xcat_aggs
    if sum_clause:
        sum_index = xcat_aggs.index('sum')

    df_output = []
    if years is None:
        expln = xcats[0]
        depnd = xcats[1]

        df_w = df.pivot(index=('cid', 'real_date'), columns='xcat', values=val)
        df_w = df_w.groupby([pd.Grouper(level='cid'),
                             pd.Grouper(level='real_date', freq=freq)])
        expln_col = df_w[expln].agg(xcat_aggs[0]).astype(dtype=np.float32)
        depnd_col = df_w[depnd].agg(xcat_aggs[1]).astype(dtype=np.float32)
        if sum_clause and sum_index:
            depnd_col = depnd_col.replace({0.0: np.nan})
        elif sum_clause:
            expln_col = expln_col.replace({0.0: np.nan})

        # Explanatory variable is shifted forward.
        if lag > 0:
            # Utilise .groupby() to handle for multi-index Pandas DataFrame.
            expln_col = expln_col.groupby(level=0).shift(1)
        if fwin > 0:
            s = 1 - fwin
            depnd_col = depnd_col.rolling(window=fwin).mean().shift(s)

        expln_df = expln_col.reset_index()
        expln_df['xcat'] = expln
        expln_df = expln_df.rename(columns={expln: "value"})

        depnd_df = depnd_col.reset_index()
        depnd_df['xcat'] = depnd
        depnd_df = depnd_df.rename(columns={depnd: "value"})
        df_output.append(pd.concat([expln_df, depnd_df], ignore_index=True))

    else:
        s_year = pd.to_datetime(start).year
        start_year = s_year
        e_year = df['real_date'].max().year + 1

        grouping = int((e_year - s_year) / years)
        remainder = (e_year - s_year) % years

        year_groups = {}

        for group in range(grouping):
            value = [i for i in range(s_year, s_year + years)]
            key = f"{s_year} - {s_year + (years - 1)}"
            year_groups[key] = value

            s_year += years

        v = [i for i in range(s_year, s_year + (remainder + 1))]
        year_groups[f"{s_year} - now"] = v
        list_y_groups = list(year_groups.keys())

        translate_ = lambda year: list_y_groups[int((year % start_year) / years)]
        df['real_date'] = pd.to_datetime(df['real_date'], errors='coerce')
        df['custom_date'] = df['real_date'].dt.year.apply(translate_)

        dfx_list = [df[df['xcat'] == xcats[0]],
                    df[df['xcat'] == xcats[1]]]
        df_agg = list(map(aggregation_helper, dfx_list, xcat_aggs))
        df_output.extend([d[col_names] for d in df_agg])

    dfc = pd.concat(df_output)
    # If either of the two variables, explanatory or dependent variable, contain a NaN
    # value, remove the row: a relationship is not able to be established between a
    # realised datapoint and a Nan value. Therefore, remove the row from the returned
    # DataFrame.
    dfc = dfc.pivot(index=('cid', 'real_date'), columns='xcat',
                    values=val).dropna()[xcats]

    return dfc


if __name__ == "__main__":

    cids = ['NZD', 'AUD', 'GBP', 'CAD']
    xcats = ['XR', 'CRY', 'GROWTH', 'INFL']
    df_cids = pd.DataFrame(index=cids, columns=['earliest', 'latest', 'mean_add',
                                                'sd_mult'])
    df_cids.loc['AUD'] = ['2000-01-01', '2020-12-31', 0.1, 1]
    df_cids.loc['CAD'] = ['2001-01-01', '2020-11-30', 0, 1]
    df_cids.loc['GBP'] = ['2002-01-01', '2020-11-30', 0, 2]
    df_cids.loc['NZD'] = ['2002-01-01', '2020-09-30', -0.1, 2]

    df_xcats = pd.DataFrame(index=xcats, columns=['earliest', 'latest', 'mean_add',
                                                  'sd_mult', 'ar_coef', 'back_coef'])
    df_xcats.loc['XR'] = ['2000-01-01', '2020-12-31', 0.1, 1, 0, 0.3]
    df_xcats.loc['CRY'] = ['2000-01-01', '2020-10-30', 1, 2, 0.95, 1]
    df_xcats.loc['GROWTH'] = ['2001-01-01', '2020-10-30', 1, 2, 0.9, 1]
    df_xcats.loc['INFL'] = ['2001-01-01', '2020-10-30', 1, 2, 0.8, 0.5]

    black = {'AUD': ['2000-01-01', '2003-12-31'], 'GBP': ['2018-01-01', '2100-01-01']}

    random.seed(2)
    dfd = make_qdf(df_cids, df_xcats, back_ar=0.75)

    dfd_x1 = reduce_df(dfd, xcats=xcats[:-1], cids=cids[0],
                       start='2012-01-01', end='2018-01-31')
    print(dfd_x1['xcat'].unique())

    dfd_x2 = reduce_df(dfd, xcats=xcats, cids=cids, start='2012-01-01', end='2018-01-31')
    dfd_x3 = reduce_df(dfd, xcats=xcats, cids=cids, blacklist=black)

    tickers = [cid + "_XR" for cid in cids]
    dfd_xt = reduce_df_by_ticker(dfd, ticks=tickers, blacklist=black)

    # Testing categories_df().
    dfc1 = categories_df(dfd, xcats=['GROWTH', 'CRY'], cids=cids, freq='M', lag=1,
                         xcat_aggs=['mean', 'mean'], start='2000-01-01', blacklist=black)

    dfc2 = categories_df(dfd, xcats=['GROWTH', 'CRY'], cids=cids, freq='M', lag=0,
                         fwin=3, xcat_aggs=['mean', 'mean'],
                         start='2000-01-01', blacklist=black)

    dfc3 = categories_df(dfd, xcats=['GROWTH', 'CRY'], cids=cids, freq='M', lag=0,
                         xcat_aggs=['mean', 'mean'], start='2000-01-01', blacklist=black,
                         years=3)

    # Testing reduce_df()
    filt1 = ~((dfd['cid'] == 'AUD') & (dfd['xcat'] == 'XR'))
    filt2 = ~((dfd['cid'] == 'NZD') & (dfd['xcat'] == 'INFL'))
    dfdx = dfd[filt1 & filt2]  # simulate missing cross sections
    dfd_x1, xctx, cidx = reduce_df(dfdx, xcats=['XR', 'CRY', 'INFL'], cids=cids,
                                   intersect=True, out_all=True)

    dfc = categories_df(dfd, xcats=['XR', 'CRY'], cids=['CAD'],
                        freq='M', lag=0, xcat_aggs=['mean', 'mean'],
                        start='2000-01-01', years=10)