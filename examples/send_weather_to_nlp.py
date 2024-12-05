# some_file.py
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, './module')

from call_nlp import call_nlp
from call_weather_api import call_weather_api

results_weather = call_weather_api()
prompt = f"請解析後方的json文檔，告訴我台北市明日的天氣狀態。'{results_weather['臺北市']}'"
results = call_nlp(prompt)
print(results)