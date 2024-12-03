import requests
import json
def call_nlp(prompt):
    if not prompt:
        return "empty prompt"
    # Define the URL and the payload
    url = 'http://122.116.26.243:11434/api/generate'
    #url = 'http://localhost:11434/api/generate'
    payload = {
        "model": "llama3.2",
        "prompt": prompt
    }

    # Convert the payload to a JSON string
    data = json.dumps(payload)

    # Make the POST request
    response = requests.post(url, data=data, headers={'Content-Type': 'application/json'})

    if response.status_code == 200:
        list_dict_words = []
        for each_word in response.text.split("\n"):
            try:
                data = json.loads(each_word)
            except:
                pass
            list_dict_words.append(data)

    llama_response = " ".join([word['response'] for word in list_dict_words if type(word) == type({})])
    return llama_response

"""
if you want to import this file, please use the following code.
"""
"""
# some_file.py
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, './module')
import call_nlp.py
"""