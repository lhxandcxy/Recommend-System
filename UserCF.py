import numpy as np
from Similarity import *


class UserCF:
    def __init__(self):
        self.user_rate = {}
        self.user_similarity = {}
        self.user_list = []

    def readFile(self,filename):
        f = open(filename, "r")
        rows = []    
        rows = f.readlines()  
        f.close()  
        return rows

    #得到user的评分矩阵 (user, {(item1,ratig), (item2, rating)....}), (user2, {(item1,rating), (item3, rating)....})
    def getRateMatrix(self,lines):
        for line in lines:
            info = line.split("\t")
            user_id = int(info[0])
            item_id = int(info[1])
            rating = int(info[2])
            if user_id not in self.user_rate.keys():
                self.user_rate[user_id] = {}
            self.user_rate[user_id][item_id] = rating
            
        #得到user列表
        self.user_list = list(self.user_rate.keys())



    #两个user的相似度计算
    def getUserSim(self, user1, user2):
        common = {}
        #找出共同评分
        for item in user1.keys():
            if item in user2.keys():
                common[item] = 1
        if(len(common) == 0):
            return 0
        sim1 = [user1[item] for item in common]
        sim2 = [user2[item] for item in common]
        return pearsSim(sim1, sim2)


    #实时计算用户之间的相似度，得出最相似的k个用户
    def getSimilarity(self, user_id, k):
        return 0;
        

    #计算所有用户之间的相似度
    def getSimility(self):
        for i in range(0, len(self.user_list)):
            user1 = self.user_list[i]
            if user1 not in self.user_similarity.keys() :
                self.user_similarity[user1] = {}
            for j in range(i+1, len(self.user_list)):
                user2 = self.user_list[j]
                if user2 not in self.user_similarity.keys():
                    self.user_similarity[user2] = {}
                similarity = self.getUserSim(self.user_rate[user1], self.user_rate[user2])
                self.user_similarity[user1][user2] = similarity
                self.user_similarity[user2][user1] = similarity

    def buildUserCF(self,filename):
        self.getRateMatrix(self.readFile(filename))
        self.getSimility()
        print("finish")



    #给定item_id,推荐k个商品
    def recommend(self,user_id, k):
        d = user_similarity[user_id]
        sorted_list = sorted(d.items(), key=lambda d:d[1], reverse = True)
        recommend_list = []
        i = 0
        while i < k:
            recommend_list.append(sorted_list[i][0]);
            i += 1;
        return recommend_list;
                
