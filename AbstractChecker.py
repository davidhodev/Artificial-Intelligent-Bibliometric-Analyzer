import os
import numpy as np
import pandas as pd
from mat2vec.processing import MaterialsTextProcessor

''' Constants '''
path = 'mat2vec/training/AllAbstracts'
text_processor = MaterialsTextProcessor()
catalyst_names = ['Cp*Ti(OBz)3','Cp2ZrCl2','Cp2ZrCl','Cp2HfCl2','Cp2TiCl2','EtInd2ZrCl2','(nBuCp)2ZrCl2','Et[Ind]2ZrCl2','Et(Ind)2ZrCl2','(n-BuCp)2ZrCl2','(SBI)ZrMe2',
'Cp2TiMe2','Cp2ZrMe2','Cp2HfMe2','Me2SiInd2ZrCl2','CpZrCl3','CpTiCl3','CpHfCl3','Cl4Ti','Cp*ZrMe3','B(C6F5)3']
activator_names = ['MAO','TIBA','TEA','TIBAO','MMAO','methylaluminoxane','triethylaluminum','triisobutylaluminum','Et3Al','AlEt3','AlEtCl2','AlEt2Cl','tris(pentafluorophenyl)borane',
'[CPh3][B(C6F5)4]','CPh3B(C6F5)4','ethylaluminoxane','tetrachloroaluminate','tri-isobutylaluminum','methyl-aluminoxane','tetrakis(pentafluorophenyl)borane']

abstractFiles = os.listdir(path)
abstractFiles.sort()

ARRAY = np.zeros((len(catalyst_names),len(activator_names)))

for file in abstractFiles:
    catalystlist = []
    activatorlist = []

    infile = open(path+"/"+str(file))
    abstract = infile.read()

    processedAbstract = text_processor.process(abstract)
    for i in range(len(processedAbstract[0])):
        if processedAbstract[0][i] in catalyst_names:
            if processedAbstract[0][i] not in catalystlist:
                catalystlist.append(processedAbstract[0][i])
        if processedAbstract[0][i] in activator_names:
            if processedAbstract[0][i] not in activatorlist:
                activatorlist.append(processedAbstract[0][i])

    for j in range(len(catalystlist)):
        idx = catalyst_names.index(catalystlist[j])
        for k in range(len(activatorlist)):
            idx2 = activator_names.index(activatorlist[k])
            ARRAY[idx][idx2] += 1
    infile.close()


ARRAY = pd.DataFrame(ARRAY, index = catalyst_names, columns = activator_names)
ARRAY['MAO'] += ARRAY['methylaluminoxane'] + ARRAY['methyl-aluminoxane']
ARRAY['TEA'] += ARRAY['triethylaluminum'] + ARRAY['AlEt3'] + ARRAY['Et3Al']
ARRAY['TIBA'] += ARRAY['triisobutylaluminum'] + ARRAY['tri-isobutylaluminum']
ARRAY['B(C6F5)3'] += ARRAY['tris(pentafluorophenyl)borane']
ARRAY.loc['Cp2ZrCl2'] += ARRAY.loc['Cp2ZrCl']
ARRAY['[CPh3][B(C6F5)4]'] += ARRAY['CPh3B(C6F5)4'] + ARRAY['tetrakis(pentafluorophenyl)borane']
ARRAY.loc['Et[Ind]2ZrCl2'] += ARRAY.loc['EtInd2ZrCl2'] + ARRAY.loc['Et(Ind)2ZrCl2']
ARRAY.loc['(nBuCp)2ZrCl2'] += ARRAY.loc['(n-BuCp)2ZrCl2']
ARRAY = ARRAY.drop(['methylaluminoxane','methyl-aluminoxane'],axis = 1)
ARRAY = ARRAY.drop(['triethylaluminum','AlEt3','Et3Al'],axis = 1)
ARRAY = ARRAY.drop(['triisobutylaluminum','tri-isobutylaluminum'],axis = 1)
ARRAY = ARRAY.drop(['CPh3B(C6F5)4','tetrakis(pentafluorophenyl)borane'],axis = 1)
ARRAY = ARRAY.drop('tris(pentafluorophenyl)borane',axis = 1)
ARRAY = ARRAY.drop(['EtInd2ZrCl2','Et(Ind)2ZrCl2'])
ARRAY = ARRAY.drop(['Cp2ZrCl'])
ARRAY = ARRAY.drop('(n-BuCp)2ZrCl2')
ARRAY.transpose()
print(ARRAY)
ARRAY.to_csv()
with open('CatalystActivatorResults.csv', 'w') as f:
    f.write(ARRAY.to_csv())
    f.close()
