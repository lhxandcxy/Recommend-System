import numpy as np
from Similarity import *


class ItemCF:
    def __init__(self):
        self.item_rate = {}
        self.item_similarity = {}
        self.item_list = []


  
    def readFile(self,filename):
        f = open(filename, "r")
        rows = []    
        rows = f.readlines()  
        f.close()  
        return rows  

    #得到item的评分矩阵 (item1, {(user1,ratig), (user2, rating)....}), (item2, {(user1,rating), (user3, rating)....})
    def getRateMatrix(self,lines):
        for line in lines:
            info = line.split("\t")
            user_id = int(info[0])
            item_id = int(info[1])
            rating = int(info[2])
            if item_id not in self.item_rate.keys():
                self.item_rate[item_id] = {}
            self.item_rate[item_id][user_id] = rating
            
        #得到item列表
        self.item_list = list(self.item_rate.keys())

    #两个item的相似度计算
    def getItemSim(self,item1, item2):
        common = {}
        #找出共同评分
        for user in item1.keys():
            if user in item2.keys():
                common[user] = 1
        if(len(common) == 0):
            return 0
        sim1 = [item1[user] for user in common]
        sim2 = [item2[user] for user in common]
        return pearsSim(sim1, sim2)



    #线下计算所有商品之间的相似度
    def getSimility(self):
        for i in range(0, len(self.item_list)):
            item1 = self.item_list[i]
            if item1 not in self.item_similarity.keys() :
                self.item_similarity[item1] = {}
            for j in range(i+1, len(self.item_list)):
                item2 = self.item_list[j]
                if item2 not in self.item_similarity.keys():
                    self.item_similarity[item2] = {}
                similarity = self.getItemSim(self.item_rate[item1], self.item_rate[item2])
                self.item_similarity[item1][item2] = similarity
                self.item_similarity[item2][item1] = similarity

    def buildItemCF(self,filename):
        self.getRateMatrix(self.readFile(filename))
        self.getSimility()
        print("finish")



    #给定item_id,推荐k个商品
    def recommend(self,item_id, k):
        d = item_similarity[item_id]
        sorted_list = sorted(d.items(), key=lambda d:d[1], reverse = True)
        recommend_list = []
        i = 0
        while i < k:
            recommend_list.append(sorted_list[i][0]);
            i += 1;
        return recommend_list;
                
        
        
        
        

        
            
        
