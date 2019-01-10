import os #引入文件模块
import re #正则表达式
import urllib.request

#连接网页并返回源码
def open_url(url):
      try:
            req = urllib.request.Request(url)
            req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")
            response = urllib.request.urlopen(req)
            # status_code = response.code
            html = response.read()
            return html
      except:
            print(url + " 404 网页丢失，请稍后再试!")
            return 404

def main():
    dongman_url = 'https://www.dongmanxingkong.com/category/pic/wallpaper/page/1'
    dongman_url0 = 'https://www.dongmanxingkong.com/category/pic/wallpaper/page/'
    add_urls = [] # 网页列表
    paper_urls = [] # 壁纸地址列表
    img_num = 1 # 图片序列号
    os.chdir('PC_paper') # 转移到图片防止目录
    for i in range(1,4): # 搜集网页
        dongman_url = dongman_url0 + str(i)
        dongman_html = open_url(dongman_url)
        dongman_html = dongman_html.decode('utf-8')
        # 正则表达式匹配
        add_url = re.findall(r'class="post-title"><a href="([^"]+\.html)" title="【电脑壁纸】', dongman_html)
        print(len(add_url))# 输出当前网页
        add_urls.extend(add_url) # 将子网页添加到列表中
    print(add_urls) # 输出列表
    print(len(add_urls)) # 列表长度
    for i in add_urls: # 从网页列表中搜集图片源地址
        print(i)

        paper_html = open_url(i)
        paper_html = paper_html.decode('utf-8')
        paper_url = re.findall(r'电脑壁纸 " src="([^"]+\.jpg)"',paper_html)
        paper_urls.extend(paper_url) #　将所有地址存放到列表中
        print(paper_url)

    print(paper_urls)
    print('共' + str(len(paper_urls)) + '张,现在开始下载图片，请勿关闭程序!')
    # 开始保存图片
    for i in paper_urls:
        file_name = str(img_num) + '.jpg'
        img_html = open_url(i)
        with open(file_name, 'wb') as f:
            f.write(img_html)
        img_num = img_num + 1


if __name__ == '__main__':
    main()