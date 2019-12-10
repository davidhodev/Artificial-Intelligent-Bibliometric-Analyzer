
from gensim.models import Word2Vec
path = "mat2vec/training/models/"
model = "processedCorpusSG100"
#model = "FlowModelNew"
print(path+model+'\n')
w2v_model = Word2Vec.load(path+model)

w2v_model.wv.save_word2vec_format(path+'CompleteProjectorModel')
