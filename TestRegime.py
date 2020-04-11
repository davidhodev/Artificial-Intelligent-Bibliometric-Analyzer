from gensim.models import Word2Vec
import os
import numpy as np
import pandas as pd
path = "mat2vec/training/TestingModels"

print(path)
Models = os.listdir(str(path)+'/Models')
print(Models)
print('\n\n')
results = []
maxScore = 0
for model in Models:
    w2v_model = Word2Vec.load(path+'/Models/'+model)
    score = 0
    count = 0
    with open(path+'/newAnalogies.txt', 'r') as f:
        for line in f:
            count += 1
            listOfEntries = line.split()
            #Index 0: Neg1      Index 1: Pos1      Index 2: Pos 2       Index 3: Neg 2
            try:
                if w2v_model.wv.most_similar(positive=[listOfEntries[1], listOfEntries[2]], negative=[listOfEntries[0]], topn=1)[0][0] == listOfEntries[3]:
                    score += 1
            except:
                pass
    if maxScore < score:
        maxScore = score
    pct = round(score/count,2)
    results.append([model, score, pct])

for result in results:
    result.append(round(result[1]/maxScore,2))

results = np.array(results)
df = pd.DataFrame(results, columns = ['Name','Score','PCT','Rel PCT'])

print(df.sort_values(by=['Name']))
