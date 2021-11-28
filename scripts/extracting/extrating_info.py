
# https://bugzilla.mozilla.org/rest/bug/724477
# https://bugzilla.mozilla.org/rest/bug/724477/comment


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
    continued = False
    words = [ 'Platform', 'Preconditions' 'Steps to reproduce', 'Expected result', 'Actual result']
    for palavra in raw_text_array:
        for word in words: 
            if word.lower() in palavra.lower():
                head = word
#                text += palavra
                values[head] = ''
                break
            
        values[head] = values[head] + palavra
        #frase = palavra.replace('**', '') # Remover negrito
        #print(frase)
        # if  frase in words:
        #     print(frase)



        # Version 1
        # frase = palavra.replace('https:', 'links#')
        # frase = frase.replace('http:', 'link#')
        # textoFormatado = frase
        # #print('-----------' + palavra + '----------------')
        # frase = testArray(frase.split(':'))
        # #frase = cleanArray(frase)
        # #print('xxxx', frase)
        # #print(textoFormatado)
        # if len(frase) > 1:
        #     if head in values: ## se já tem valor no dionário
        #         # print('xxxx...', head, values[head], text)
        #         # print()
        #         values[head] = values[head] + text
        #     else:
        #         values[head] = text
        #     head = frase[0]
        #     text = ''
        #     continued = False

        #     index = frase[0]
        #     values[index] = frase[1]
        #     # print(head,  values[index])
        # else:

        #     # print('head', head, 'text', text)
        #     # print(frase)
        #     if ': ' in textoFormatado:
        #         if continued == True:
        #             values[head] = text
        #             text = ''
        #         head = frase[0]
        #         continued = True
        #     else:
        #         text += frase[0]

        #print('head' + head + "-------------> text: " + text)
        ##print(frase, len(frase))

    #values[head] = values[head] + text
    #print(values)
    return values
    #print(raw_text_array)



FOLDER = 'data/'
#variaveis = os.walk(directory)

bugs_list = os.listdir(FOLDER)

bug_id = bugs_list[2]
print(bug_id)


basic = FOLDER + bug_id + '/' + bug_id
summary = basic + '_summary.json'
comment = basic + '_comment.json'
history = basic + '_history.json'

#links = { 'summary': summary, 'comment': comment, 'history': history }
links = { 'comment': comment}

#print(links)
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

#print(history, )


##id = '724477'
id = '808252'

# url = 'https://bugzilla.mozilla.org/rest/bug/' + id + '/comment'

# resp = requests.get(url=url)
# data = resp.json()


# with open(id + '.json', 'w') as f:
#     json.dump(data, f)

# print(data)

# exit()

#data = {'bugs': {'724477': {'comments': [{'author': 'sui.han@oracle.com', 'attachment_id': None, 'creator': 'sui.han@oracle.com', 'tags': [], 'count': 0, 'is_private': False, 'id': 6036788, 'bug_id': 724477, 'raw_text': "User Agent: Mozilla/5.0 (X11; SunOS i86pc; rv:9.0.1) Gecko/20100101 Firefox/9.0.1\nBuild ID: 20120110095621\n\nSteps to reproduce:\n\n1. Launch Firefox and Orca Speech.\n2. Click 'View' -> 'Character Encoding'\n3. Navigate the sub-menu of 'Character Encoding'\n\n\n\nActual results:\n\nThe sub-menu of 'Character encoding' can not be read by Orca.\n\n\nExpected results:\n\nThe sub-menu of 'Character encoding' should be read by Orca.", 'creation_time': '2012-02-06T08:21:46Z', 'time': '2012-02-06T08:21:46Z', 'text': "User Agent: Mozilla/5.0 (X11; SunOS i86pc; rv:9.0.1) Gecko/20100101 Firefox/9.0.1\nBuild ID: 20120110095621\n\nSteps to reproduce:\n\n1. Launch Firefox and Orca Speech.\n2. Click 'View' -> 'Character Encoding'\n3. Navigate the sub-menu of 'Character Encoding'\n\n\n\nActual results:\n\nThe sub-menu of 'Character encoding' can not be read by Orca.\n\n\nExpected results:\n\nThe sub-menu of 'Character encoding' should be read by Orca."}, {'bug_id': 724477, 'id': 6036793, 'count': 1, 'is_private': False, 'text': 'The firefox version is 10.0', 'time': '2012-02-06T08:24:54Z', 'creation_time': '2012-02-06T08:24:54Z', 'raw_text': 'The firefox version is 10.0', 'tags': [], 'creator': 'sui.han@oracle.com', 'attachment_id': None, 'author': 'sui.han@oracle.com'}, {'author': 'surkov.alexander@gmail.com', 'raw_text': 'Trevor, can you look please?', 'attachment_id': None, 'creation_time': '2012-02-07T11:24:33Z', 'time': '2012-02-07T11:24:33Z', 'text': 'Trevor, can you look please?', 'creator': 'surkov.alexander@gmail.com', 'tags': [], 'count': 2, 'is_private': False, 'id': 6040076, 'bug_id': 724477}]}}, 'comments': {}}

# with open('724477.json', 'w') as f:
#     json.dump(data, f)

# data = {'comments': {}, 'bugs': {'808252': {'comments': [{'time': '2012-11-03T01:10:23Z', 'creation_time': '2012-11-03T01:10:23Z', 'raw_text': 'User Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.2; .NET4.0E)\n\nSteps to reproduce:\n\nI am facing this issue since long time. keyboard navigation is not working properly on firefox browser. pressing home key does not get you to top of page and same with end key. also observed that on some web sites, navigating using up and down key gets you to very top or bottom of the page.\n\n\nActual results:\n\nusing up key on keyboard take you to top of the page rather than moving few lines upward\n\n\nExpected results:\n\nproper navigation of keyboard strokes..', 'text': 'User Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.2; .NET4.0E)\n\nSteps to reproduce:\n\nI am facing this issue since long time. keyboard navigation is not working properly on firefox browser. pressing home key does not get you to top of page and same with end key. also observed that on some web sites, navigating using up and down key gets you to very top or bottom of the page.\n\n\nActual results:\n\nusing up key on keyboard take you to top of the page rather than moving few lines upward\n\n\nExpected results:\n\nproper navigation of keyboard strokes..', 'count': 0, 'is_private': False, 'id': 6789665, 'bug_id': 808252, 'author': 'prakashpatel83@gmail.com', 'attachment_id': None, 'tags': [], 'creator': 'prakashpatel83@gmail.com'}, {'raw_text': 'Try basic troubleshooting steps:\n\n1) Safe mode: https://support.mozilla.org/en-US/kb/troubleshoot-firefox-issues-using-safe-mode\n\n2) New profile: https://support.mozilla.org/en-US/kb/profile-manager-create-and-remove-firefox-profiles\n\nDoes it fix your issue?', 'creation_time': '2012-11-03T11:13:15Z', 'attachment_id': None, 'time': '2012-11-03T11:13:15Z', 'author': 'epinal99-bugzilla2@yahoo.fr', 'creator': 'epinal99-bugzilla2@yahoo.fr', 'tags': [], 'text': 'Try basic troubleshooting steps:\n\n1) Safe mode: https://support.mozilla.org/en-US/kb/troubleshoot-firefox-issues-using-safe-mode\n\n2) New profile: https://support.mozilla.org/en-US/kb/profile-manager-create-and-remove-firefox-profiles\n\nDoes it fix your issue?', 'id': 6790055, 'count': 1, 'is_private': False, 'bug_id': 808252}, {'creator': 'prakashpatel83@gmail.com', 'tags': [], 'author': 'prakashpatel83@gmail.com', 'attachment_id': None, 'text': 'Tried with safe mode and problem still exists.', 'creation_time': '2012-11-04T00:21:19Z', 'raw_text': 'Tried with safe mode and problem still exists.', 'time': '2012-11-04T00:21:19Z', 'bug_id': 808252, 'is_private': False, 'count': 2, 'id': 6790753}, {'time': '2012-11-04T16:34:38Z', 'raw_text': '(In reply to Prakash from comment #2)\n> Tried with safe mode and problem still exists.\n\nTry with a new profile too, please.', 'creation_time': '2012-11-04T16:34:38Z', 'text': '(In reply to Prakash from comment #2)\n> Tried with safe mode and problem still exists.\n\nTry with a new profile too, please.', 'count': 3, 'is_private': False, 'id': 6791426, 'bug_id': 808252, 'author': 'epinal99-bugzilla2@yahoo.fr', 'attachment_id': None, 'tags': [], 'creator': 'epinal99-bugzilla2@yahoo.fr'}, {'tags': [], 'creator': 'ilphrin@autistici.org', 'author': 'ilphrin@autistici.org', 'attachment_id': None, 'text': 'Hi,\n\nAs it has been 7 years without any news on this, I think the bug can be marked as closed', 'time': '2019-04-07T11:03:53Z', 'creation_time': '2019-04-07T11:03:53Z', 'raw_text': 'Hi,\n\nAs it has been 7 years without any news on this, I think the bug can be marked as closed', 'bug_id': 808252, 'is_private': False, 'count': 4, 'id': 14037778}, {'author': 'daylin.trenton@zooape.net', 'creation_time': '2021-08-04T13:16:26Z', 'raw_text': "Firefox has no key to copy link since 88.\nFirefox removed the hotkey to copy link is 88. Firefox is now unusable by all of the people that used that shortcut. This is completely unreasonable.\n\nA replacement key that is unusable by human hands is not a replacement. It's not unlike telling people they can vote, if they stand in line for 8 hours without after. That is telling people that they can't vote.\n\nTelling people that there is a new key, but it's across the room where NO ONE, NO ONE can reach, is telling them that there is no key.\n\nFirefox has NO KEY to copy link currently.\n\nThere was no reason to break this, and I want you to know that I am never going to stop reporting it, and I will be identifying the people who broke it, like Asif Youssuff, personally, until it is identified as the bug that it is.\n\nYou broke a browser that millions of people depended on for NO REASON. NO REASON. There was NO REASON TO REMOVE THE HOTKEY TO COPY LINKS FROM FIREFOX.\n\n---\n\nSince someone is removing these legitimate bug reports, I am now leaving this as comments on other people's bug reports.", 'attachment_id': None, 'time': '2021-08-04T13:16:26Z', 'text': "Firefox has no key to copy link since 88.\nFirefox removed the hotkey to copy link is 88. Firefox is now unusable by all of the people that used that shortcut. This is completely unreasonable.\n\nA replacement key that is unusable by human hands is not a replacement. It's not unlike telling people they can vote, if they stand in line for 8 hours without after. That is telling people that they can't vote.\n\nTelling people that there is a new key, but it's across the room where NO ONE, NO ONE can reach, is telling them that there is no key.\n\nFirefox has NO KEY to copy link currently.\n\nThere was no reason to break this, and I want you to know that I am never going to stop reporting it, and I will be identifying the people who broke it, like Asif Youssuff, personally, until it is identified as the bug that it is.\n\nYou broke a browser that millions of people depended on for NO REASON. NO REASON. There was NO REASON TO REMOVE THE HOTKEY TO COPY LINKS FROM FIREFOX.\n\n---\n\nSince someone is removing these legitimate bug reports, I am now leaving this as comments on other people's bug reports.", 'creator': 'daylin.trenton@zooape.net', 'tags': ['abusive-reviewed', 'off-topic'], 'is_private': False, 'count': 5, 'id': 15514228, 'bug_id': 808252}]}}}

# print('Números de comentários', len(data['bugs'][id]['comments']))

# raw_text = data['bugs'][id]['comments'][0]['raw_text']


# raw_text_array = raw_text.split('\n')

# cleanArray(raw_text_array)


# head = ''
# text = ''
# values = {}
# continued = False
# for palavra in raw_text_array:
#     frase = palavra.split(': ')
#     if len(frase) > 1:
#         values[head] = text
#         head = ''
#         text = ''
#         continued = False

#         index = frase[0]
#         values[index] = frase[1]
#     else:

#         # print('head', head, 'text', text)
#         # print(frase)
#         if ':' in frase[0]:
#             if continued == True:
#                 values[head] = text
#                 text = ''
#             head = frase[0]
#             continued = True
#         else:
#             text += frase[0]
#     ##print(frase, len(frase))

# values[head] = text
# print(values)

# #print(raw_text_array)