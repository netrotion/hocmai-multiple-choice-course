from time import sleep
from requests import Session
import requests
import os
#module import python-docx (must be install)
class main:
    def __init__(self):
        self.user = 'hunghunghungle@gmail.com'
        self.pwd = 'Lehung2808@'
        self.rq = Session()

    def clrscr(self):
        if os.name == 'posix':os.system('clear')
        else:os.system('cls')

    def login(self):
        headers = {
            'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language'           : 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control'             : 'max-age=0',
            'dnt'                       : '1',
            'origin'                    : 'https://hocmai.vn',
            'referer'                   : 'https://hocmai.vn/loginv2/',
            'sec-ch-ua'                 : '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile'          : '?0',
            'sec-ch-ua-platform'        : '"Windows"',
            'sec-fetch-dest'            : 'document',
            'sec-fetch-mode'            : 'navigate',
            'sec-fetch-site'            : 'same-origin',
            'sec-fetch-user'            : '?1',
            'upgrade-insecure-requests' : '1',
            'user-agent'                : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        }

        files = {
            'a': (None, ''),
            'username': (None, self.user),
            'password': (None, self.pwd),
        }

        baseurl   = 'https://hocmai.vn/loginv2/index.php'
        open_page = self.rq.get(baseurl,headers=headers)
        get_login = self.rq.post(baseurl, headers=headers, files=files)
        if 'student-name' in get_login.text:
            return True
        return False
    
    def show_course(self):#ham liet ke du lieu khoa hoc
        self.clrscr()
        course_url = 'https://hocmai.vn/course/mycourse2.php'
        data = self.rq.get(course_url).text
        total_course = data.count('data-state="studying"') #so khoa hoc da dang ky
        
        if total_course == 0:return

        url_list = []

        print(f'Tong khoa hoc: {total_course}')

        for i in range(total_course):#lay danh sach khoa hoc
            data = data[data.index('data-state="studying"'):]
            data = data.replace('data-state="studying"','',1)
            name = data.split('alt="')[1].split('"')[0]
            url = data.split('href="')[1].split('"')[0]
            url_list.append(url)
            print('\t\t'+str(i)+'.',name)
        choose = input('\n-Chon khoa hoc can tai tai lieu: ')
        return url_list[int(choose)]

    def scrape(self,url):
        def online_tn(data):
            pass
        if 'phong-luyen' in url:
            print(url)


if __name__ == '__main__':
    r = main()
    r.login()
    r.scrape(r.show_course())


