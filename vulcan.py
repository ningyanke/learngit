#!/usr/bin/env python
# coding=utf-8

class vulan(object):
    def __init__(self,name):
        self.name = name 
    def p_n(self):
        return  self.name

if __name__ == "__main__":
    xianzai = vulan("ningyanke")
    print xianzai.p_n() 

