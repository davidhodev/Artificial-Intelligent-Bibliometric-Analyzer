from gensim.models import Word2Vec
path = "mat2vec/training/models/"

#model = input("\nEnter model name\n"
model = "NP200SG"
print(path+model+'\n')

model = Word2Vec.load(path+model)

substring_list = ['Zr','Hf','Ti']
count = 0
catalysts = []
for word in model.wv.vocab:
    if len(word) > 5:
        if any(substring in word for substring in substring_list):
            count += 1
            catalysts.append(word)

print(count)
print(catalysts)

with open('catalysts.txt', 'w') as f:
				data[i]['records'][k]['abstract']
			doiAbstractDictionary[data[i]['records'][k]['doi']] = data[i]['records'][k]['abstract']
