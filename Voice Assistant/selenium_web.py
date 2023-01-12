from selenium import webdriver
class youtube():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='D:\\chromedriver_win32\\chromedriver.exe')
    
    def play(self, query):
        self.query=query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        search = self.driver.find_element_by_xpath('//*[@id="meta"]')
        search.click()
#class infow():
    #def __init__(self):
     #   self.driver = webdriver.Chrome(executable_path='D:\\chromedriver_win32\\chromedriver.exe')
    
    #def get_info(self, query):
       # self.query=query
        #self.driver.get(url="https://www.wikipedia.org")
       # search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
      #  search.click()
     #    enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
   #     enter.click()

