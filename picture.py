#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

part_url = 'http://www.nm.zsks.cn'
institute=['141099','141220','141242','141270','141271','141278','141279']
def get_detail(url,school_id):
    print url
    resp = requests.get(url)
    resp.encoding = 'gbk'
    bs = BeautifulSoup(resp.text, 'lxml')
    subject_ids = bs.select('.report1_3_6')
    subject_names = bs.select('.report1_3_1')
    nums_grade = bs.select('.report1_4_3')
    subject_ids = subject_ids[3:]
    subject_names = subject_names[5::2]
    nums = nums_grade[0::4]
    min_grades = nums_grade[1::4]
    subject=[]

def get_urls(student_id):
    student_url='http://jwas2.nju.edu.cn:8080/jiaowu/Data/Photos/14/'+student_id+'.JPG'
    return student_url

def get_picture(imgUrl):
    local_filename = imgUrl.split('/')[-1]
    print "Download Image File=", local_filename
    r = requests.get(imgUrl, stream=True) # here we need to set stream = True parameter
    with open("/home/pandy/"+local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()
    pass

def get_data(url):

    response=requests.get(url)
    response.encoding = 'gbk'
    soup=BeautifulSoup(response.text,'lxml')
    #print (response.text.encode(response.encoding).decode('utf-8'))
    id_name=soup.select('.report1_4_1')
    statis=soup.select('.report1_4_3')
    urls=soup.select('td > a')
    if year==2014:
        school_urls=urls[0:len(urls):2]
        ids= id_name[0:len(id_name):2]
        names= id_name[1:len(id_name):2]
    else:
        school_urls=urls[1:len(urls):3]
        ids= id_name[0:len(id_name):3]
        names= id_name[1:len(id_name):3]
    plans=statis[0:len(statis):7]
    grades=statis[3:len(statis):7]



if __name__=='__main__':
    type = 2
    url = 'http://www.nm.zsks.cn/zy_3_1_2014/3_B_11.html'
    year = 2014
    get_data(url)

    print 'finish'



