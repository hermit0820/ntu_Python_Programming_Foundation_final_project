# some_file.py
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, './module')

import call_nlp

print(call_nlp.call_nlp("hi"))