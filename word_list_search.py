# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:14:23 2022

@author: 楊登棋
"""
import re

people = ["Malfoy","Crabbe","Goyle","Ron","Hermione"]
magic_spell = ["ReparoV","Alohomora"]
print("------------------------------------1.人名------------------------------------")
print(people)
print("------------------------------------2.咒語------------------------------------")
print(magic_spell)
find_people=[]
find_spells=[]
find_whosay=[]
r=[]
with open(file='HP4Excerpt.txt',mode="r",encoding="utf-8") as f:
    #print(f.read().replace("\n"," ")) 
    a = f.readlines()
    new_line = []
    new_list = []
    for line in a:
        new_line = line.strip('\n')
        new_list.append(new_line)
    text_str = " ".join(new_list)
    #print("------------------------------------1.文本------------------------------------")
    #print(text_str)
    i=0    
    final=[]
    for spell in magic_spell: 
        find_spells.append(re.findall(pattern=spell,string=text_str))
    
        for person in people:      
            #find_people.append(re.findall(pattern=person,string=text_str))    
            find_whosay.append(re.findall(pattern=person+".*"+spell, string=text_str))
            if re.findall(pattern=person+".*"+spell, string=text_str):
                i+=1
        if i:
            final.append(i-1)
            i=0
    print("------------------------------------3.咒語在文本------------------------------------")
    print(find_spells)   
    print("--------------------------------4方法一.咒語:人_陣列應用--------------------------------")
    for F in range(len(final)):
        print(find_whosay[final[F]])    
    #print(find_people)
   
    print("--------------------------------4方法二.咒語:人_暴力搜尋--------------------------------")
    start_spell=[]
    start_person=[0]
    i=0
    text_list=text_str.split()
    for text in text_list:        
        for spell in magic_spell:         
            if text==spell:
                start_spell.append(text_list.index(text))
        for person in people:
            if text==person:
                start_person.append(text_list.index(text,start_person[i])) 
                i+=1
    ans=len(text_list)
    start=[0]
    end=[0]            
    for n in start_spell:
        for m in start_person:
            if n-m<ans and n>m:
                ans=n-m
                
                start[start_spell.index(n)]=m
                end[start_spell.index(n)]=n
        ans=len(text_list)  
    for j in range(len(start_spell)):
        print(" ".join(text_list[start[j]:end[j]+1]))        
    
              
            
    
    
    
    