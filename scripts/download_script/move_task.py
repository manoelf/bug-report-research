import requests
import json
import os
from aux import *
 
# Basic information
#FILENAME = 'bug-report.csv'
FILENAME = 'test.csv'
FOLDER = './data/'

def writeCSV(postData, summaryData, postRaw, startTime, endTime):    
    line = "{} § {} § {} § {} § {}".format(
        summaryData, postData, postRaw, startTime, endTime
    )

    with open(FILENAME, 'a') as f: 
        f.write('\n' + line.replace('\n',''))


'''
    Returns a String containing all information collected from the bug history
'''
def collectHistory(historyPath):
    endTime = ''

    with open(historyPath,) as f:
        data = json.load(f)
        hist = data['bugs'][0]['history']
        endTime = hist[-1]['when']

    return endTime

'''
    Returns a String containing all information collected from the bug history
'''
def collectSummary(summaryPath):
    summary = ''
    global notDefect
    with open(summaryPath,) as f:
        data = json.load(f)
        summaryData = data['bugs'][0]
        if not summaryData['type'] == 'defect':
            notDefect += 1
            os.rename(source,destination)
        print(summaryData['type'] == 'defect')
        summary = '{} § {} § {} § {} § {} § {} § {} § {}'.format(str(bug_id), 
            summaryData['resolution'], summaryData['severity'], 
            summaryData['type'], summaryData['status'], summaryData['classification'], 
            str(summaryData['comment_count']), summaryData['priority'])
    
    return summary

# Function Main of program

def transformToText(data):
    words = [ 'Platform', 'Preconditions', 'Steps to reproduce', 'Expected result', 'Actual result', 'Reproducible', 'User Agent', '']
    line = ''
    for word in words:
        if word in data:
            dataField = data[word].getData()
            line += dataField['text'] + '§' + dataField['size'] + '§' + dataField['lines'] + '§'
        else:
            line += 'None§ 0§ 0§'

    line = line[:-1]
    return line

def collectComment(bugId, commentPath, summaryPath, historyPath):  
    #endTime = collectHistory(historyPath)  
    summaryData = collectSummary(summaryPath)
    #print(summaryData)
    # Semantica misuturada
    # with open(commentPath,) as f:
    #     def loadData(file):
    #         data = json.load(file)
    #         return data['bugs'][bug_id]['comments'][0]
        
    #     bugReport = loadData(f)
    #     raw_text = filterText(bugReport['raw_text'])
    #     startTime = bugReport['time']
    #     #print('Tamanho total', len(raw_text))
       
    #     raw_text_array = raw_text.split('\n')

    #     cleanArray(raw_text_array)
    #     extracted = parsingPost(raw_text_array)
    #     postData = transformToText(extracted)
    #     writeCSV(postData, summaryData, raw_text, startTime, endTime)

count = 0
notDefect = 0

bugs_list = os.listdir(FOLDER)
for bug_id in bugs_list:

    basic = FOLDER + bug_id + '/' + bug_id
    summary = basic + '_summary.json'
    comment = basic + '_comment.json'
    history = basic + '_history.json'
    #print(summary, history, comment)
    print(bug_id)
    collectComment(bug_id, comment, summary, history)
    print('-----------------------------')
    count += 1
    if count == 5760:
        print('notDefect', notDefect)
        exit()