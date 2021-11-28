

import time
import requests
import json
import os
# https://bugzilla.mozilla.org/rest/bug/ID - sumário
# https://bugzilla.mozilla.org/rest/bug/ID/comment - comentários
# https://bugzilla.mozilla.org/rest/bug/ID/history - histórico

# informações dos usuários(estatísticas) não tem na API
    # https://bugzilla.mozilla.org/user_profile?user_id=55

FILENAME = 'bugs_ids.txt'
FOLDER = 'data'
URL = 'https://bugzilla.mozilla.org/rest/bug/'

with open(FILENAME, "r") as a_file:
  for line in a_file:
    bug_id = line.strip()
    
    summary = URL + bug_id
    comment = summary + '/comment'
    history = summary + '/history'

    links = { 'summary': summary, 'comment': comment, 'history': history }
    


    os.mkdir(FOLDER + '/' + bug_id)

    
    for name in links.keys():
        resp = requests.get(url=links[name])
        data = resp.json()
        
        filename = "{}/{}/{}_{}.json".format(FOLDER, bug_id, bug_id, name)
    
        with open(filename, 'w') as f:
            json.dump(data, f)

    print(summary)
    print(history)
    print(comment)
    print()
    time.sleep(40)