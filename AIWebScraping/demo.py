from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
AUTH = 'brd-customer-hl_921e7343-zone-ai_scraper_app:ui306c5fy3fn'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

def scrape_website(website):
    print("Launching chrome browser....")
        
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        print('Taking page screenshot to file page.png')  
        driver.get_screenshot_as_file('./page.png')  
        #CAPTCHA handling: If you're expecting a CAPTCHA on the target page, use the following code snippet to check the status of Scraping Browser's automatic CAPTCHA solver
        # print("Waiting captcha to solve....")
        # solve_res=driver.execute('executeCdpCommand',{
        #     'cmd': 'Captcha.waitForSolve',
        #     'params':{'detectTimeout':10000},
        # })
        # print('Captcha solve status:', solve_res['value']['status'])
            
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html
        
        