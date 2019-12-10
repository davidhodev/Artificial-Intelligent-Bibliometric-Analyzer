# Artificial Intelligent Bibliometric Analyzer: AIBA

AIBA is an Artificially Intelligent Natural Language Processor that can be used to group chemical reagants based on past academic research.

## Set Up

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

What things you need to install the software and how to install them

```
Give examples
```



## Usage
### Downloading Abstracts
Run the AbstractDownloader.py file in order to download Abstracts under a certain keyword you will enter. Do not forget to create your own SpringerNature and Elsevier API Keys.

```
python3 AbstractDownloader.py
```
This will download all abstracts with your keyword and can be run several times until completion. The abstracts will be downloaded with the DOI of the abstract as the names of files.

### Creating the Corpus

### Phrase To Vector

### Resave as Word2Vec to Tensor File

### Downloading Abstracts

### Generate Data and MetaData
```
python3 -m gensim.scripts.word2vec2tensor -i ~[Path to your Model] -o [Output e.g. 100SG for 100 Skip Gram]
```


### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo


### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

Add additional notes about how to deploy this on a live system

## Built With

* [Mat2Vec](https://github.com/materialsintelligence/mat2vec) - The Machine Learning Language Processor
* [Research Article](https://www.nature.com/articles/s41586-019-1335-8#Sec9) - The Google / Berkeley Article in which this research branched off of.

## Authors

* **David Ho** - *Initial work* - [Github](https://github.com/davidhodev)
* **Albert Shkolnik** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
