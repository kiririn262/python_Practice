import time
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

user_name = "t170521"
passward = "ared5849"
url = 'https://qiita.com/drafts/new'
DRIVER_PATH = (r'D:\python\msedgedriver.exe')
# DRIVER_PATH = (r'D:\python\chromedriver.exe')
text_title = "スタンプ型デバイス~ ~"
tag = "Unity3D Unity hololens2 "
text_body = "####まえがき\n\n####本題\n\n#####機器概要\n\n####手順\n\n1. \n\n2. \n\n3. \n\n####実行例\n\n####あとがき\n\n####参考"

# ブラウザの起動
driver = webdriver.Edge(executable_path=DRIVER_PATH)
# driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

# ログイン処理
user_box = driver.find_element_by_id('identity')
user_box.send_keys(user_name)
pass_box = driver.find_element_by_id('password')
pass_box.send_keys(passward)
pass_box.submit()
time.sleep(2)

# 自動でフォーマット作成
new_title = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div/div/input')
new_title.send_keys(text_title)
new_tag = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/input')
new_tag.send_keys(tag)
new_body = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[3]/div/div[1]/div[2]/textarea')
new_body.send_keys(text_body)
time.sleep(2)

# 下書き保存
# <a href="#" tabindex="43" class="MarkdownEditorFooterSelector__DropdownItem-sc-11l11zp-4 fUjZzp"><i class="fa fa-check"></i><i class="fa fa-save"></i>下書き保存</a>
# save = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[4]/div/div[2]/div[2]/div/ul/li[1]/a')
# save.click()
# button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[4]/div/div[2]/div[2]/div/button')
# button.click()
driver.quit()

driver = webdriver.Edge(executable_path=DRIVER_PATH)
driver.get('https://qiita.com/drafts')
time.sleep(2)

# ログイン処理
user_box = driver.find_element_by_id('identity')
user_box.send_keys(user_name)
pass_box = driver.find_element_by_id('password')
pass_box.send_keys(passward)
pass_box.submit()