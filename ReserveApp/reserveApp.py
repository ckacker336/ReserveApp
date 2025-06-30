from selenium import webdriver
from selenium.webdriver.edge.service import Service 
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from datetime import datetime
import sched, time
import requests
import datetime

#先にEdgeを立ち上げておく
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)
driver.implicitly_wait(100)

def reserve_doctor(): 
    url = "XXX"
    id = "XXX"
    password = "XXX"

    driver.get(url)
    #「午前を受付」ボタンを押す
    login_bottun = driver.find_element(By.CSS_SELECTOR,"#group-all-menu > div > div.box__content > div.group-box.furiwake-box--g1 > div.group-box__content > div.group-next-button-wrapper > a") 
    login_bottun.click() 

    #「受診したことがある人」ボタンを押す
    login_bottun = driver.find_element(By.CSS_SELECTOR,"#ymake") 
    login_bottun.click() 

    #「診察券番号」を入力する
    user_input = driver.find_element(By.CSS_SELECTOR,"#id1")    
    user_input.send_keys(id)

    #「パスワード」を入力する
    user_input = driver.find_element(By.CSS_SELECTOR,"#birth1")    
    user_input.send_keys(password)

    #「認証するボタン」を押す
    login_bottun = driver.find_element(By.CSS_SELECTOR,"#form1 > div.button-wrapper-reserve > input") 
    login_bottun.click()

    #「はい」ボタンを押す（情報の確認）
    login_bottun = driver.find_element(By.CSS_SELECTOR,"body > div.header-sub-box-wrapper > div.box-wrapper > div.box > div:nth-child(4) > div:nth-child(3) > a") 
    login_bottun.click()

    #予約種類の選択（診察）
    # ドロップダウンリストを取得するためにid:Dropdown の要素を取得
    dropdown = driver.find_element(By.CSS_SELECTOR,"#form1 > div.select-md-wrapper > select")
    # Select オブジェクトを生成。
    select = Select(dropdown)
    # インデックスなので1つ目の選択肢は0からスタート。
    select.select_by_index(1) 

    #次へを押す
    login_bottun = driver.find_element(By.CSS_SELECTOR,"#submit1") 
    login_bottun.click()

    #「受付する」ボタンを押す
    login_bottun = driver.find_element(By.CSS_SELECTOR,"body > div.header-sub-box-wrapper > div.box-wrapper > div.box > div.button-wrapper-reserve > a") 
    login_bottun.click()

    #「受付する」ボタンを押す
    login_bottun = driver.find_element(By.CSS_SELECTOR,"body > div.header-sub-box-wrapper > div.box-wrapper > div.box > div.button-wrapper-reserve > a") 


#テスト用
#reserve_doctor() 

#時間設定：日付はアプリ起動した日・時間は7時半固定
#YYYY MM DD形式で書く。2025年3月31日なら2025 03 31というように記載。
scheduler = sched.scheduler(time.time, time.sleep)

dt = datetime.datetime.today()
dym = dt.strftime('%Y %m %d')
reserveTime = "07:30:00"

dymhms = f'{dym} {reserveTime}'
target_time = time.strptime(dymhms, "%Y %m %d %H:%M:%S") 
target_timestamp = time.mktime(target_time)

#スケジューラに関数と時間を設定
scheduler.enterabs(target_timestamp, 1, reserve_doctor, ())
scheduler.run()