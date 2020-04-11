from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import matplotlib
from matplotlib import pyplot as plt
matplotlib.font_manager._rebuild()

csfont = {'fontname':'Times New Roman'}
plt.rcParams["font.family"] = "Times New Roman"


path = "mat2vec/training/models/"
model = "NP200SG"
#model = "FlowModelNew"
metallocenes = ['zirconocene','hafnocene','titanocene']
catalysts = ['Cp2ZrCl2','Cp2HfCl2','Cp2TiCl2','EtInd2ZrCl2','(nBuCp)2ZrCl2','Me2Si(Ind)2ZrCl2','CpTi(OMe)3']
activators = ['methylaluminoxane','triethylaluminum','triisobutylaluminum','trimethylaluminum','tris(pentafluorophenyl)borane']
support = ['alumina','MgCl2(THF)2','Al2O3','silica',]
acronyms = ['MAO','TIBA','TMA','TEA']
monomers = ['1-hexene','propene','ethene','1-butene','1,7-octadiene','1-octene','1-decene','1-dodecene']
polymers = ['polyethylene','polypropylene','poly(1-hexene)']
category = ['activator','monomer','catalyst']
elements = ['Zr','Ti','Hf']
allElements = ['Zr','Ti','Hf','Al','Pt','Pd','Rh','Ni','Fe']
#vocabulary = ['Zr','Ti','zirconocene','ßtitanocene','Cp2ZrCl2','Cp2TiCl2']
#vocabulary = ['MAO','TIBA','TMA','TEA','methylaluminoxane','trimethylaluminum','triethylaluminum','triisobutylaluminum']
#vocabulary = ['polyethylene','polypropylene','poly(1-hexene)','1-hexene','propene','ethene']
#vocabulary = ['zirconocene','hafnocene','titanocene','Cp2ZrCl2','Cp2HfCl2','Cp2TiCl2','methylaluminoxane','trimethylaluminum','triethylaluminum','triisobutylaluminum','polyethylene','polypropylene','poly(1-hexene)','1-hexene','propene','ethene']

vocabulary = monomers
vocabulary2 = catalysts
vocabulary3 = activators
X = []
Y = []
Z = []
print(path+model+'\n')

w2v_model = Word2Vec.load(path+model)

for vocab in vocabulary:
    X.append(w2v_model.wv[vocab])
len1 = len(vocabulary)
for vocab in vocabulary2:
    Y.append(w2v_model.wv[vocab])
len2 = len(vocabulary2)
for vocab in vocabulary3:
    Z.append(w2v_model.wv[vocab])
len3 = len(vocabulary3)

pca = PCA(n_components=2)
result = pca.fit_transform(X+Y+Z)
print(result)
# create a scatter plot of the projection
fig, plot = plt.subplots(figsize=(10,8),dpi=205)
plot.scatter(result[0:len1, 0], result[0:len1, 1], c = 'tab:green')
plot.scatter(result[len1:len1+len2, 0], result[len1:len1+len2, 1], c = 'tab:red')
plot.scatter(result[len1+len2:len1+len2+len3, 0], result[len1+len2:len1+len2+len3, 1], c = 'tab:blue')
words = vocabulary + vocabulary2 + vocabulary3
for i, word in enumerate(words):
    if word == 'trimethylaluminum':
        plot.annotate(word, xy=(result[i, 0]-.2, result[i, 1]-.2))
    else:
        if word == 'CpTi(OMe)3':
            plot.annotate(word, xy=(result[i, 0]-.2, result[i, 1]-.2))
        else:
            if word == '1-octene':
                plot.annotate(word, xy=(result[i, 0]-.2, result[i, 1]-.2))
            else:
                plot.annotate(word, xy=(result[i, 0]-.2, result[i, 1]+.06))

plot.legend()
plt.ylabel('Dimension 2',**csfont,fontsize=14)
plt.xlabel('Dimension 1',**csfont,fontsize=14)
plt.title('Reagent Categories PCA',**csfont,fontsize=14)

plt.show()
