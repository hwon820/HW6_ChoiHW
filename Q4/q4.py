#!/usr/bin/env python
# coding: utf-8

# In[8]:


import csv
import matplotlib.pyplot as plt

if __name__ == '__main__':

    f = open('q4.csv', 'r', encoding = 'utf-8-sig')
    data = csv.reader(f, delimiter = ',')
    
    num = []
    multi = []
    
    #[역이름, 승차수, 하차수] 형태로 저장
    for row in data:
        if row[0] not in multi:
            num.append([row[0], int(row[1]) + int(row[3]), int(row[2]) + int(row[4])])
            multi.append(row[0])
        #중복역 승객수 합산
        else: 
            for m in num:
                if m[0] == row[0]:
                    m[1] += int(row[1]) + int(row[3])
                    m[2] += int(row[2]) + int(row[4])
                    
    f.close()
                    
    #승차수 기준 정렬 후 top30 추출
    num.sort(key = lambda x: x[1])        
    ride30 = num[-30:]
    #ride30.sort(key = lambda x: (x[1] + x[2]))
    #하차수 기준 정렬 후 top30 추출
    num.sort(key = lambda x: x[2])  
    off30 = num[-30:]
    #off30.sort(key = lambda x: (x[1] + x[2]))
    #승하차수 기준 정렬 후 top30 추출
    num.sort(key = lambda x: (x[1] + x[2]))  
    total30 = num[-30:]
    
    plt.rc('font', family = 'Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False
    
    cmap = ['azure', 'lightcyan', 'paleturquoise', 'powderblue', 'lightblue','lightskyblue', 'skyblue', 'cadetblue', 'darkcyan', 'darkslategray',
            'thistle', 'plum', 'violet', 'orchid', 'mediumorchid','blueviolet', 'darkorchid', 'darkviolet', 'purple', 'indigo',
           'mistyrose', 'salmon', 'lightcoral', 'indianred','rosybrown','firebrick', 'brown', 'maroon', 'darkred', 'red']
    
    #최대 승차 30개역의 승객수
    plt.figure(figsize=(32,18))
    plt.xlabel('역 이름', fontsize = 30)
    plt.ylabel('승객 수', fontsize = 30)
    plt.yticks(fontsize=30)
    
    for i in range(len(ride30)):
        plt.title("최대 승차 30개역의 승객수", fontsize = 38)
        plt.bar(ride30[i][0], ride30[i][1], label = ride30[i][0], color = cmap[i])
        plt.gca().axes.xaxis.set_visible(False)
        plt.legend(fontsize = 27, ncol = 3)
        
    plt.show()
    
    #최대 하차 30개역의 승객수
    plt.figure(figsize=(32,18))
    plt.xlabel('역 이름', fontsize = 30)
    plt.ylabel('승객 수', fontsize = 30)
    plt.yticks(fontsize=30)
    
    for i in range(len(off30)):
        plt.title("최대 하차 30개역의 승객수", fontsize = 38)
        plt.bar(off30[i][0], off30[i][2], label = off30[i][0], color = cmap[i])
        plt.gca().axes.xaxis.set_visible(False)
        plt.legend(fontsize = 27, ncol = 3)
        
    plt.show()
    
    #최대 승하차 30개역의 승객수
    plt.figure(figsize=(32,18))
    plt.xlabel('역 이름', fontsize = 30)
    plt.ylabel('승객 수', fontsize = 30)
    plt.yticks(fontsize=30)
    
    for i in range(len(ride30)):
        plt.title("최대 승하차 30개역의 승객수", fontsize = 38)
        plt.bar(total30[i][0], total30[i][1]+total30[i][2], label = total30[i][0], color = cmap[i])
        plt.gca().axes.xaxis.set_visible(False)
        plt.legend(fontsize = 25, ncol = 3)
        
    plt.show()
    
    plt.figure(figsize=(15,13))
    plt.xlabel('역 이름', fontsize = 10)
    plt.ylabel('승객 수', fontsize = 10)
    plt.yticks(fontsize=10)
    
    for i in range(len(ride30)):
        if total30[i][0] == '여의도' or total30[i][0] == '서울역' or total30[i][0] == '구로디지털단지':
            plt.subplot(3, 1, 1)
            plt.title("승차 승객수", fontsize = 15)
            plt.bar(total30[i][0], total30[i][1], label = total30[i][0])
            plt.gca().axes.xaxis.set_visible(False)
            plt.legend(fontsize = 15, ncol = 3)
            plt.subplot(3, 1, 2)
            plt.title("하차 승객수", fontsize = 15)
            plt.bar(total30[i][0], total30[i][2], label = total30[i][0])
            plt.gca().axes.xaxis.set_visible(False)
            plt.legend(fontsize = 15, ncol = 3)
            plt.subplot(3, 1, 3)
            plt.title("승하차 승객수", fontsize = 15)
            plt.bar(total30[i][0], total30[i][1]+total30[i][2], label = total30[i][0])
            plt.gca().axes.xaxis.set_visible(False)
            plt.legend(fontsize = 15, ncol = 3)
        
    plt.show()

