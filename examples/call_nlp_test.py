# some_file.py
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, './module')

import call_nlp

prompt = ""
results = call_nlp.call_nlp(prompt)
print(results)