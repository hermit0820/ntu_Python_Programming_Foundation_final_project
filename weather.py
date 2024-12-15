import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import requests
import json
import threading


def process_weather_data(weather_data):
    # 提取必要資訊
    weather_status = weather_data.get("天氣現象", "未知")
    temperature = int(weather_data.get("最低溫", "未知"))
    rain_prob = int(weather_data.get("降雨機率", "0"))

    suggestions = []

    # 溫度建議
    if temperature < 10:
        suggestions.append("建議穿厚重的大衣和保暖長褲，搭配雪地靴。")
        suggestions.append("戴手套、圍巾和毛帽保暖。")
    elif 10 <= temperature < 20:
        suggestions.append("建議穿夾克或毛衣，以及長褲。")
        suggestions.append("穿保暖運動鞋，並攜帶輕便帽子保暖。")
    elif 20 <= temperature < 30:
        suggestions.append("建議穿輕便T恤和牛仔褲，搭配運動鞋。")
    else:  # temp >= 30
        suggestions.append("建議穿短袖T恤和短褲，搭配涼鞋或輕便鞋。")
        suggestions.append("戴輕便帽子以遮陽。")

    # 根據溫度決定頭部穿戴
    if temperature >= 30:
        suggestions.append("戶外建議戴輕便的帽子以遮陽。")
    elif 20 <= temperature < 30:
        suggestions.append("戶外活動戴鴨舌帽帽子防曬。")
    elif 10 <= temperature < 20:
        suggestions.append("可以戴輕便的帽子保暖。")
    elif 0 <= temperature < 10:
        suggestions.append("建議戴毛帽或圍巾保暖。")
    else:
        suggestions.append("建議戴厚重的帽子和圍巾保暖。")

    # 降雨機率建議
    if rain_prob > 50:
        suggestions.append("降雨機率較高，請攜帶雨傘或穿雨衣，並選擇防水鞋款。")
    elif 20 < rain_prob <= 50:
        suggestions.append("可能有小雨，建議攜帶輕便雨具。")

    # 根據溫度提供顏色建議
    if temperature >= 30:
        suggestions.append("建議選擇淺色（如白色、米色），減少吸熱效果。")
    elif 20 <= temperature < 30:
        suggestions.append("建議選擇中性色調（如灰色、卡其色），保持舒適耐看。")
    elif 10 <= temperature< 20:
        suggestions.append("建議選擇暖色調（如深棕色、橄欖綠），增加視覺暖意。")
    elif temperature < 10:
        suggestions.append("建議選擇深色（如黑色、深藍色），吸熱且保暖。")

    # 根據降雨機率添加 建議
    if rain_prob > 50:
        suggestions.append("同時建議選擇深色衣物，避免雨水濕透後透光。")

    # 結合所有建議
    return " ".join(suggestions)

def call_nlp(prompt):
    if not prompt:
        return "empty prompt"
    # Define the URL and the payload
    url = 'http://122.116.26.243:11434/api/generate'
    #url = 'http://localhost:11434/api/generate'
    payload = {
        "model": "llama3.2-vision",
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

def call_weather_api():
    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-2DBA06BF-8B31-481D-B1D0-7A3D76502B2A"
    response = requests.get(url)
    json_api = json.loads(response.text)
    location = json_api["records"]["location"]
    element_dict = {}
    city = city_var.get().strip() # 縣市名稱
    """
    wx = {}
    pop = {}
    mint = {}
    ci = {}
    maxt = {}
    """
    weather_element = None
    for loc in location:
        if loc["locationName"] == city:
            weather_element = loc["weatherElement"]
            break
    if not weather_element:
        return {"錯誤": "無法取得該城市的天氣資訊"}
    for counter in range(0, 3):
        time = weather_element[0]["time"][counter]["startTime"]
        element_dict[time] = {
            "天氣現象": weather_element[0]["time"][counter]["parameter"]["parameterName"],
            "降雨機率": weather_element[1]["time"][counter]["parameter"]["parameterName"],
            "最低溫": weather_element[2]["time"][counter]["parameter"]["parameterName"],
            "舒適度": weather_element[3]["time"][counter]["parameter"]["parameterName"],
            "最高溫": weather_element[4]["time"][counter]["parameter"]["parameterName"]
        }
    return element_dict

def fetch_weather_data():
    if city_var.get().strip() == "請選擇欲查詢城市":
        print("ff")
        suggestion_display.config(state=tk.NORMAL)  # 允許編輯
        suggestion_display.delete("1.0", tk.END)
        suggestion_display.insert(tk.END, "請選擇一個有效的城市名稱。")
        return
    else :
        suggestion_display.config(state=tk.NORMAL)  # 允許編輯
        suggestion_display.delete("1.0", tk.END)    # 清空現有內容
        suggestion_display.insert(tk.END, f"請稍後......")  #等待訊息
        # 啟動子執行緒
        threading.Thread(target=task).start()

def task():
    # 在子執行緒中運行的邏輯
    try:
        weather_data = call_weather_api()
        if "錯誤" in weather_data:
            suggestion_display.insert(tk.END, weather_data["錯誤"])
        else:
            latest_data = list(weather_data.values())[0]
            for key, value in latest_data.items():
                if key in weather_info:
                    weather_info[key].set(value)
            prompt = (
                "請用繁體中文根據以下資訊生成穿搭建議，且不另外列出天氣資訊和活動類型資訊："
                + str(latest_data)
                + "，粗估穿搭："
                + process_weather_data(latest_data)
                + "，活動類型："
                + str(activity_var.get().strip())
            )
            response = call_nlp(prompt)
            suggestion_display.delete("1.0", tk.END)
            suggestion_display.insert(tk.END, response)
    except Exception as e:
        suggestion_display.insert(tk.END, f"發生錯誤：{e}")
    finally:
        suggestion_display.config(state=tk.DISABLED)  # 禁用編輯



# 初始化主視窗
root = tk.Tk()
root.title("天氣穿衣建議")
root.geometry("400x700")
root.resizable(True, True)

# 標題
title_label = tk.Label(root, text="天氣穿衣建議", font=("Arial", 20))
title_label.pack(pady=10)

# 城市選擇
city_label = tk.Label(root, text="城市選擇：", font=("Arial", 12))
city_label.pack(anchor="w", padx=20)
city_var = tk.StringVar()
city_list = [
    "請選擇欲查詢城市","臺北市", "新北市", "基隆市", "桃園市", "新竹市", "新竹縣",
    "苗栗縣", "臺中市", "彰化縣", "南投縣", "雲林縣", "嘉義市",
    "嘉義縣", "臺南市", "高雄市", "屏東縣", "宜蘭縣",
    "花蓮縣", "臺東縣", "澎湖縣", "金門縣", "連江縣"
]
city_dropdown = ttk.Combobox(root, textvariable=city_var, values=city_list)
city_dropdown.pack(padx=20, pady=5)
city_dropdown.current(0)  # 預設為第一個選項


# 活動類型選擇
activity_label = tk.Label(root, text="活動類型：", font=("Arial", 12))
activity_label.pack(anchor="w", padx=20)
activity_var = tk.StringVar(value="室內")
activity_indoor = tk.Radiobutton(root, text="室內", variable=activity_var, value="室內")
activity_outdoor = tk.Radiobutton(root, text="戶外", variable=activity_var, value="戶外")
activity_indoor.pack(anchor="w", padx=40)
activity_outdoor.pack(anchor="w", padx=40)

# 顯示天氣資訊區域
weather_frame = tk.LabelFrame(root, text="天氣資訊", font=("Arial", 12))
weather_frame.pack(fill="both", expand="yes", padx=20, pady=10)
weather_info = {
    "天氣現象": tk.StringVar(value="未知"),
    "降雨機率": tk.StringVar(value="未知"),
    "最低溫": tk.StringVar(value="未知"),
    "舒適度": tk.StringVar(value="未知"),
    "最高溫": tk.StringVar(value="未知"),
}

for key, var in weather_info.items():
    frame = tk.Frame(weather_frame)
    frame.pack(anchor="w", pady=2)
    label = tk.Label(frame, text=f"{key}：", font=("Arial", 12))
    label.pack(side="left")
    value_label = tk.Label(frame, textvariable=var, font=("Arial", 12))
    value_label.pack(side="left")

# 穿衣建議
suggestion_label = tk.Label(root, text="建議穿著：", font=("Arial", 12))
suggestion_label.pack(anchor="w", padx=20)


# 建立一個主框架
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# 建議框架（上部）
suggestion_frame = tk.Frame(main_frame)
suggestion_frame.pack(fill=tk.BOTH, expand=True)

# 放置 ScrolledText
suggestion_display = ScrolledText(suggestion_frame, font=("Arial", 12), wrap=tk.WORD, height=10, width=40)
suggestion_display.pack(fill=tk.BOTH, expand=True)
suggestion_display.insert("1.0", "請查詢天氣後顯示建議。")
suggestion_display.config(state=tk.DISABLED)

# 按鈕框架（下部）
button_frame = tk.Frame(main_frame)
button_frame.pack(fill=tk.X)

# 提交按鈕
submit_button = tk.Button(button_frame, text="提交查詢", font=("Arial", 12), command=fetch_weather_data)
submit_button.pack(pady=10)

# 啟動主視窗
root.mainloop()
