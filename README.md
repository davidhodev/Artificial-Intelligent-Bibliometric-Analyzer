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



### Break down into tests

We have a preset list of analogies of approximately 40,000 analogies to test the model you decide to create. All you have to do is feed your models into TestRegime.py in order to see the best model for your anologies, whether you choose to use your own or ours.

```
python3 TestRegime.py
```

Add additional notes about how to deploy this on a live system

## Built With

* [Mat2Vec](https://github.com/materialsintelligence/mat2vec) - The Machine Learning Language Processor
* [Research Article](https://www.nature.com/articles/s41586-019-1335-8#Sec9) - The Google / Berkeley Article in which this research branched off of.

## Authors

* **David Ho** - [Github](https://github.com/davidhodev)
* **Neil Ferraro**
* **Albert Shkolnik**
* **Benjamin Rizkin** 
* **Hartman Labs** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
