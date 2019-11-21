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

os.system('cls' if os.name == 'nt' else 'clear')

def springerNatureAbstracts(searchTerm):
	count=0
	doiAbstractDictionary = {}
	with urllib.request.urlopen("http://api.springernature.com/meta/v2/json?q=title:%22"+searchTerm+"%22&s=1&p=100&api_key=1a9041505fecd88e690023546c5d857f") as url:
		data = [json.loads(url.read().decode())]
		with open('requests.json', 'w') as outfile:
			json.dump(data[0], outfile)

	totalNumberOfAbstracts = int(data[0]['result'][0]['total'])
	data.pop()
	print(totalNumberOfAbstracts)
	for i in range(0,totalNumberOfAbstracts//100):
		with urllib.request.urlopen("http://api.springernature.com/meta/v2/json?q=title:%22microfluidics%22&s="+str(i*100)+"&p=100&api_key=1a9041505fecd88e690023546c5d857f") as url:
			data.append(json.loads(url.read().decode()))
		with urllib.request.urlopen("http://api.springernature.com/meta/v2/json?q=title:%22microfluidics%22&s="+ str(totalNumberOfAbstracts-(totalNumberOfAbstracts%100))+ "&p=" +str(totalNumberOfAbstracts%100)+ "&api_key=1a9041505fecd88e690023546c5d857f") as url:
			data.append(json.loads(url.read().decode()))

	listy = []
	destination = '/home/benjamin/Python_Codes/AI-Microreactor/Zr_Abstracts'


	for i in range(len(data)):
		for k in range(len(data[i]['records'])):
			titleName = data[i]['records'][k]['doi']
			if titleName and titleName != "":
				titleName = titleName.replace("/","--s")
			else:
				titleName = "blankSpringer_"+str(count)+""
				count+=1
			with open(os.path.join(destination,data[i]['records'][k]['doi'] + '.txt'), 'w') as f:
				data[i]['records'][k]['abstract']

			doiAbstractDictionary[data[i]['records'][k]['doi']] = data[i]['records'][k]['abstract']

	return doiAbstractDictionary

def generateAbstracts():
	count = 0
	search = input('Enter Search Terms\n')
	option = input('Enter 1 for Exact search, 0 for inexact search\n')

	if option == '1':
		query = '{' + search + '}' # exact search
	else:
		query = 'TITLE-ABS-KEY( ' + search + ')' # inexact search

	scopusSearchAbstracts = ScopusSearch(query, download=False)


	length = scopusSearchAbstracts.get_results_size()
	print('Number of results: ', length)

	if length > 0:
		dl = input('Would you like to download the results y/n\n')
		if dl == 'y':
			s = ScopusSearch(query, download=True)
			dataframe = pd.DataFrame(pd.DataFrame(s.results)) # converts results into a dataframe
			pd.options.display.max_colwidth = 150
			pd.options.display.max_rows = None
			print(dataframe[['eid', 'title']])
			dataframe.iloc[:,0] = dataframe.iloc[:,0].astype(str) # converts the eid dataframe objects to string

			decision = input('Enter "abstract" to dl abstractrs or enter "info" to retrieve urls\n')

			if decision == 'abstract':

				option2 = input('\n Enter the row of the abstract you want to download, or enter ALL to download all\n')

				destinationFolder = input('Enter the name of the folder you wish to download to\n')
				destination = '/home/benjamin/Python_Codes/AI-Microreactor/' + destinationFolder
				if not os.path.exists(destination):
					os.makedirs(destination)

				if option2 == 'ALL':
					print("Number of Results of springernature:")
					out = springerNatureAbstracts(search)
					print(len(out))
					for i in progressbar(range(length), "Download Progress ", 40):
						try:
							ab = AbstractRetrieval(dataframe.iloc[i,0],view='FULL') # searches for abstracts using eid
							titleName = dataframe.iloc[i,1]
							if titleName and titleName != "":
								titleName = titleName.replace("/", "--")
							else:
								titleName = "blankOther_"+str(count)+""
								count += 1
							with open(os.path.join(destination,titleName + '.txt'), 'w') as f:
								f.write("%s\n" % ab.abstract) #creates individual txt files titled by their eid
						except:
							pass
				else:
					try:
						val = int(option2)
						print('Attempting to download abstract with eid ' + dataframe.iloc[val,0])
						ab = AbstractRetrieval(dataframe.iloc[val,0],view='FULL') # searches for abstracts using eid
						with open(os.path.join(destination,dataframe.iloc[val,0] + '.txt'), 'w') as f:
							f.write("%s\n" % ab.abstract)
						print('Success!\n')
					except ValueError:
						print('Invalid row number\n')

			else:
				optionInfo = input('\n Enter the row of the info you want to download, or enter ALL to download all\n')

				destinationFolder = input('Enter the name of the folder you wish to download to\n')
				destination = '/home/benjamin/Python_Codes/AI-Microreactor/' + destinationFolder

				if not os.path.exists(destination):
					os.makedirs(destination)

				if optionInfo == 'ALL':
					for i in progressbar(range(length), "Download Progress ", 40):
						ab = AbstractRetrieval(dataframe.iloc[i,0],view='FULL') # searches for abstracts using eid
						if datafram.iloc[i,0] is not None:
							with open(os.path.join(destination,dataframe.iloc[i,0] + '.txt'), 'w') as f:
								f.write("%s\n" % dataframe.iloc[i,4])
								f.write("%s\n" % ab.scopus_link) #creates individual txt files titled by their eid
						else:
							with open(os.path.join(destination,dataframe.iloc[i,1] + '.txt'), 'w') as f:
								f.write("%s\n" % dataframe.iloc[i,4])
								f.write("%s\n" % ab.scopus_link) #creates individual txt files titled by their eid
				else:
					try:
						val = int(optionInfo)
						print('Attempting to download info with eid ' + dataframe.iloc[val,0])
						ab = AbstractRetrieval(dataframe.iloc[val,0],view='FULL') # searches for abstracts using eid
						with open(os.path.join(destination,dataframe.iloc[val,0] + '.txt'), 'w') as f:
							f.write("%s\n" % dataframe.iloc[val,4])
							f.write("%s\n" % ab.scopus_link)
						print('Success!\n')
					except ValueError:
						print('Invalid row number\n')
	else:
		print('No results found, please try again\n')



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
	generateAbstracts()

if __name__ == "__main__":
	main()
