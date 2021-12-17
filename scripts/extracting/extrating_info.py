import requests
import json
import os
from aux import *

# Basic information
FILENAME = 'bug-report.csv'
FOLDER = '../download_script/data/'

bugs_list = os.listdir(FOLDER)


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
    with open(FILENAME, 'a') as f: 
        f.write('\n' + line.replace('\n',''))


# Function Main of program


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
    
    with open(summaryPath,) as f:
        data = json.load(f)
        summaryData = data['bugs'][0]
        summary = '{} § {} § {} § {} § {} § {} § {}'.format(str(bug_id), 
            summaryData['resolution'], summaryData['severity'], 
            summaryData['type'], summaryData['status'], summaryData['classification'], 
            str(summaryData['comment_count']))
    
    return summary

def collectComment(bugId, commentPath, summaryPath, historyPath):  
    endTime = collectHistory(historyPath)  
    summary = collectSummary(summaryPath)
   
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
    exit()