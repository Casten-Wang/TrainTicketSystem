from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import re
import datetime
import csv


chrome_options = Options()
# chrome_options.add_argument('--disable-gpu')  # 如果不加这个选项，有时定位会出现问题

# 启动浏览器，获取网页源代码 chrome_options=chrome_options
browser = webdriver.Chrome()
browser.maximize_window()
origin = "北京"
destination = "长沙"

myurl = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
browser.get(myurl)
browser.find_element_by_xpath("/html/body/div[48]/div[2]/div[2]/div[2]/a").click()

browser.find_element_by_xpath("/html/body/div[7]/div[4]/form/div[2]/ul/li[1]/div/input[2]").click()
browser.find_element_by_xpath("/html/body/div[7]/div[4]/form/div[2]/ul/li[1]/div/input[2]").send_keys(origin)
browser.find_element_by_xpath("/html/body/div[7]/div[4]/form/div[2]/ul/li[1]/div/input[2]").send_keys(Keys.ENTER)

browser.find_element_by_xpath("/html/body/div[7]/div[4]/form/div[2]/ul/li[3]/div/input[2]").click()
browser.find_element_by_xpath("/html/body/div[7]/div[4]/form/div[2]/ul/li[3]/div/input[2]").send_keys(destination)
browser.find_element_by_xpath("/html/body/div[7]/div[4]/form/div[2]/ul/li[3]/div/input[2]").send_keys(Keys.ENTER)


parent = browser.find_element_by_xpath('//*[@id="date_range"]')
child = parent.find_elements_by_tag_name('li')
datas = []
for everyday in child[1:4]:
    everyday.click()
    time.sleep(3)
    message = []
    # 获取日期
    date = browser.find_element_by_xpath('//*[@id="sear-result"]/p[1]/strong[1]')
    date = date.text
    print(date)
    a = browser.find_elements_by_xpath("//*[@class='bgc']")
    for i in a[:-1]:
        print(i.text)
        message.append(i.text)

    time.sleep(3)
    a = browser.find_elements_by_xpath("//*[@class='bgc']")
    for i in a[0:1]:
        child = i.find_elements_by_tag_name('td')
        child[4].click()
    time.sleep(3)
    allprice = browser.find_element_by_xpath("/html/body/div[8]/div[7]/table/tbody[1]/tr[2]")
    allprice = allprice.text
    print(allprice)

    # 数据清洗
    # 重复的数据
    a = re.findall('(\d*)月(\d*)', date)[0]
    month = int(a[0])
    day = int(a[1])
    a = re.findall('(\d*)\.', allprice)
    b = list(map(int, a))
    price = min(b)
    maxpeople = 20

    # 遍历的数据
    for text in message:
        a = re.search('.\d*', text)
        train = a.group()
        a = re.findall('\d\d:\d\d', text)
        begintime = a[0]
        begintimehour = int(begintime.split(':')[0])
        begintimemin = int(begintime.split(':')[1])
        endtime = a[1]
        endtimehour = int(endtime.split(':')[0])
        endtimemin = int(endtime.split(':')[1])
        a = re.search('..到达', text)
        now_or_tom = a.group()
        begintime = datetime.datetime(2021, month, day, begintimehour, begintimemin)
        endtime = datetime.datetime(2021, month, day, endtimehour, endtimemin)
        if now_or_tom == "次日到达":
            endtime += datetime.timedelta(days=1)
        row = []
        row.append(train)
        row.append(maxpeople)
        row.append(begintime)
        row.append(endtime)
        row.append(origin)
        row.append(destination)
        row.append(price)
        row.append("A0002")
        datas.append(row)

browser.quit()

with open('D:\\数据库实训\\Flask\\SQL操作\\数据csv\\Train.csv', 'a', newline='', encoding="utf-16") as f:
    writer = csv.writer(f)
    writer.writerows(datas)
