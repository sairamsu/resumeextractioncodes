keywords = ['experience','years','months']
with open('Abhi.txt', 'r', encoding='latin-1') as in_file:
    text = in_file.read()
    sentences = text.split(".")
    
for sentence in sentences :
    if (any(map(lambda word: word in sentence, keywords))):
        print (sentence)