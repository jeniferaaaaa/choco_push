import time
import logging
from config import config
from module import date
from module import hantei
from selenium import webdriver


#ドライバー読み込み
driver = webdriver.Chrome('./driver/chromedriver.exe')

#日付取得
now = date.getNowDate()

#ログレベルセット
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#実行判定
hanteiResult = hantei.judgeTime(now)
if hanteiResult == False:
    driver.quit()

#アクセスURL
driver.get('')
time.sleep(3)

#ログイン
syainNumElement = driver.find_element_by_name('username')
syainNumElement.send_keys(config.getUserNum())
passwordElement = driver.find_element_by_name('password')
passwordElement.send_keys(config.getUserPass())
buttonElement = driver.find_element_by_xpath('//*[@id="btnLogin"]/input').click()
time.sleep(5)

#出社ボタンクリック
timeButtonElement = driver.find_element_by_id('OfficeGoBtn')
timeButtonElement.click()
time.sleep(5)

#処理が終了したらログを吐く
#ハンドラ取得
get_handler = logging.FileHandler('log/success.log')
logger.addHandler(get_handler)

#ログメッセージ
msg = 'にちょこきんを押したよ。'

logger.info(now + msg)

#終了
driver.quit()

