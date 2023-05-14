#!/usr/bin/env python
# coding: utf-8

# In[100]:


import csv
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    #2008, 2012, 2016 데이터
    f1 = open('q3_1.csv')
    
    data1 = csv.reader(f1, delimiter = ',')
    h1 = next(data1)
    for row in data1:
        r1 = row
        
    f1.close()
    
    #2020 데이터
    f2 = open('q3_2.csv')
    
    data2 = csv.reader(f2, delimiter = ',')
    h2 = next(data2)
    h1.extend(h2[1:])
    r2 = next(data2)
    r1.extend(r2[1:])
    
    f2.close()
    
    #2008, 2012, 2016, 2020 데이터 생성
    f = open('q3.csv', 'w', newline = '')
    
    write = csv.writer(f)
    write.writerow(h1)
    write.writerow(r1)
    
    f.close()
    
    #생성한 데이터 불러옴
    f = open('q3.csv')
    data = csv.reader(f, delimiter = ',')
    header = next(data)
    header = header[1:]
    peop = row[1:]
    
    for i in range(len(peop)):
        peop[i] = int(peop[i])
    
    print("**제주특별자치도 2008, 2012, 2016, 2020 남녀 인구수 추이**")
    for i in range(len(header)):
        print(header[i]+':', int(peop[i]))
    
    f.close()
    
    #### 시각화 ####
    
    plt.rc('font', family = 'Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(12,10))
    bar_width = 0.8
    x = 0
    
    #막대그래프
    for i in range(len(header)):
        if i%3 == 0:
            x += 1
        if '남자' in header[i]:
            plt.subplot(2, 2, x)
            plt.bar(header[i], peop[i], bar_width, color = 'cornflowerblue', label = 'male')
        if '여자' in header[i]:
            plt.subplot(2, 2, x)
            plt.bar(header[i], peop[i], bar_width, color = 'salmon', label = 'female')
        plt.legend()
        plt.title('제주특별자치도 남녀 인구수(막대그래프)')
        plt.ylim([0, 350000])
        plt.xlabel('year & sex')
        plt.ylabel('count')
            
    plt.show()
    
    #파이차트
    plt.figure(figsize=(14,10))
    bar_width = 0.8
    color = ['cornflowerblue', 'salmon']
    x = 0
    
    for i in range(len(header)):
        if i%3 == 0:
            x += 1
            plt.subplot(2, 2, x)
            plt.pie(peop[i+1:i+3], labels = header[i+1:i+3], autopct='%.1f%%', startangle=90, colors = color)
            plt.title('제주특별자치도 인구 남녀 비율(파이차트)', fontsize=15)
            plt.legend(loc=(0.2, 0), fontsize=12)
            
    plt.show() 

