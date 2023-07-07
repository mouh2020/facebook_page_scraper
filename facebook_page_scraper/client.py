from pages.login_page import Login
from pages.page_page import Page
from pages.post_page import Post
from selenium import webdriver
from selenium.webdriver.common import action_chains,keys
class Client(Login,
             Page,
             Post):
    
    def __init__(self,page_id) :
        self.page_id  = page_id
        self.driver   = webdriver.Chrome()
        self.__get_page()

    @property
    def page_url(self) : 
        return f"https://facebook.com/{str(self.page_id)}"

    def __get_page(self) :
        try : 
            self.driver.get(self.page_url)
        except Exception as e : 
            self.driver.save_screenshot('screenshots/__get_page.png')
    
    def __kill_login_page(self) : 
        try : 
            if 'aria-label="Close"' in self.driver.switch_to.active_element.get_attribute('innerHTML') :
                action_chains.ActionChains(self.driver).send_keys(keys.Keys.SPACE)
        except Exception as e : 
            self.driver.save_screenshot('screenshots/__kill_login_page.png')       


    
    