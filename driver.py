import asyncio
import time
from pyppeteer import launch
import os
from main import get_chart_timeinterval_driver, get_multiple_charts_timeinterval_driver,get_chart_timeperiod_driver,get_multiple_charts_timeperiod_driver

def get_chart_timeinterval(ticker,path,interval_list):
    asyncio.run(get_chart_timeinterval_driver(ticker, path, interval_list))

def get_multiple_charts_timeinterval(ticker_list,path,interval_list):
    asyncio.run(get_multiple_charts_timeinterval_driver(ticker_list,path,interval_list))

def get_charts_timeperiod(ticker_list,path,timeperiod):
    asyncio.run(get_chart_timeperiod_driver(ticker_list,path,timeperiod))

def get_multiple_charts_timeperiod(ticker_list,path,timeperiod):
    asyncio.run(get_multiple_charts_timeperiod_driver(ticker_list,path,timeperiod))


ticker =['HDFCBANK','YESBANK']
path = r'D:\Work\pypi\v2\images'
tp = '5D'

get_charts_timeperiod(ticker,path,tp)