# some_file.py
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, './module')

from call_nlp import call_nlp

prompt = "hi"
results = call_nlp(prompt)
print(results)