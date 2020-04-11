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

metallocenes = ['zirconocene','hafnocene','titanocene']
catalysts = ['Cp2ZrCl2','Cp2HfCl2','Cp2TiCl2','EtInd2ZrCl2','(nBuCp)2ZrCl2']
activators = ['methylaluminoxane','triethylaluminum','triisobutylaluminum','trimethylaluminum']
support = ['alumina','MgCl2(THF)2','Al2O3','silica',]
acronyms = ['MAO','TIBA','TEA','TMA','MWD']
monomers = ['1-hexene','propene','ethene','1-butene','1,7-octadiene']
polymers = ['polyethylene','polypropylene','poly(1-hexene)']
category = ['activator','monomer','polymer','metallocene','catalyst']
elements = ['Zr','Ti','Hf','Al','Pd','Pt']
other = ['homogeneous','heterogeneous','isotactic','syndiotactic','property','rheological','support']
vocab = metallocenes + catalysts + activators + support + acronyms + monomers + polymers + category + elements + other

labels = []
tokens = []
for word in model.wv.vocab:
    if word in vocab:
        tokens.append(model[word])
        labels.append(word)

tsne_model = TSNE(perplexity=5, n_components=2, init='pca', n_iter=10000, random_state=23)
new_values = tsne_model.fit_transform(tokens)

x = []
y = []
for value in new_values:
    x.append(value[0])
    y.append(value[1])

plt.figure(figsize=(16, 16))
for i in range(len(x)):
    plt.scatter(x[i],y[i])
    plt.annotate(labels[i],
                 xy=(x[i], y[i]),
                 xytext=(5, 2),
                 textcoords='offset points',
                 ha='right',
                 va='bottom')
plt.ylabel('Dimension 2')
plt.xlabel('Dimension 1')
plt.title('t-SNE')
plt.show()
