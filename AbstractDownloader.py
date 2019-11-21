from pybliometrics.scopus import ScopusSearch
from pybliometrics.scopus import AbstractRetrieval
import urllib.request, json
import pandas as pd
import os
import time
from tqdm import tqdm
import sys

'''
This Program will query Pybliometrics as well as SpringerNature based off key words
to download abstracts to train our neural network.
'''

'''
Get all API Keys
'''



'''
Retreives the abstracts from the Springer Nature API
API gives a JSON that needs to be parsed.
Make sure to enter your own Springer Nature API key
'''
def springerNatureAbstracts(searchTerm, destination):
	doiAbstractDictionary = {}
    #API KEY
	with urllib.request.urlopen("http://api.springernature.com/meta/v2/json?q=title:%22"+searchTerm+"%22&s=1&p=100&api_key=1a9041505fecd88e690023546c5d857f") as url:
		data = [json.loads(url.read().decode())]
		with open('requests.json', 'w') as outfile:
			json.dump(data[0], outfile)

	totalNumberOfAbstracts = int(data[0]['result'][0]['total'])
	data.pop()

	print("Number of Results from Springer Nature: ", totalNumberOfAbstracts)
	for i in range(0,totalNumberOfAbstracts//100):
		with urllib.request.urlopen("http://api.springernature.com/meta/v2/json?q=title:%22"+searchTerm+"%22&s="+ str(i*100)+ "&p=100&api_key=1a9041505fecd88e690023546c5d857f") as url:
			data.append(json.loads(url.read().decode()))

    # Going through and creating a dictionry with the DOI as the key and the abstract as the value

	blankDOICount = 0
	for i in range(len(data)):
		for k in range(len(data[i]['records'])):
			titleName = data[i]['records'][k]['doi']
			if titleName and titleName != "":
				titleName = titleName.replace("/","--s")
			else:
				titleName = ""+searchTerm+"_blankSpringer_"+str(blankDOICount)+""
				blankDOICount+=1
			with open(os.path.join(destination,data[i]['records'][k]['doi'] + '.txt'), 'w') as f:
				data[i]['records'][k]['abstract']
			doiAbstractDictionary[data[i]['records'][k]['doi']] = data[i]['records'][k]['abstract']

	return doiAbstractDictionary


'''
Elsevier Abstract download
'''
def elsevierAbstracts(search, destination):
	option = input('Enter 1 for Exact search, 0 for inexact search\n')
	count = 0
	if option == '1':
		query = '{' + search + '}' # exact search
	else:
		query = 'TITLE-ABS-KEY( ' + search + ')' # inexact search

	print("This may take a while...")

	scopusSearchAbstracts = ScopusSearch(query, download=False)
	length = scopusSearchAbstracts.get_results_size()
	print('Number of results from Elsevier: ', length)

	s = ScopusSearch(query, download=True)
	dataframe = pd.DataFrame(pd.DataFrame(s.results)) # converts results into a dataframe
	pd.options.display.max_colwidth = 150
	pd.options.display.max_rows = None
	print(dataframe[['doi', 'title']])
	dataframe.iloc[:,0] = dataframe.iloc[:,0].astype(str) # converts the eid dataframe objects to string

	for i in progressbar(range(length), "Download Progress ", 40):
		try:
			ab = AbstractRetrieval(dataframe.iloc[i,0],view='FULL') # searches for abstracts using eid
			titleName = dataframe.iloc[i,1]
			if titleName and titleName != "":
				titleName = titleName.replace("/", "--")
			else:
				titleName = ""+search+"_blankElsevier_"+str(count)+""
				count += 1
			with open(os.path.join(destination,titleName + '.txt'), 'w') as f:
				f.write("%s\n" % ab.abstract) #creates individual txt files titled by their eid
		except:
			pass


'''
Generates all Abstracts
'''
def generateAbstracts():
	search = input('Enter Search Terms\n')
	destinationFolder = input('Enter the name of the folder you wish to download to\n')
	destination = os.getcwd()+ '/'+destinationFolder
	if not os.path.exists(destination):
		os.makedirs(destination)

	elsevierAbstracts(search, destination)
	springerNatureAbstracts(search, destination)



'''
Progress Bar to illustrate loading
'''
def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()


def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	generateAbstracts()

if __name__ == "__main__":
	main()
