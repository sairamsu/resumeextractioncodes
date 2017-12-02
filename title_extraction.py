with open('Abhi.txt','r', encoding='latin-1')as file1:
    with open('Details.txt','r',encoding='latin-1' )as file2:
        same = set(file1).intersection(file2)
        

same.discard('\n')

with open('final.txt','w', encoding='latin-1')as file_out:
    for line in same:
        file_out.write(line)