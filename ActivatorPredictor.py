from gensim.models import Word2Vec
import os
import numpy as np
import pandas as pd
path = "mat2vec/training/models/"
#print(os.listdir(path))
#model = input("\nEnter model name\n")
model = "NP200SG"
print(path+model+'\n')
w2v_model = Word2Vec.load(path+model)

catalyst_names = ['Cp*Ti(OBz)3','Cp2ZrCl2','Cp2ZrCl','Cp2HfCl2','Cp2TiCl2','EtInd2ZrCl2','(nBuCp)2ZrCl2','Et[Ind]2ZrCl2','Et(Ind)2ZrCl2','(n-BuCp)2ZrCl2','(SBI)ZrMe2',
'Cp2TiMe2','Cp2ZrMe2','Cp2HfMe2','Me2SiInd2ZrCl2','CpZrCl3','CpTiCl3','CpHfCl3','Cl4Ti','Cp*ZrMe3']
activator_names = ['MAO','TIBA','TEA','TIBAO','MMAO','methylaluminoxane','triethylaluminum','triisobutylaluminum','Et3Al','AlEtCl2','AlEt2Cl','tris(pentafluorophenyl)borane',
'[CPh3][B(C6F5)4]','CPh3B(C6F5)4','ethylaluminoxane','tetrachloroaluminate','tri-isobutylaluminum','methyl-aluminoxane','tetrakis(pentafluorophenyl)borane']
count = 0
array = []
for catalyst in catalyst_names:
    try:
        result = w2v_model.wv.most_similar(positive=['MAO', catalyst], negative=['Cp2ZrCl2'], topn=100)
        results = []
        for i in range(len(result)):
            results.append(result[i][0])
        for j in range(len(results)):
            if results[j] in activator_names:
                array.append([catalyst,results[j]])
    except Exception:
        print(catalyst)
        print('Not found!\n')
        pass

ARRAY = pd.DataFrame(array, columns = ['Catalyst','Activator'])
print(ARRAY)
ARRAY.to_csv()
with open('Predictions.csv', 'w') as f:
    f.write(ARRAY.to_csv())
    f.close()
