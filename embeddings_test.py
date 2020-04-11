from gensim.models import Word2Vec
path = "mat2vec/training/models/"

model = input("\nEnter model name\n")
#model = "NP200SG"
print(path+model+'\n')
w2v_model = Word2Vec.load(path+model)

choice = input('Enter 1 to run similarity check, enter 2 to run a comparison\n')

while choice == '1':
    try:
        word = input('\nChoose a word to check similarity\n')
        print(w2v_model.wv.most_similar(word,topn=20))
    except Exception:
        print('\n\n\nWord not in corpus!\n')
        pass


while choice == '2':
    try:
        pos1 = input('\n\n\n\n___\n')
        neg1 = input('minus ___\n\n')
        pos2 = input('plus ___\n')

        print(
        w2v_model.wv.most_similar(positive=[pos1, pos2], negative=[neg1], topn=10))
    except Exception:
        print('\n\nNot found!\n\n')
        pass

while choice == '3':
    try:
        word = input('\nChoose a word to check context\n')
        print(w2v_model.predict_output_word(word,topn=100))

    except Exception:
        print('\n\n\nWord not in corpus!\n')
        pass
