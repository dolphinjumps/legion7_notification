from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from product import Product

class Scanner:
    def __init__(self, url, driver_path):

        self.url = url
        
        # Open chrome without opening GUI
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')

        self.driver_path = driver_path

    def scan_products(self):
        driver = webdriver.Chrome(self.driver_path, chrome_options=self.chrome_options)

        driver.get(self.url)

        product_tags = driver.find_elements(By.CLASS_NAME, 'product_right')
        products = []
        
        for product_tag in product_tags:
            model = product_tag.find_element(By.CLASS_NAME, "lazy_href").text
            final_price = product_tag.find_element(By.CLASS_NAME, "final_price").text
            specs = product_tag.find_element(By.CLASS_NAME, "specs").text

            product = Product(model, final_price, specs)
            
            products.append(product)
        driver.close()

        return products
