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
finalWordDictionary = {}

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
            wordDictionary[word] = 1
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
    corpus = re.sub("®", "", corpus)
    corpus = re.sub("rac-", "", corpus)
    corpus = re.sub(" - ", "-", corpus)
    '''
    corpus = re.sub(r"\s\(\s\d+\s\)\s"," <count> ", corpus)
    corpus = re.sub(r"\s\(\s\d+\w\s\)\s"," <count> ", corpus)

    allPolyParenthesis = re.findall(r"poly\(\w+\)", corpus)
    for polyParenthesis in allPolyParenthesis:
        wordWithoutParenthesis = polyParenthesis.replace(')',"")
        wordWithoutParenthesis = wordWithoutParenthesis.replace('(',"")
        corpus.replace(polyParenthesis, wordWithoutParenthesis)
    '''


    corpus = corpus.replace("polypropene", "polypropylene")
    corpus = corpus.replace("polyethene", "polyethylene")

    corpus = corpus.replace("octene-1", "1-octene")
    corpus = corpus.replace("hexene-1", "1-hexene")

    corpus = corpus.replace("titanocenium", "titanocene")
    corpus = corpus.replace("zirconocenium", "zirconocene")
    corpus = corpus.replace("hafnocenium", "hafnocene")


    corpus = corpus.replace("(i)", "(I)")
    corpus = corpus.replace("(ii)", "(II)")
    corpus = corpus.replace("(iii)", "(III)")
    corpus = corpus.replace("(iv)", "(IV)")
    corpus = corpus.replace("( i )", "(I)")
    corpus = corpus.replace("( ii )", "(II)")
    corpus = corpus.replace("( iii )", "(III)")
    corpus = corpus.replace("( iv )", "(IV)")
    corpus = corpus.replace("( I )", "(I)")
    corpus = corpus.replace("( II )", "(II)")
    corpus = corpus.replace("( III )", "(III)")
    corpus = corpus.replace("( IV )", "(IV)")

    corpus = corpus.replace("(C ", "(C")
    corpus = corpus.replace("Cp'", "Cp")
    corpus = corpus.replace("cp2", "Cp2")
    corpus = corpus.replace("Cp2 ", "Cp2")
    corpus = corpus.replace(" 2Zr", "2Zr")

    corpus = corpus.replace("g mol", "gmol")
    corpus = corpus.replace("g*mol", "gmol")
    corpus = corpus.replace("Me 2", "Me2")

    corpus = corpus.replace("Cp2Ind2", "Cp2[Ind]2")
    corpus = corpus.replace("Cp2(Ind)2", "Cp2[Ind]2")
    corpus = corpus.replace("Et(Ind)2", "Et[Ind]2")
    corpus = corpus.replace("Et2(Ind)2", "Et2[Ind]2")

    corpus = corpus.replace("CPh3B(C6F5)4", "[CPh3][B(C6F5)4]")
    corpus = corpus.replace("[Ph3C][B(C6F5)4]", "[CPh3][B(C6F5)4]")
    corpus = corpus.replace("[Ph3C][B(C6F5)4", "[CPh3][B(C6F5)4]")
    corpus = corpus.replace("Ph3CB(C6F5)4", "[CPh3][B(C6F5)4]")


    corpus = corpus.replace("(n-BuCp)", "(nBuCp)")
    corpus = corpus.replace("i-Bu3Al", "Al(iBu)3")
    corpus = corpus.replace("AliBu3", "Al(iBu)3")

    corpus = corpus.replace("methylaluminoxane(MAO)", "methylaluminoxane ( MAO )")
    corpus = corpus.replace("Cp2ZrCl ", "Cp2ZrCl2 ")

    with open(path+'/mat2vec/training/data/'+modelName+".txt", 'w') as f:
        f.write(corpus)
        f.close()

    finalTotalCount = corpus.split()
    for word in finalTotalCount:
        finalWordDictionary[word] = 1
    print("WORD DICT: ", len(wordDictionary))
    print("FINAL WORD DICT: ", len(finalWordDictionary))
    print("HERE: ", finalWordDictionary)

def main():
    directory = input('Enter the name of the folder you wish to use to make your corpus\n')
    name = input('What would you like to call your corpus\n' )
    makeCorpus(directory + "/", name)
    print("DONE!")

if __name__ == "__main__":
    main()
