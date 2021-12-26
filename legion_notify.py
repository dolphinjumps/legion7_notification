#!/usr/bin/env python

# pip install selenium dbus-python
# install chromedriver and specify its path
# https://chromedriver.chromium.org/downloads

from scanner import Scanner
from notification import Notification
import time

URL = 'https://www.lenovo.com/us/en/c/laptops/legion-laptops/legion-7-series'
CHROME_DRIVER_PATH = '/usr/bin/chromedriver'
SCAN_FREQUENCY_IN_MINUTES = 30

def scan_and_notify():
    scanner = Scanner(URL, CHROME_DRIVER_PATH)
    products = scanner.scan_products()


    print_txt = ''

    for product in products:
        print_txt += product.model + " : <b>" + product.final_price + "</b>\n"

    
    # print(print_txt)
    
    notification = Notification()
    notification.notify('', print_txt)

def main():
    starttime = time.time()
    scan_time = 60.0 * SCAN_FREQUENCY_IN_MINUTES

    # run it every SCAN_FREQUENCY_IN_MINUTES
    while True:
        scan_and_notify()
        time.sleep(scan_time - ((time.time() - starttime) % scan_time))

main()
