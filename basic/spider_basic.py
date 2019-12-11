import string
from urllib import error
from urllib import request
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

web_url = "https://so.gushiwen.org/authors/Default.aspx?p={0}&c={1}"

querystring = {"p": "1", "c": "唐代"}

headers = {
    'dnt': "1",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    'sec-fetch-user': "?1",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    'cache-control': "no-cache",
    'postman-token': "8bde7a6a-53dd-fe3a-83a0-8f210f9e2895"
}


def download_page(url):
    try:
        url = quote(url, safe=string.printable)
        req = request.Request(url=url, headers=headers, method="GET")
        html_auth = request.urlopen(req).read().decode('utf-8')
        print(html_auth)
        return html_auth;
    except error.URLError as e:
        if hasattr(e, 'reason'):
            print('错误原因是' + str(e.reason))
    except error.HTTPError as e:
        if hasattr(e, 'code'):
            print('错误状态码是' + str(e.code))
    else:
        print('请求成功通过。')


def confirm_url():
    url = web_url.format('1', '唐代')
    return url


def parase_page(page_str):
    soup = BeautifulSoup(page_str, 'lxml')
    authors = soup.find('/html/body/div[2]/div[1]/div[3]/div[1]/p[2]')


if __name__ == '__main__':
    page_url = confirm_url()
    page_content = download_page(page_url)
    parase_page(page_content)
