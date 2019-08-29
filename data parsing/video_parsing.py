
# coding: utf-8

# In[1]:


#https://kwonsye.github.io/study%20note/2019/03/24/download-youtube.html
#Excel 읽어들여 비디오 다운


# In[2]:


import os
import subprocess
import pytube
from moviepy.editor import * 
from openpyxl import load_workbook #엑셀 파일 읽어오기
import requests 
from bs4 import BeautifulSoup 


# In[ ]:


# 해당 경로에서 엑셀 파일 가져오기
load_wb = load_workbook("test_1.xlsx", data_only=True)
# 시트 이름으로 불러오기
load_ws = load_wb['Sheet1']

print('헤더를 제외한 엑셀의 모든 행과 열 저장')
all_values = []
for row in load_ws['A2':'B21']:
    row_value = []
    for cell in row:
        row_value.append(cell.value)
    all_values.append(row_value)

URL = 'https://www.youtube.com/results'

for row in range(len(all_values)):
    # HTTP request
    params = {'search_query': all_values[row][1] } # 엑셀파일의 'title'에 해당하는 문자열로 query
    response = requests.get(URL, params=params)
    
    # parsing
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    
    watch_url = soup.find_all(class_='yt-uix-sessionlink spf-link')[0]['href']
    
     # 유튜브 가져오기
    
    youtube = pytube.YouTube("https://www.youtube.com" + watch_url) # 동영상 url
    videos = youtube.streams.all()    

    for i in range(len(videos)) :
        print(i,":", videos[i])
        
    parent_dir = "C:\\Users\\HYUNJIN BAE\documents\\Python Scripts\\video\laliga" # 저장할 파일 경로
    videos[0].download(parent_dir) # mp4로 다운로드
    
    
    default_filename = videos[0].default_filename # 기존 mp4 파일이름


    print("완료!")

