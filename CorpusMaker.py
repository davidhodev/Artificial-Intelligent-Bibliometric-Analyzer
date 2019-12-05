from __future__ import absolute_import, division, print_function, unicode_literals
import os
import numpy as np
from nltk import *
from collections import OrderedDict
import math
import operator
import string
import re
from mat2vec.processing import MaterialsTextProcessor
from string import punctuation

''' Constants '''
path = os.getcwd()
text_processor = MaterialsTextProcessor()
wordDictionary = {}

def makeCorpus(directory, modelName):
    totalNumberOfAbstracts = 0
    corpus = ''
    abstractFiles = os.listdir(str(directory))
    abstractFiles.sort()
    for file in abstractFiles:
        totalNumberOfAbstracts += 1
        infile = open(path+"/"+str(directory) + str(file))
        abstract = infile.read()

        # Process Each Abstract and Add to Corpus
        processedAbstract = text_processor.process(abstract)
        newAbstract = ''
        for word in processedAbstract[0]:
            newAbstract = newAbstract + word + ' '
        corpus = corpus + newAbstract + '\n'
        infile.close()

    newCorpus = ""
    count = 0
    # Removes Copyrights and All Rights Reserved
    sentencesWithLineBreaks = []
    for sentenceWithLineBreaks in corpus.splitlines():
        sentences = tokenize.sent_tokenize(sentenceWithLineBreaks)
        for sentence in sentences:
            if "©" in sentence or "copyright" in sentence:
                count += 1
            else:
                newCorpus += sentence + " "
        newCorpus += "\n"
    corpus = newCorpus
    print(count, "removed Copyrights")


    corpus = re.sub("aluminium", "aluminum", corpus)
    corpus = re.sub("alumoxane", "aluminoxane", corpus)
    corpus = re.sub("all rights reserved.", "", corpus)
    corpus = re.sub("all rights reserved", "", corpus)
    corpus = re.sub(r"\s\(\s\d+\s\)\s"," <count> ", corpus)
    corpus = re.sub(r"\s\(\s\d+\w\s\)\s"," <count> ", corpus)
    allPolyParenthesis = re.findall(r"poly\(\w+\)", corpus)
    for polyParenthesis in allPolyParenthesis:
        wordWithoutParenthesis = polyParenthesis.replace(')',"")
        wordWithoutParenthesis = wordWithoutParenthesis.replace('(',"")
        corpus.replace(polyParenthesis, wordWithoutParenthesis)


    corpus = corpus.replace("polypropene", "polypropylene")
    corpus = corpus.replace("polyethene", "polyethylene")


    corpus = corpus.replace("(i)", "(I)")
    corpus = corpus.replace("(ii)", "(II)")
    corpus = corpus.replace("(iii)", "(III)")
    corpus = corpus.replace("(iv)", "(IV)")
    corpus = corpus.replace("( i )", "( I )")
    corpus = corpus.replace("( ii )", "( II )")
    corpus = corpus.replace("( iii )", "( III )")
    corpus = corpus.replace("( iv )", "( IV )")

    with open(path+'/mat2vec/training/data/'+modelName+".txt", 'w') as f:
        f.write(corpus)
        f.close()

def main():
    directory = input('Enter the name of the folder you wish to use to make your corpus\n')
    name = input('What would you like to call your corpus\n' )
    makeCorpus(directory + "/", name)
    print("DONE!")

if __name__ == "__main__":
    main()
