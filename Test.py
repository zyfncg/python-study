import requests

def get_urls(student_id):
    student_url='http://jwas2.nju.edu.cn:8080/jiaowu/Data/Photos/14/'+student_id+'.JPG'
    return student_url

def get_picture(imgUrl):
    local_filename = imgUrl.split('/')[-1]
    # print "Download Image File=", local_filename
    r = requests.get(imgUrl, stream=True) # here we need to set stream = True parameter
    # print(r)
    if 404==r.status_code:
        return 1
    with open("picture/"+local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()
    return 0
if __name__=='__main__':
    institute=['141099','141220','141242','141270','141271','141278','141279']
    thre=0
    for inst in institute:
        for i in range(1,400):
            if i<10:
                endStr='00'+str(i)
            elif  i<100:
                endStr='0'+str(i)
            else:
                endStr=str(i)
            student_id=inst+endStr
            url=get_urls(student_id)
            status=get_picture(url)
            thre=thre+status
            if thre==10:
                thre=0
                break
    print("finsih")

