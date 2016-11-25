import pandas as pd
import numpy as np
import re
univ_towns = open('university_towns.txt', 'r')
univ_towns_dict = {}
lines = univ_towns.read().split('\n')
#print(lines)
univ_towns.close()
for line in lines:
    #print(line)
    if '[edit]' in line:
        regex = re.compile('([a-z A-Z]*)\[edit\].*')
        re_match = re.match(regex, line)
        currentState = re_match.group(1)
        #print(currentState)
        if currentState not in univ_towns_dict:
            univ_towns_dict[currentState] = []
        #print(re_match.group())
    else:
        if ' (' in line:
            for index in range(len(line)):
                if line[index] == ' ' and line[index + 1] == '(':
                    indexToKeep = index
                    break
            if ',' in line[:indexToKeep] and line[:indexToKeep] not in univ_towns_dict[currentState]:
                univ_towns_dict[currentState].append(line[:indexToKeep].split(',')[0])   
            else:
                if line[:indexToKeep] not in univ_towns_dict[currentState]:
                    univ_towns_dict[currentState].append(line[:indexToKeep])
        else:
            if ',' in line and line.split(',')[0] not in univ_towns_dict[currentState]:
                univ_towns_dict[currentState].append(line.split(',')[0])   
            else:
                if line.split(',')[0] not in univ_towns_dict[currentState]:
                    univ_towns_dict[currentState].append(line)
        #print(line)
        #if ':' in line and '(' not in line:
        #    pass
        #elif 'Faribault' in line:
        #    univ_towns_dict[currentState].append('Faribault')  
        #elif 'North Mankato' in line:
        #    univ_towns_dict[currentState].append('North Mankato')  
        #else:
        #    for index in range(len(line)):
        #        #print(line[index], line[index+1])
        #        if line[index] == ' ' and line[index + 1] == '(':
        #            indexToKeep = index
        #            break
        #    univ_towns_dict[currentState].append(line[:indexToKeep])


return_list = []
for key in univ_towns_dict:
    for i in univ_towns_dict[key]:
        return_list.append([key, i])
return_list = sorted(return_list, key = lambda x : (x[0], x[1]))
#print(return_list)

df = pd.DataFrame(return_list, columns = ['State', 'RegionName'])
df.to_csv('output.csv')