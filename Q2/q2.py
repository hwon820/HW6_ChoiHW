#!/usr/bin/env python
# coding: utf-8

# In[18]:


import csv
import random
import matplotlib.pyplot as plt

if __name__ == '__main__':

    #주사위 시뮬레이션 함수
    def random_tool(n):
        rand = []
        for _ in range(n):
            num = random.randrange(1, 7)
            rand.append(num)
            
        return rand
    
    do100 = random_tool(100)
    do1000 = random_tool(1000)
    do10000 = random_tool(10000)
    do100000 = random_tool(100000)
    
    #결과 csv데이터 생성
    f = open('q2.csv', 'w', newline = '')
    
    write =  csv.writer(f)
    write.writerow(do100)
    write.writerow(do1000)
    write.writerow(do10000)
    write.writerow(do100000)
    
    f.close()
    
    #생성한 데이터 기반 그래프
    x, r = 0, -1
    nums = [1, 2, 3, 4, 5, 6]
    
    f = open('q2.csv')
    data = csv.reader(f, delimiter = ',')
    
    for row in data:  
        r += 1
        x += 1
        time = 10 * (10**x)
        
        row = list(row)
        row.sort()
        
        plt.ylim(0, time/3.5)
        plt.title('Results of {0:d} dice simulation runs'.format(time))
        plt.xlabel('number')
        plt.ylabel('count')
        plt.hist(row, bins = 6, edgecolor = 'whitesmoke', linewidth = 1.4, color='darkgreen')
        
        plt.show()
    
    f.close()

