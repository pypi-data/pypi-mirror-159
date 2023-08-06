import pandas as pd
from joconst.maps import INTERVAL_TDX_MAP
from joconst.object import Interval
from joconst.constant import TdxMarket

from jotdx.utils import to_data, get_stock_market
from jotdx.params import TDXParams
from jotdx.quotes import Quotes


def mootdx_method(symbol):
    quotes = Quotes.factory(market='std')

    df = quotes.xdxr(
        symbol=symbol
    )

    quotes.close()
    print(1)


def pytdx_method(symbol, market):
    from jotdx.hq import TdxHq_API
    from jotdx.utils.best_ip_async import select_best_ip_async

    ip_port_dict = select_best_ip_async(_type="stock")
    ip = ip_port_dict['ip']
    port = ip_port_dict['port']

    api = TdxHq_API()
    with api.connect(ip=ip, port=port):
        bfq_data = api.to_df(api.get_security_bars())
        xdxr_data = get_xdxr_data(api, symbol, market)
        _QA_data_stock_to_fq(bfq_data=bfq_data, xdxr_data=xdxr_data)


def get_xdxr_data(api, symbol, market):
    data = api.to_df(api.get_xdxr_info(market=market, code=symbol))

    category = {
        '1': '除权除息', '2': '送配股上市', '3': '非流通股上市', '4': '未知股本变动',
        '5': '股本变化',
        '6': '增发新股', '7': '股份回购', '8': '增发新股上市', '9': '转配股上市',
        '10': '可转债上市',
        '11': '扩缩股', '12': '非流通股缩股', '13': '送认购权证', '14': '送认沽权证'}

    if len(data) >= 1:
        data = data \
            .assign(date=pd.to_datetime(data[['year', 'month', 'day']], utc=False)) \
            .drop(['year', 'month', 'day'], axis=1) \
            .assign(category_meaning=data['category'].apply(
            lambda x: category[str(x)])) \
            .assign(code=str(symbol)) \
            .rename(index=str, columns={'panhouliutong': 'liquidity_after',
                                        'panqianliutong': 'liquidity_before',
                                        'houzongguben': 'shares_after',
                                        'qianzongguben': 'shares_before'}) \
            .set_index('date', drop=False, inplace=False)
        return data.assign(date=data['date'].apply(lambda x: str(x)[0:10]))
    else:
        return None

    print(1)


def _QA_data_stock_to_fq(bfq_data, xdxr_data, fqtype):
    '使用数据库数据进行复权'
    info = xdxr_data.query('category==1')
    bfq_data = bfq_data.assign(if_trade=1)

    if len(info) > 0:
        data = pd.concat(
            [
                bfq_data,
                info.loc[bfq_data.index[0]:bfq_data.index[-1],
                         ['category']]
            ],
            axis=1
        )

        data['if_trade'].fillna(value=0, inplace=True)
        data = data.fillna(method='ffill')

        data = pd.concat(
            [
                data,
                info.loc[bfq_data.index[0]:bfq_data.index[-1],
                         ['fenhong',
                          'peigu',
                          'peigujia',
                          'songzhuangu']]
            ],
            axis=1
        )
    else:
        data = pd.concat(
            [
                bfq_data,
                info.
                loc[:,
                    ['category',
                     'fenhong',
                     'peigu',
                     'peigujia',
                     'songzhuangu']]
            ],
            axis=1
        )
    data = data.fillna(0)
    data['preclose'] = (
        data['close'].shift(1) * 10 - data['fenhong'] +
        data['peigu'] * data['peigujia']
    ) / (10 + data['peigu'] + data['songzhuangu'])

    if fqtype in ['01', 'qfq']:
        data['adj'] = (data['preclose'].shift(-1) /
                       data['close']).fillna(1)[::-1].cumprod()
    else:
        data['adj'] = (data['close'] /
                       data['preclose'].shift(-1)).cumprod().shift(1).fillna(1)

    for col in ['open', 'high', 'low', 'close', 'preclose']:
        data[col] = data[col] * data['adj']
    # data['volume'] = data['volume'] / \
    #     data['adj'] if 'volume' in data.columns else data['vol']/data['adj']

    data['volume'] = data['volume']  if 'volume' in data.columns else data['vol']
    try:
        data['high_limit'] = data['high_limit'] * data['adj']
        data['low_limit'] = data['low_limit'] * data['adj']
    except:
        pass
    return data.query('if_trade==1 and open != 0').drop(
        ['fenhong',
         'peigu',
         'peigujia',
         'songzhuangu',
         'if_trade',
         'category'],
        axis=1,
        errors='ignore'
    )


def std_bars_test():

    symbol = "123075"
    symbol = "300001"
    market = get_stock_market(symbol=symbol)


    # mootdx_method(symbol=symbol)
    pytdx_method(symbol=symbol, market=market)


if __name__ == '__main__':
    std_bars_test()
