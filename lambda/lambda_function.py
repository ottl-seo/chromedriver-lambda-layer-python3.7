import boto3
import json
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
import os, io
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebDriver(object):
    def __init__(self):
        self.options = Options()
        self.options.binary_location = '/opt/headless-chromium'
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--start-fullscreen')
        self.options.add_argument('--single-process')
        self.options.add_argument('--disable-dev-shm-usage')

    def get(self):
        driver = Chrome('/opt/chromedriver', options=self.options)
        return driver

def lambda_handler(event, context):
    
    # 크롤링
    instance_ = WebDriver()
    driver = instance_.get()
    driver.get('https://google.com/')

    driver.maximize_window()
    time.sleep(1)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Done')
    }
    
if __name__ == "__main__":
    lambda_handler(None, None)
