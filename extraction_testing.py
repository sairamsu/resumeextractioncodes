#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

#extracting workexperience and summary titles
with open('Abhi.txt','r', encoding='latin-1')as file1:
    with open('Details.txt','r',encoding='latin-1' )as file2:
        same = set(file1).intersection(file2)
        
same.discard('\n')
words_list = []

for line in same:
    words_list.append(line)
    
words_list = list(map(str.strip,words_list))
print ('words_list', words_list)

#extracting other titles
with open('Abhi.txt','r', encoding='latin-1')as file3:
    with open('other_details.txt','r',encoding='latin-1' )as file4:
        same1 = set(file3).intersection(file4)
                
same1.discard('\n')
words_extract = []

for f in same1:
    words_extract.append(f)
    
words_extract = list(map(str.strip,words_extract))
print ('words_extract', words_extract)

#function to replace extracted titles        
def multiwordReplace(text, wordDic):
    rc = re.compile('|'.join(map(re.escape, wordDic)))
    def translate(match):
        return wordDic[match.group(0)]
    return rc.sub(translate, text)


str1 = open('Abhi.txt','r', encoding='latin-1')
str1 = str1.read()

wordDic1 = dict((k,'Summary') for k in words_list)
wordDic2 = dict((k,'xyz') for k in words_extract)
wordDic = dict(wordDic1, **wordDic2)
print(wordDic)

with open ('se.txt','w', encoding='latin-1') as infile:
    str2 = multiwordReplace(str1,wordDic)
    infile.write(str2)
    
#extracting summary paragraphs
with open("se.txt", encoding='latin-1')as infile,open("fgh.txt",'w', encoding='latin-1')as outfile:
    copy = False
    for word in words_extract:
        for line in infile:
            if line.strip() == "Summary":
                copy = True
       
            elif line.strip() == "xyz":
                copy = False
            if copy:
                outfile.write(line)
        


