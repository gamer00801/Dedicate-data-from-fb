import csv
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# 打開瀏覽器去CostcoFB
url = "https://www.facebook.com/groups/1260448967306807/"
# 创建ChromeOptions对象
chrome_options = Options()

# 设置headless模式
chrome_options.add_argument('--headless')
# 安裝驅動程式

driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
driver.get(url)
# 等待網頁出現
time.sleep(4)
# 往下滑動10次並展開貼文以及留言
for x in range(10):
    try:
        element_1 = driver.find_elements_by_xpath(
            "//div[@class='x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz x6s0dn4 xi81zsa x1iyjqo2 xs83m0k xsyo7zv xt0b8zv' and @role='button']//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f xi81zsa' and @dir='auto']"
        )
        if len(element_1):
            for el in element_1:
                driver.execute_script("arguments[0].click();", el)
                try:
                    element = driver.find_element_by_xpath(
                        "//div[@role='button' and contains(text(), '顯示更多')]"
                    )
                    driver.execute_script("arguments[0].click();", element)
                except:
                    continue
                time.sleep(2)
    except StaleElementReferenceException as e:
        element_1 = driver.find_elements_by_xpath(
            "//div[@class='x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz x6s0dn4 xi81zsa x1iyjqo2 xs83m0k xsyo7zv xt0b8zv' and @role='button']//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f xi81zsa' and @dir='auto']"
        )
    try:
        element_2 = driver.find_elements_by_xpath(
            "//div[@class='x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz x6s0dn4 xi81zsa x1iyjqo2 xs83m0k xsyo7zv xt0b8zv' and @role='button']//span[@class='x78zum5 x1w0mnb xeuugli']//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f xi81zsa' and @dir='auto']"
        )
        if len(element_2):
            for ell in element_2:
                driver.execute_script("arguments[0].click();", ell)
                time.sleep(2)
    except StaleElementReferenceException as e:
        element_2 = driver.find_elements_by_xpath(
            "//div[@class='x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz x6s0dn4 xi81zsa x1iyjqo2 xs83m0k xsyo7zv xt0b8zv' and @role='button']//span[@class='x78zum5 x1w0mnb xeuugli']//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f xi81zsa' and @dir='auto']"
        )
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
# 抓取貼文以及留言
soup = BeautifulSoup(driver.page_source, "html.parser")
titles = soup.find_all("div", class_="x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z")
# 存放到CSV檔中
with open("fb.csv", "w", encoding="utf-16", newline="") as csvfile:
    # 欄位:貼文和留言
    fieldnames = ["貼文", "留言"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter="\t")
    writer.writeheader()
    for title in titles:
        posts = title.find_all("div", dir="auto")
        # 如果有文章標題才印出
        if len(posts):
            for post in posts:
                # 找到標題就退出迴圈
                writer.writerow({"貼文": post.text})
                break
        # 找出留言
        commd = title.find_all(
            "div", class_="x11i5rnm xat24cr x1mh8g0r x1vvkbs xdj266r"
        )
        # 有留言才開始印出
        if len(commd):
            for co in commd:
                writer.writerow({"留言": co.text})
#關閉瀏覽器
driver.quit()

