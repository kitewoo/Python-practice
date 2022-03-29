import os
import tqdm
import time
from urllib import request

def makedir(keyword):

    fdir="C:/Users/tt/Desktop/pycode/images"

    if os.path.exists(fdir):  # 폴더가 있다면 뒤쪽에 "/"만 연결
        fdir += "/"
    else:
        os.makedirs(fdir)     # 폴더가 없다면 폴더 생성후 뒤쪽에 "/"만 연결
        fdir += "/"

    # images 폴더에 검색 키워드를 이용해 폴더 생성후 저장
    # 키워드와 동일한 폴더가 있는 경우 뒤에 1씩 번호를 증가시기면서 폴더명 확인(없으면 생성)

    if not os.path.exists(fdir + keyword):
        os.makedirs(fdir + keyword)     # 폴더가 없다면 폴더 생성후 뒤쪽에 "/"만 연결
        fdir = fdir + keyword +  "/"
    else:
        # 폴더가 있다면 새로운 폴더 생성(번호 증가)
        num = 0
        while True:
            num += 1 #번호 1씩 증가

            #증가된 번호와 기존 폴더명을 연경해서 존재여부 확인
            if not os.path.exists(fdir + keyword + str(num)):
                # 없으면 폴더 생성후 while 종료
                os.makedirs(fdir + keyword + str(num)) 
                fdir = fdir + keyword + str(num) + "/"
                break 
    return fdir


def downloadimg(fdir,keyword,tag_src):
    num = 1
    for tag in tqdm(tag_src):
        img_name = fdir + keyword + str(num) + ".jpg"
        request.urlretrieve(tag, img_name)
        time.sleep(1)
        num += 1