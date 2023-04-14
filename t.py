from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import csv
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
# 打开浏览器并访问页面
url = 'https://www.facebook.com/groups/1260448967306807/'
driver = webdriver.Chrome(r"C:\Users\yrz52\Downloads\chromedriver_win32\chromedriver.exe")
driver.get(url)
time.sleep(4)

# 点击 "See More" 按钮，直到没有更多内容

for x in range(10):
    # x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f
    
    # element = driver.find_elements_by_xpath("//div[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f' and @role='button']")
    # for el in element:
    #     driver.execute_script("arguments[0].click();", el)
    #     time.sleep(1)
    # element_2 = driver.find_elements_by_xpath("//div[@class='x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz x6s0dn4 xi81zsa x1iyjqo2 xs83m0k xsyo7zv xt0b8zv' and @role='button']//span[@class='x78zum5 x1w0mnb xeuugli']//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f xi81zsa' and @dir='auto']")
    # for el in element_2:
    #     driver.execute_script("arguments[0].click();", el)
    #     time.sleep(1)  
    try:
        element_1 = driver.find_elements_by_xpath("//div[@class='x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz x6s0dn4 xi81zsa x1iyjqo2 xs83m0k xsyo7zv xt0b8zv' and @role='button']//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f xi81zsa' and @dir='auto']")
        if len(element_1):
            for el in element_1:
                driver.execute_script("arguments[0].click();", el)
                try:
                    element = driver.find_element_by_xpath("//div[@role='button' and contains(text(), '顯示更多')]")
                    driver.execute_script("arguments[0].click();", element)
                except:
                    continue
                time.sleep(1)
    except StaleElementReferenceException:
        element_1 = driver.find_elements_by_xpath("//div[@class='x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz x6s0dn4 xi81zsa x1iyjqo2 xs83m0k xsyo7zv xt0b8zv' and @role='button']//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f xi81zsa' and @dir='auto']")
    try:
        element_2 = driver.find_elements_by_xpath("//div[@class='x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz x6s0dn4 xi81zsa x1iyjqo2 xs83m0k xsyo7zv xt0b8zv' and @role='button']//span[@class='x78zum5 x1w0mnb xeuugli']//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f xi81zsa' and @dir='auto']")
        if len(element_2):
            for ell in element_2:
                driver.execute_script("arguments[0].click();", ell)
                time.sleep(1)
    except StaleElementReferenceException:
        element_2 = driver.find_elements_by_xpath("//div[@class='x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz x6s0dn4 xi81zsa x1iyjqo2 xs83m0k xsyo7zv xt0b8zv' and @role='button']//span[@class='x78zum5 x1w0mnb xeuugli']//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f xi81zsa' and @dir='auto']")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
soup = BeautifulSoup(driver.page_source, 'html.parser')
titles = soup.find_all("div", class_='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z')
with open('fb.csv', 'w',encoding='utf-16',newline='') as csvfile:
    fieldnames = ['貼文','留言']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter='\t')
    writer.writeheader()
    for title in titles:
        # 定位每一行標題
        
        posts = title.find_all("div", dir="auto")
        # print("貼文"+"-" * 30)
        # 如果有文章標題才印出
        if len(posts):
            for post in posts:
                    writer.writerow({'貼文': post.text})
                # print(post.text)
                    break
        # print("留言"+"-" * 30)
        commd = title.find_all("div",class_='x11i5rnm xat24cr x1mh8g0r x1vvkbs xdj266r')
        if len(commd):    
            for co in commd:
                writer.writerow({'留言': co.text})

        # print("-" * 30)
print("OK")
