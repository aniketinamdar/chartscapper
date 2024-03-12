import asyncio
import time
from pyppeteer import launch
import os

async def get_chart_timeinterval_driver(stock_ticker,save_location,time_interval_list):
    start = time.time()
    # ticker = 'SBIN'
    ticker = stock_ticker
    # download_directory = r'D:\Work\pypi\v2\images'
    download_directory = save_location

    browser = await launch(
        headless=True,
        args=[
            '--no-sandbox',
            '--disable-dev-shm-usage',
            f'--disable-setuid-sandbox',
            f'--download.default_directory={download_directory}',
        ]
    )
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})
    await page.goto(f'https://www.tradingview.com/chart/?symbol=NSE%3A{ticker}')
    print("Link loaded")
    # Before navigating to the page, set the download behavior
    await page._client.send('Page.setDownloadBehavior', {
        'behavior': 'allow',
        'downloadPath': download_directory
    })

    try:
        charts = 'body > div.js-rootresizer__contents.layout-with-border-radius > div.layout__area--center > div.chart-container.single-visible.top-full-width-chart.active > div.chart-container-border > div > div.chart-markup-table > div:nth-child(1) > div.chart-markup-table.pane > div > canvas:nth-child(2)'
        await page.waitForSelector(charts, timeout=10000)

        #Time zone manager
        time_button = 'body > div.js-rootresizer__contents.layout-with-border-radius > div.layout__area--center > div.chart-toolbar.chart-controls-bar > div > div.seriesControlWrapper-BXXUwft2 > div:nth-child(1) > div > button'
        india_local_time = '#overlap-manager-root > div > div.menu-Tx5xMZww.context-menu.menuWrap-Kq3ruQo8 > div > div > table > tbody > tr:nth-child(139) > td:nth-child(2)'
        await page.waitForSelector(time_button, timeout=10000)
        await page.click(time_button)
        await asyncio.sleep(0.2)

        await page.waitForSelector(india_local_time, timeout=10000)
        await page.click(india_local_time)

        # charts = '/html/body/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div'

        await asyncio.sleep(0.5)
        # await page.keyboard.type('1d')
        for time_interval in time_interval_list:
            await page.keyboard.type(time_interval)
            await page.keyboard.press('Enter')
            print('Time Interval sent')

            await asyncio.sleep(1)

            header_toolbar_screenshot = '#header-toolbar-screenshot'
            await page.waitForSelector(header_toolbar_screenshot, timeout=10000)
            await page.click(header_toolbar_screenshot)

            save_chart_image = '#overlap-manager-root > div > span > div.menuWrap-Kq3ruQo8 > div > div > div:nth-child(2)'
            await page.waitForSelector(save_chart_image, timeout=10000)
            await page.click(save_chart_image)
            print("Image Downloaded")

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        end = time.time()
        await asyncio.sleep(3)
        await browser.close()

        print(end - start)

async def get_multiple_charts_timeinterval_driver(ticker_list,path,interval_list):
    start = time.time()
    await asyncio.gather(*(get_chart_timeinterval_driver(t,path,interval_list) for t in ticker_list))
    end = time.time()
    print(f"Time taken: {end-start}")

async def get_chart_timeperiod_driver(stock_ticker,save_location,time_period):
    start = time.time()
    # ticker = 'SBIN'
    ticker = stock_ticker
    # download_directory = r'D:\Work\pypi\v2\images'
    download_directory = save_location

    browser = await launch(
        headless=True,
        args=[
            '--no-sandbox',
            '--disable-dev-shm-usage',
            f'--disable-setuid-sandbox',
            f'--download.default_directory={download_directory}',
        ]
    )
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})
    await page.goto(f'https://www.tradingview.com/chart/?symbol=NSE%3A{ticker}')
    print("Link loaded")
    # Before navigating to the page, set the download behavior
    await page._client.send('Page.setDownloadBehavior', {
        'behavior': 'allow',
        'downloadPath': download_directory
    })

    try:
        charts = 'body > div.js-rootresizer__contents.layout-with-border-radius > div.layout__area--center > div.chart-container.single-visible.top-full-width-chart.active > div.chart-container-border > div > div.chart-markup-table > div:nth-child(1) > div.chart-markup-table.pane > div > canvas:nth-child(2)'
        await page.waitForSelector(charts, timeout=10000)

        #Time zone manager
        time_button = 'body > div.js-rootresizer__contents.layout-with-border-radius > div.layout__area--center > div.chart-toolbar.chart-controls-bar > div > div.seriesControlWrapper-BXXUwft2 > div:nth-child(1) > div > button'
        india_local_time = '#overlap-manager-root > div > div.menu-Tx5xMZww.context-menu.menuWrap-Kq3ruQo8 > div > div > table > tbody > tr:nth-child(139) > td:nth-child(2)'
        await page.waitForSelector(time_button, timeout=10000)
        await page.click(time_button)
        await asyncio.sleep(0.2)

        await page.waitForSelector(india_local_time, timeout=10000)
        await page.click(india_local_time)

        # charts = '/html/body/div[2]/div[5]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div'

        await asyncio.sleep(0.5)
        # await page.keyboard.type('1d')
        time_date = {'1D':'1','5D':'2','1M':'3','3M':'4','6M':'5','YTD':'6','1Y':'7','5Y':'8','ALL':'9'}
        if time_period in time_date:
            value = time_date[time_period]
        else:
            print("Time period entered is incorrect")


        # time_period_button = f'body > div.js-rootresizer__contents.layout-with-border-radius > div.layout__area--center > div.chart-toolbar.chart-controls-bar > div > div:nth-child(2) > div > div > button:nth-child({value})'
        time_period_button = f'/html/body/div[2]/div[5]/div[1]/div/div[2]/div/div/button[{value}]'
        # await page.waitForSelector(time_period_button,timeout = 10000)
        await page.waitForXPath(time_period_button,timeout = 10000)
        await page.click(time_period_button)
        print('Time interval sent')

        await asyncio.sleep(1)

        header_toolbar_screenshot = '#header-toolbar-screenshot'
        await page.waitForSelector(header_toolbar_screenshot, timeout=10000)
        await page.click(header_toolbar_screenshot)

        save_chart_image = '#overlap-manager-root > div > span > div.menuWrap-Kq3ruQo8 > div > div > div:nth-child(2)'
        await page.waitForSelector(save_chart_image, timeout=10000)
        await page.click(save_chart_image)
        print("Image Downloaded")


    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        end = time.time()
        await asyncio.sleep(3)
        await browser.close()

        print(end - start)

async def get_multiple_charts_timeperiod_driver(ticker_list,path,interval_list):
    start = time.time()
    await asyncio.gather(*(get_chart_timeperiod_driver(t,path,interval_list) for t in ticker_list))
    end = time.time()
    print(f"Time taken: {end-start}")
