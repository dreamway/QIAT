#coding=utf-8

def annual_return(df):
    change = df['capital_market_value'].iloc[-1] / df['capital_market_value'].iloc[0] - 1
    annual = pow(change + 1, 250 / len(df)) - 1
    print('总收益为%f，年化收益为%f\n' % (change, annual))


def sharp_ratio(df):
    from math import sqrt
    rf = 0.0284
    change = df['capital_market_value'].iloc[-1] / df['capital_market_value'].iloc[0]
    annual = pow(change, 250 / len(df)) - 1
    volatility = df['profolio_daily_return'].std() * sqrt(250)
    sharp = (annual - rf) / volatility
    print('sharp ratio is %f\n' % sharp)


def average_change(df):
    ave = df['profolio_daily_return'].mean()
    print('平均每日涨幅为%f' % ave)


def max_dramdown(df):
    df['max_value_before_today'] = pd.Series.expanding(df['capital_market_value']).max()
    df['drawdown'] = df['capital_market_value'] / df['max_value_before_today']
    temp = df.sort_values(by='drawdown').iloc[0][['date', 'drawdown']]
    end_date = temp['date']
    maxdd = temp['drawdown']
    maxdd = abs(maxdd - 1)

    start_date = df[df['date'] <= end_date].sort_values(by='capital_market_value', ascending=False).iloc[0]['date']

    print('最大回撤为%f，开始时间为%s，结束时间为%s' % (maxdd, start_date, end_date))
