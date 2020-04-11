from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

path = "mat2vec/training/models/"
model = "NP200SG"
#model = "FlowModelNew"
metallocenes = ['zirconocene','hafnocene','titanocene']
catalysts = ['Cp2ZrCl2','Cp2HfCl2','Cp2TiCl2','EtInd2ZrCl2','(nBuCp)2ZrCl2']
activators = ['methylaluminoxane','trimethylaluminum','triethylaluminum','triisobutylaluminum']
support = ['alumina','MgCl2(THF)2','Al2O3','silica',]
acronyms = ['MAO','TIBA','TMA','TEA']
monomers = ['1-hexene','propene','ethene']
polymers = ['polyethylene','polypropylene','poly(1-hexene)']
category = ['activator','monomer','polymer','metallocene']
elements = ['Zr','Ti','Hf']
allElements = ['Zr','Ti','Hf','C','Al','Pt','Pd','Rh','Ni','Fe']
#vocabulary = ['Zr','Ti','zirconocene','titanocene','Cp2ZrCl2','Cp2TiCl2']
#vocabulary = ['MAO','TIBA','TMA','TEA','methylaluminoxane','trimethylaluminum','triethylaluminum','triisobutylaluminum']
#vocabulary = ['polyethylene','polypropylene','poly(1-hexene)','1-hexene','propene','ethene']
#vocabulary = ['zirconocene','hafnocene','titanocene','Cp2ZrCl2','Cp2HfCl2','Cp2TiCl2','methylaluminoxane','trimethylaluminum','triethylaluminum','triisobutylaluminum','polyethylene','polypropylene','poly(1-hexene)','1-hexene','propene','ethene']

vocabulary = acronyms + activators
X = []
print(path+model+'\n')

w2v_model = Word2Vec.load(path+model)

for vocab in vocabulary:
    X.append(w2v_model.wv[vocab])

pca = PCA(n_components=2)
result = pca.fit_transform(X)
# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
words = vocabulary
for i, word in enumerate(words):
	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()
