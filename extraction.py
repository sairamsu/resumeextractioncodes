import re

#extracting titles
with open('Abhi.txt','r', encoding='latin-1')as file1:
    with open('Details.txt','r',encoding='latin-1' )as file2:
        same = set(file1).intersection(file2)
        

same.discard('\n')
words_list = []

for line in same:
    words_list.append(line)
    
words_list = list(map(str.strip,words_list))
print ('words_list', words_list)

        
#replacing titles
def multiwordReplace(text, wordDic):
    rc = re.compile('|'.join(map(re.escape, key_value)))
    def translate(match):
        return wordDic[match.group(0)]
    return rc.sub(translate, text)


str1 = open('Abhi.txt','r', encoding='latin-1')

str1 = str1.read()

key_value = dict((k,'Summary') for k in words_list)
print(key_value)

with open ('se5.txt','w', encoding='latin-1') as infile:
    str2 = multiwordReplace(str1,key_value)
    infile.write(str2)
    #print(str2)
    
with open("se5.txt", encoding='latin-1')as infile,open("fgh5.txt",'w', encoding='latin-1')as outfile:
    copy = False
    for line in infile:
        if line.strip() == "Summary":
            copy = True
        elif line.strip() == "Technical Skills":
            copy = False
        elif copy:
            outfile.write(line)
        fh = open("fgh5.txt",'r')
        contents = fh.read()
        len(contents)

'''with open('se3.txt','r', encoding='latin-1')as file1:
    with open('other_details.txt','r',encoding='latin-1' )as file2:
        same1 = set(file1).intersection(file2)
                
same.discard('\n')
words_extract = []

for line in same1:
    
    words_extract.append(line)
    
words_extract = list(map(str.strip,words_extract))
print ('words_extract', words_extract)'''


#extracting paragraphs    

        
        

