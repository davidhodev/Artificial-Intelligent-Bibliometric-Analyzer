from gensim.models import Word2Vec
import os
path = "mat2vec/training/TestingModels"

print(path)
print('\n')
Models = os.listdir(str(path)+'/Models')
print(Models)
print('\n\n\n')
results = []
maxScore = 0
count = 0
for model in Models:
    w2v_model = Word2Vec.load(path+'/Models/'+model)
    score = 0
    count += 1
    with open(path+'/newAnalogies.txt', 'r') as f:
        for line in f:
            listOfEntries = line.split()
            #Index 0: Neg1      Index 1: Pos1      Index 2: Pos 2       Index 3: Neg 2
            try:
                if w2v_model.wv.most_similar(positive=[listOfEntries[1], listOfEntries[2]], negative=[listOfEntries[0]], topn=1)[0][0] == listOfEntries[3]:
                    score += 1
                    #print(listOfEntries)
            except:
                pass
    if maxScore < score:
        maxScore = score
    pct = score/count
    results.append([model, score, pct])
for result in results:
    result.append(result[1]/maxScore)
    print(result[0])
    print(result[1:4])
    print('\n')


        #except Exception:
        #    print('\n\nNot found!\n\n')
        #    pass
