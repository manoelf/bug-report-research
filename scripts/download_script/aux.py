import requests
import json
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

def parsingPost(raw_text_array):
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


def filterText(text): 
    text = text.replace('STR', 'Steps to reproduce')
    text = text.replace('Plataform', 'Platform')
    text = text.replace('Result', 'Actual result')
    text = text.replace('Expectations', 'Expected result')
    text = text.replace('Prerequisites', 'Preconditions')
    text = text.replace('User-Agent', 'User Agent')

    return text

