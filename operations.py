from time import sleep
from weakref import WeakValueDictionary
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.Keys import Keys
from selenium.webdriver.chrome.service import Service

class Operation():
  def __init__(self):
    self.service = Service(executable_path="./_internal/chromedriver")
    self.driver = webdriver.Chrome(service=self.service)
    self.options = webdriver.ChromeOptions()
    self.options.add_argument('--headless')
    self.options.add_argument('--window-size=1920,1080')
    self.wait = WebDriverWait(self.driver, 10)


  def move(self, url):
    print("move: "+ url)
    self.driver.get(url)


  def click(self, locator):
    print("click: "+ locator)
    self.element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
    self.element.click()


  def input(self, locator, text):
    print("input: "+ locator)
    self.element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
    self.element.clear()
    self.element.send_keys(text)


  def check(self, locator):
    print("check: "+ locator)
    self.element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
    if not(self.element.is_selected()):
      self.element.click()


  def select(self, locator, value):
    print("select: "+ locator)
    self.element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
    selector = Select(self.element)
    if (selector.select_by_visible_text(value)):
      selector.select_by_visible_text(value)