from selenium import webdriver

class Browser(object):
    def __init__(self, implicit_wait=10):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(implicit_wait)

    def __enter__(self):
        return self.driver

    def __exit__(self, exception_type, exception_value, traceback):
        if exception_type is not None:
            print(f'Page source:\n\n{self.driver.page_source}\n\n')
        self.driver.quit()