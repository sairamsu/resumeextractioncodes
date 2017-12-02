import re

def multiwordReplace(text, wordDic):
    rc = re.compile('|'.join(map(re.escape, wordDic)))
    def translate(match):
        return wordDic[match.group(0)]
    return rc.sub(translate, text)


str1 = open('Abhi.txt','r', encoding='latin-1')

#l = open('Abhi.txt','r', encoding='latin-1')

str1 = str1.read()

wordDic = { 'Experience Summary': 'Summary', 'Project Details':  'Summary'}

with open ('se.txt','w', encoding='latin-1') as infile:
    str2 = multiwordReplace(str1,wordDic)
    infile.write(str2)
