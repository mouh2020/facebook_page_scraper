import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

class Page:
    
    def page_title(self,) :
        try : 
            title = self.driver.title
            if title :
                return title.replace(' | Facebook','') 
        except Exception as e : 
            self.driver.save_screenshot('screenshots/page_title.png')
        





