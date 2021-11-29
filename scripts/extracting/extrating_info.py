import requests
import json
from pprint import pprint
from difflib import SequenceMatcher
import distance
import os

def similar(a, b):
    return distance.sorensen(a,b)


def cleanArray(nArray):
    for index in range(len(nArray) -1, -1, -1):
        i = nArray[index]
        if i == '':
            nArray.pop(index)


def testArray(nArray): # TODO: Possui um erro aqui
    copy_array = nArray[:]
    for index in range(len(copy_array) -1, -1, -1):
        item = copy_array[index]
        if len(item.strip()) == 0:
            copy_array.pop(index)

    return copy_array



def print_info(raw_array):
    for name in raw_array.keys():
        print(name + ' -> ' + raw_array[name])
        print('##########')

def extract_info(raw_text_array):
    head = ''
    text = ''
    values = {'': ''}
    words = [ 'Platform', 'Preconditions', 'Steps to reproduce', 'Expected result', 'Actual result']
    findHead = False
    stepsNumber = 0
    for palavra in raw_text_array:
        for word in words: 
            #print('Test:', palavra, word) # Debug
            if word.lower() in palavra.lower():
                #  Statics
                values['numberLines_' + head] = str(stepsNumber)
                
                # reset values
                stepsNumber = 0
                findHead = True
                
                #print('Macth: ', word, palavra) # Debug
                head = word
                values[head] = ''
                break
        
        if not findHead:
            stepsNumber += 1
            values[head] = values[head] + palavra
        
        findHead = False
    return values



FOLDER = 'data/'
#variaveis = os.walk(directory)

bugs_list = os.listdir(FOLDER)

bug_id = bugs_list[4]
print(bug_id)


basic = FOLDER + bug_id + '/' + bug_id
summary = basic + '_summary.json'
comment = basic + '_comment.json'
history = basic + '_history.json'

#links = { 'summary': summary, 'comment': comment, 'history': history }
links = { 'comment': comment}

for name in links.keys():
    with open(links[name],) as f:
        data = json.load(f)
        raw_text = data['bugs'][bug_id]['comments'][0]['raw_text']
        #pprint(raw_text)

        raw_text_array = raw_text.split('\n')

        cleanArray(raw_text_array)
        extracted = extract_info(raw_text_array)
        print_info(extracted)
    exit()



##id = '724477'
id = '808252'