from selenium import webdriver
import re  # 正则表达式模块
import time
import requests



def main(html_url):
    browser = webdriver.Chrome()
    browser.get(html_url)

    for i in range(0,200):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print(f"================================{i}================================")
        time.sleep(2)
    # 爬取完整的
    # while(True):
    #     # 执行js脚本返回当前页面高度
    #     height = browser.execute_script("return document.body.scrollHeight;");
    #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(2)
    #     # 下滑完了,再次检查当前页面高度,如果滑到底部,则两次高度相同
    #     newHeight = browser.execute_script("return document.body.scrollHeight;")
    #     if height == newHeight :
    #         break;
        

    source = browser.page_source
    browser.close()
    obj = re.compile(r"<source src=\"(?P<url>.*?)\" type=\"video/mp4\">")
    video_urls = obj.finditer(source)
   
    for tmp in video_urls:
        download(tmp.group("url"))

def download(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    dir_name = '/Volumes/US100 2TB/videos/'
    # video_real_url = requests.get(url=url, headers=headers, allow_redirects=True).url
    file = dir_name + url[url.rfind("/")+1:url.find("?")]
    with open(file, mode='wb') as f:
        response = requests.get(url=url, headers=headers, allow_redirects=True)
        f.write(response.content)
        response.close()
        f.close()
        print(f'视频：{file}----------下载完成')

if __name__ == '__main__':
    url = "https://www.pexels.com/zh-cn/search/videos/%E7%8B%97/"
    # url = "https://player.vimeo.com/external/363977237.sd.mp4?s=2dd5036d66646b9032a4309bfd232b645f8fff9f&amp;profile_id=164&amp;oauth2_token_id=57447761"
    main(url)