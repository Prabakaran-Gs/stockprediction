from alpha_vantage.timeseries import TimeSeries
def datas(comp_name):
    API_KEY="L8QEIXX6NPFNIXWD"
    ts=TimeSeries(key = API_KEY,output_format='pandas')
    data=ts.get_daily_adjusted(comp_name)
    return data[0]