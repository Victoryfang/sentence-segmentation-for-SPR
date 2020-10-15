import nltk

lst=list(open('yes.txt')) # This is to read in txt file

for i in range(len(lst)):
    lst[i]=lst[i].replace('\n','') # This is to remove \n

s=[nltk.word_tokenize(s) for s in lst] # list comprehension

y=[s.split() for s in lst]  #list comprehension

for s in y:
    print(s, len(s)) # This is to make a list of each sentence
