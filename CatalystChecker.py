from gensim.models import Word2Vec
import os
path = "mat2vec/training/models/"
#print(os.listdir(path))
#model = input("\nEnter model name\n")
model = "NP200SG"
print(path+model+'\n')
w2v_model = Word2Vec.load(path+model)


substring_list = ['Zr','Hf','Ti']
count = 0
catalysts = []
for word in w2v_model.wv.vocab:
    if len(word) > 5:
        if any(substring in word for substring in substring_list):
            count += 1
            catalysts.append(word)

activators = ['methylaluminoxane','triethylaluminum','triisobutylaluminum','trimethylaluminum','dimethylanilium','triphenylcarbenium','MAO','TIBA','TEA','TMA']

checkcount = 1000 # top number of simialirty results
Combined = []
for catalyst in catalysts:
    listofwords = w2v_model.wv.most_similar(catalyst,topn=checkcount)
    listofwords2 = w2v_model.predict_output_word(catalyst,topn=checkcount)
    activatorlist = []
    activatorlist2 = []
    for i in range(checkcount):
        if listofwords[i][0] in activators:
            activatorlist.append(listofwords[i][0])
        if listofwords2[i][0] in activators:
            activatorlist2.append(listofwords2[i][0])
    Combined.append([catalyst,activatorlist,activatorlist2])

for i in range(len(catalysts)):
    print('\n')
    print(Combined[i][0]+' co-catalysts most similar:\n')
    print(Combined[i][1])
    print('\nco-catalysts most likely to appear next to:')
    print(Combined[i][2])
