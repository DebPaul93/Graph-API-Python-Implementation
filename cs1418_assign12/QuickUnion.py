#!/usr/bin/python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------
'''Name: DEBJYOTI PAUL
Roll Number:CS1418
Date of Submission:7/12/2014
Deadline date:  7/12/2014
Program description:QUICKUNION MODULE
Acknowledgements:'''
#--------------------------------------------------------------------
#this quick union function is written on the basis of
#the quick union algorithm in Princeton Lecture
#https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf
class QuickUnion:

    def __init__(self, N=0):
        id = []
        count = 0
        while count < N:
            id.append(count)
            count = count + 1
        self.id = id
        self.N = N

    def root(self, i):
        while i != self.id[i]:
            j = self.id[i]
            k = self.id[j]
            self.id[i] = k
            i = self.id[i]
        return i

    def find(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        self.id[self.root(p)] = self.root(q)



