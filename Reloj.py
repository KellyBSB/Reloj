# -*- coding: utf-8 -*-
"""
Created on Thu May 10 08:46:51 2018

@author:Cortez,Narváez,Soto
"""
import time
hour=0
mint=0
def bucle(hour,mint):
        for i in range(1, 62):
            if(i<61):
                print(str(hour)+":"+str(mint)+":"+str(i))
                time.sleep(1)
            elif(i==61):
                mint=mint+1
                if(mint==61):
                    mint=0
                    hour=hour+1
                    if(hour==25):
                        hour=0
                        bucle(hour,mint)
                bucle(hour,mint)
            
bucle(hour,mint)