# Dedicate-data-from-fb

## FB costco社團豹蟲
<小時>
使用selenium中的webdriver，打開瀏覽器之前要先取的網址
fb屬於動態網頁，
要使用driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")模擬滑鼠滾動，
使用迴圈滾動並展開每則貼文以及留言後，
一次刷取全部貼文以及留言並保存在CSV文件中。
