from fileinput import filename
import os
from jproperties import Properties
import argparse

from numpy import outer

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(r"dir",help="enter the path for saving properties files")
    args = parser.parse_args()

#Define Path and variables
folderpath = args.dir
filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]
all_files = []
configs = Properties()
key = 'PWD','Password','secret','Secret','Key','key','KEY'
unfoundkey='(secret)'


#Read properties files from prop folder
for path in filepaths:
    string = os.path.basename(path)
    string = string[:string.find('.properties')].strip()
    with open(path, 'rb') as config_file:
        configs.load(config_file)

#Config properties files from prop folder
        result = []
        items_view = configs.items()
        for item in items_view:
            Output=(string,'\:env\:',item[0],"=",item[1].data.replace(' ', ''))
            Output = "" .join(map(str, Output)) + ""
            if any (x in Output for x in key):
                Output=Output.replace('\:env\:', '\:secret\:')
                print(Output)
            result.append(Output)
        string = string+'.properties'
    
        for loc,a in enumerate(result):
            if a.endswith('='):
                result[loc] = a.replace('=','=undefined')
        for loc1,b in enumerate(result):
            if b.endswith(unfoundkey):
                result[loc1] = b.replace(unfoundkey,'').replace('\:env\:', '\:secret\:')
                print(result[loc1])
 #Create a new properties files  
    with open(string, 'x') as f:
        for abc in result:
            f.write(str(abc))
            f.write('\n')