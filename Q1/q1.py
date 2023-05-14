#!/usr/bin/env python
# coding: utf-8

# In[27]:


import csv
import matplotlib.pyplot as plt

#월평균 데이터 추출

#전국 월평균

if __name__ == "__main__":
    
    f = open('q1_all.csv')
    data_all = csv.reader(f, delimiter = ',')
    next(data_all)
    all_av = []
    for row in data_all:
        all_av.append(float(row[2]))
    
    f.close()
    
    #전국 월평균
    f = open('q1_all.csv')
    data_all = csv.reader(f, delimiter = ',')
    next(data_all)
    all_av = []
    for row in data_all:
        all_av.append(float(row[2]))
    
    f.close()
    
    #서울 월평균
    f = open('q1_seoul.csv')
    data_seoul = csv.reader(f, delimiter = ',')
    next(data_seoul)
    seoul_av = []
    for row in data_seoul:
        seoul_av.append(float(row[2]))
    
    f.close()
    
    #대전 월평균
    f = open('q1_daej.csv')
    data_daej = csv.reader(f, delimiter = ',')
    next(data_daej)
    daej_av = []
    for row in data_daej:
        daej_av.append(float(row[2]))
    
    f.close()
    
    #부산 월평균
    f = open('q1_busan.csv')
    data_busan = csv.reader(f, delimiter = ',')
    next(data_busan)
    busan_av = []
    for row in data_busan:
        busan_av.append(float(row[2]))
    
    f.close()
    
    #제주 월평균
    f = open('q1_jeju.csv')
    data_jeju = csv.reader(f, delimiter = ',')
    next(data_jeju)
    jeju_av = []
    for row in data_jeju:
        jeju_av.append(float(row[2]))
    
    f.close()
    
    #시각화
    plt.figure(figsize=(10, 10))
    plt.title('The Average Monthly Temperature of 2022')
    plt.xlabel('Month')
    plt.ylabel('Temperatrue(℃)')
    plt.xlim([0, 11])
    plt.ylim([-5, 30])
    
    month = ['Jen', 'Feb', 'May', 'Apr', 'Mar', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    plt.plot(month, all_av, label = 'All')
    plt.plot(month, seoul_av, label = 'Seoul')
    plt.plot(month, daej_av, label = 'Daejun')
    plt.plot(month, busan_av, label = 'Busan')
    plt.plot(month, jeju_av, label = 'Jeju')
    plt.legend()
    plt.show()
    
    #지역평균 - 전국평균 기온 차이
    def temp_diff(av_list):
        
        diff = []
        high_count, low_count = 0, 0
        
        for i in range(len(av_list)):
            
            print('{0:d}월 기온차: {1:0.1f}℃'.format(i+1, av_list[i] - all_av[i]))
            
            diff.append(av_list[i] - all_av[i])
            
            if av_list[i] - all_av[i] > 0:
                high_count += 1
            else:
                low_count += 1
                
        print("전국 대비 기온 높은 달: {0:d}개".format(high_count))
        print("전국 대비 기온 낮은 달: {0:d}개".format(low_count))
        return diff  
                
    
    print("---서울 기온 차이---")
    seo = temp_diff(seoul_av)
    print("")
    
    print("---대전 기온 차이---")
    dae = temp_diff(daej_av)
    print("")
    
    print("---부산 기온 차이---")
    bus = temp_diff(busan_av)
    print("")
    
    print("---제주 기온 차이---")
    jej = temp_diff(jeju_av)
    
    plt.rc('font', family = 'Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize = (10,10))
    bar_width = 0.8
    
    plt.subplot(2, 2, 1)
    plt.title('전국평균대비 서울 월별 기온차',fontsize = 12)
    plt.xlim([-10,10])
    plt.xlabel('기온차')
    plt.ylabel('월')
    plt.barh(month,seo, bar_width,color ='darkgreen',edgecolor = 'whitesmoke')
    
    plt.subplot(2, 2, 2)
    plt.title('전국평균대비 대전 월별 기온차',fontsize = 12)
    plt.xlim([-8,8])
    plt.xlabel('기온차')
    plt.ylabel('월')
    plt.barh(month,dae, bar_width,color ='darkgreen',edgecolor = 'whitesmoke')
    
    plt.subplot(2, 2, 3)
    plt.title('전국평균대비 부산 월별 기온차',fontsize = 12)
    plt.xlim([-10,10])
    plt.xlabel('기온차')
    plt.ylabel('월')
    plt.barh(month,bus, bar_width,color ='darkgreen',edgecolor = 'whitesmoke')
    
    plt.subplot(2, 2, 4)
    plt.title('전국평균대비 제주 기온차',fontsize = 12)
    plt.xlim([-10,10])
    plt.xlabel('기온차')
    plt.ylabel('월')
    plt.barh(month,jej, bar_width,color ='darkgreen',edgecolor = 'whitesmoke')

