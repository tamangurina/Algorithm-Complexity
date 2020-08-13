import random
from search import linear_search, binary_search
from time import time, time_ns
import matplotlib.pyplot as plt
import numpy as np
import math

class SearchData:
    def __init__(self):
        self.min = 10000
        self.max = 1000000
        self.step = 10000
        self.max_ = 40000000
        self.plotdatas = []
    
    def clearData(self):
        self.plotdatas = []
    
    def displayData(self, title, color):
        if(len(self.plotdatas) <= 0):
            print("Data not found")
        plt.plot(*zip(*self.plotdatas),c=color)
        plt.title(title, fontsize = 18)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()
    
    def bestCaseLinearSearch(self):
        self.clearData()
        for i in range(self.min,self.max, self.step):
            data = random.sample(range(self.max), i)
            start = time()
            linear_search(data, data[0])
            end = time()
            elapsed = end - start           
            self.plotdatas.append((i, elapsed))
        self.displayData("Best case of Linear Search", 'blue')

    def worstCaseLinearSearch(self):
        self.clearData()
        for i in range(self.min,self.max, self.step):
            data = random.sample(range(self.max), i)
            start = time()
            linear_search(data, data[len(data) - 1])
            end = time()
            elapsed = end - start           
            self.plotdatas.append((i, elapsed))
        self.displayData("Worst case of Linear Search", 'blue')

    def bestCaseBinarySearch(self):
        self.clearData()
        #sumLinearTime = 0
        for i in range(self.min,self.max, self.step):
            data = random.sample(range(self.max), i)
            start = time()
            binary_search(data, data[(len(data) -1) // 2])
            end = time()
            elapsed = end - start        
            self.plotdatas.append((i, elapsed))
        self.displayData("Best case of Binary Search", 'blue')

    def worstCaseBinarySearch(self):
        self.clearData()  
        items = 1000000
        while items <=self.max_:
            data = random.sample(range(self.max_), items)
            data.sort()
            start = time()
            index = binary_search(data, data[len(data) -1])
            end = time()
            elapsed = end - start 
            print(f"Elapsed Time for {items} datas: {elapsed}")        
            self.plotdatas.append((items, elapsed))
            items = int(items * 1.5)
        self.displayData("Worst case of Binary Search", 'blue')   
    


if __name__ == "__main__":
    SearchData().bestCaseBinarySearch()
    #SearchData().worstCaseBinarySearch()

    #SearchData().worstCaseLinearSearch()
    #SearchData().bestCaseLinearSearch()