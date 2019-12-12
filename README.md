# Artificial Intelligent Bibliometric Analyzer: AIBA

AIBA is an Artificially Intelligent Natural Language Processor that can be used to group chemical reagants based on past academic research.

## Set Up

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Pybliometrics

```
pip3 install pybliometrics
```

Now navigate to the root folder of this repository and run the following command: 
```
pip install --ignore-installed -r requirements.txt
```

## Usage
### Downloading Abstracts
Run the AbstractDownloader.py file in order to download Abstracts under a certain keyword you will enter. Do not forget to create your own SpringerNature and Elsevier API Keys. Add these API Keys into APIKeys.txt. For the Elsevier API Key, open the config file ``` open ~/.scopus/config.ini ``` and enter your API Key in the correct field.

```
python3 AbstractDownloader.py
```
This will download all abstracts with your keyword and can be run several times until completion. The abstracts will be downloaded with the DOI of the abstract as the names of files.

### Creating the Corpus
Once you have the downloaded abstracts, you can create a corpus for your abstracts. Just run the CorpusMaker python file
```
python3 CorpusMaker.py
```

### Phrase To Vector
Now we want to convert our corpus to phrase2vec. Navigate to the mat2vec folder, training, and run the phrase2vec.py. For help, run ```python3 phrase2vec.py --help ```


### Resave as Word2Vec to Tensor File
Now resave the generated model to the tensor model. Run the NewModel.py code.
```python3 NewModel.py```


### Generate Data and MetaData
```
python3 -m gensim.scripts.word2vec2tensor -i ~[Path to your Tensor Model] -o [Output e.g. 100SG for 100 Skip Gram]
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
* **Neil Ferraro** - *Initial work*
* **Albert Shkolnik** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
