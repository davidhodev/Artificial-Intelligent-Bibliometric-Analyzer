import pandas as pd
pd.options.mode.chained_assignment = None
import numpy as np
import re
import nltk

from gensim.models import Word2Vec

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

path = "mat2vec/training/models/"
model = "NP200SG"

model = Word2Vec.load(path+model)
'''
metallocenes = ['zirconocene','hafnocene','titanocene']
catalysts = ['Cp2ZrCl2','Cp2HfCl2','Cp2TiCl2','EtInd2ZrCl2','(nBuCp)2ZrCl2']
activators = ['methylaluminoxane','triethylaluminum','triisobutylaluminum','Et3Al','AlEtCl2','AlEt2Cl','tris(pentafluorophenyl)borane','diisobutylaluminum','[CPh3][B(C6F5)4]']
support = ['alumina','MgCl2(THF)2','Al2O3','silica',]
acronyms = ['MAO','TIBA','TEA','TMA','MMAO']
monomers = ['1-hexene','propene','ethene','1-butene','1,7-octadiene','1-octene']
polymers = ['polyethylene','polypropylene','poly(1-hexene)']
category = ['activator','monomer','polymer','metallocene','catalyst','cocatalyst']
elements = ['Zr','Ti','Hf']
other = ['homogeneous','heterogeneous','isotactic','syndiotactic','atactic','property','rheological','isoselective','MWD','polydispersity']
vocab = metallocenes + catalysts + activators + support + monomers + polymers + elements + other
'''
labels = []
tokens = []
'''
substring_list = ['ethyl','butyl','propyl','Zr','Hf','Ti','Al','poly']
for word in model.wv.vocab:
    if any(substring in word for substring in substring_list):
    #if word in vocab
        tokens.append(model[word])
        labels.append(word)
'''
chemicals = ['Zr','Ti','Hf','Al','Me','Cl','aluminum','zircon','titan','hafn','poly','ene','Cp','F','B','C','Pt','Pd','butyl','propyl','methyl','ethyl','Bu','Et','iso']
for word in model.wv.vocab:
    tokens.append(model[word])
    labels.append(word)
catindex = []
for words in labels:
    if any(part in words for part in ['Zr','Hf','Ti']):
        i = labels.index(words)
        catindex.append(i)
actindex = []
for words in labels:
    if any(part in words for part in ['alumin','Al','B']):
        i = labels.index(words)
        actindex.append(i)
monindex = []
for words in labels:
    if any(part in words for part in ['ethyl','propyl','1-']):
        i = labels.index(words)
        monindex.append(i)
perp = 60
iter = 5000
tsne_model = TSNE(perplexity=perp, n_components=2, init='pca', n_iter=iter, random_state=23)
new_values = tsne_model.fit_transform(tokens)

x = []
y = []
for value in new_values:
    x.append(value[0])
    y.append(value[1])

plt.figure(figsize=(32, 32))
for i in range(len(x)):
    if i in catindex:
        plt.scatter(x[i],y[i],c='tab:green')
    else:
        if i in actindex:
            plt.scatter(x[i],y[i],c='tab:blue')
        else:
            if i in monindex:
                plt.scatter(x[i],y[i],c='tab:orange')
            else:
                plt.scatter(x[i],y[i],c='tab:red', s = 10)

'''
    plt.annotate(labels[i],
                 xy=(x[i], y[i]),
                 ha='right',
                 va='bottom',fontsize=14)
'''
plt.ylabel('Dimension 2',fontsize=16)
plt.xlabel('Dimension 1',fontsize=16)
plt.title('t-SNE, perplexity = 5, inter = 10,000',fontsize=16)
plt.show()
