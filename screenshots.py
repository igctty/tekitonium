import os
import shutil
import datetime

class Screenshot:
  def __init__(self):
    self.i = 0
    self.screenshots_path = './screenshots'
    self.now = datetime.datetime.now.strftime('%Y%m%d%H%M%S')
    # スクショフォルダ掃除
    if os.path.exists(self.screenshots_path):
      shutil.rmtree(self.screenshots_path)

    os.makedirs(self.screenshots_path, exist_ok=True)


  def save(self, driver):
    title = driver.title
    self.i = self.i + 1
    count = format(self.i, '0>3')
    driver.save_screenshot(self.screenshots_path+'/'+self.now+'_'+count+'_'+title+'.png')
    print(self.screenshots_path+'/'+self.now+'_'+count+'_'+title+'.png')