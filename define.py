import requests
from requests import Session
open('log.txt','a')

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'origin': 'https://hocmai.vn',
    'referer': 'https://hocmai.vn/loginv2/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}



baseurl = 'https://hocmai.vn/loginv2/index.php'
user = 'hunghunghungle@gmail.com'
pwd = 'Lehung2808@'

rq = Session()

open_page = rq.get(baseurl,headers=headers)


files = {
    'a': (None, ''),
    'username': (None, user),
    'password': (None, pwd),
}

response = rq.post(baseurl, headers=headers, files=files)

print('get_login')


course_url = 'https://hocmai.vn/khoa-hoc-truc-tuyen/1292/phong-luyen-pen-vat-li.html'
data = rq.get(course_url).text
course_list = []
for i in range(data.count('class="learn-lesson-wr"')):
    data = data[data.index('class="learn-lesson-wr"'):]
    data = data.replace('class="learn-lesson-wr"','',1)
    url = data.split('href="')[1].split('"')[0]
    course_list.append(url)
for i in course_list:print(i)


#open('log.txt','w',encoding='utf-8').write(data.text)