import requests
import json
from pprint import pprint
from difflib import SequenceMatcher
import distance
import os

class DataField:
    '''
        name: String
        text: String
        numberLines: Number
    '''

    def __init__(self, name):
        self.name = name
        self.text = ''
        self.numberLines = 0

    
    def addText(self,text):
        self.numberLines += 1
        self.text += text + '\n'

    def __str__(self):
        return ("HEAD: {} \nNumber Lines: {}\n size: {}\n content: {}"
                .format(self.name, self.numberLines, len(self.text), self.text)) # bug aqui

    def getData(self):
        return { 'head': self.name, 'text': self.text, 'lines': str(self.numberLines), 'size': str(len(self.text))}


def cleanArray(nArray):
    for index in range(len(nArray) -1, -1, -1):
        i = nArray[index]
        if i == '':
            nArray.pop(index)


def extract_info(raw_text_array):
    head = ''
    text = ''
    values = {'': ''}
    words = [ 'Platform', 'Preconditions', 'Steps to reproduce', 'Expected result', 'Actual result', 'Reproducible', 'User Agent']
    findHead = False
    stepsNumber = 0
    data = {'': DataField('')}
    for phrase in raw_text_array:
        for word in words: 
            if word.lower() in phrase.lower():
                values['numberLines_' + head] = str(stepsNumber)
                
                stepsNumber = 0
                findHead = True
                
                head = word
                values[head] = ''
                data[head] = DataField(head)
                if (head == 'User Agent' or head == 'Reproducible'): # Case: User Agent: info info
                    final = 1
                    r = phrase.split(head)
                    if len(r) == 1:
                        final = 0
                    data[head].addText(phrase.split(head)[final])                    
                break
        
        if not findHead:
            stepsNumber += 1
            values[head] = values[head] + phrase
            data[head].addText(phrase)
        
        findHead = False

    # for key in data.keys(): # Print info in console to Debug
    #     #print('Chave', key)
    #     print(data[key])
    #     print()

    return data



FOLDER = '../download_script/data/'

bugs_list = os.listdir(FOLDER)

def filterText(text): 
    text = text.replace('STR', 'Steps to reproduce')
    text = text.replace('Plataform', 'Platform')
    text = text.replace('Result', 'Actual result')
    text = text.replace('Expectations', 'Expected result')
    text = text.replace('Prerequisites', 'Preconditions')
    text = text.replace('User-Agent', 'User Agent')

    return text


def writeCSV(data, summaryData, allInfo, startTime, endTime):
    words = [ 'Platform', 'Preconditions', 'Steps to reproduce', 'Expected result', 'Actual result', 'Reproducible', 'User Agent', '']

    line = summaryData + '§'
    
    for word in words:
        if word in data:
            dataField = data[word].getData()
            line += dataField['text'] + '§' + dataField['size'] + '§' + dataField['lines'] + '§'
        else:
            line += 'None§ None§ None§'

    line += allInfo + '§' + startTime + '§' + endTime
    with open('bug-report.csv', 'a') as f: 
        f.write('\n' + line.replace('\n',''))


# Function Main of program
def collectComment(bugId, commentPath, summaryPath, historyPath):  
    endTime = ''

    with open(historyPath,) as f:
        data = json.load(f)
        hist = data['bugs'][0]['history']
        endTime = hist[-1]['when']
    
    summary = ''
    with open(summaryPath,) as f:
        data = json.load(f)
        summaryData = data['bugs'][0]
        summary = '{} § {} § {} § {} § {} § {} § {}'.format(str(bug_id), summaryData['resolution'], summaryData['severity'], summaryData['type'], summaryData['status'], summaryData['classification'], str(summaryData['comment_count']))
    
    with open(commentPath,) as f:
        data = json.load(f)
        bug = data['bugs'][bug_id]['comments'][0]
        raw_text = bug['raw_text']
        startTime = bug['time']
        raw_text = filterText(raw_text)
        #print('Tamanho total', len(raw_text))
       
        raw_text_array = raw_text.split('\n')

        cleanArray(raw_text_array)
        extracted = extract_info(raw_text_array)
        writeCSV(extracted, summary, raw_text, startTime, endTime)

for bug_id in bugs_list:

    basic = FOLDER + bug_id + '/' + bug_id
    summary = basic + '_summary.json'
    comment = basic + '_comment.json'
    history = basic + '_history.json'
    #print(summary, history, comment)
    print(bug_id)
    collectComment(bug_id, comment, summary, history)
    print('-----------------------------')
