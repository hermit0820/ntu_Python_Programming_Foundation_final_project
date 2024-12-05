import tkinter as tk
from tkinter import ttk

# 初始化主視窗
root = tk.Tk()
root.title("天氣穿衣建議")
root.geometry("400x500")

# 標題
title_label = tk.Label(root, text="天氣穿衣建議", font=("Arial", 20))
title_label.pack(pady=10)

# 城市選擇
city_label = tk.Label(root, text="城市選擇：", font=("Arial", 12))
city_label.pack(anchor="w", padx=20)
city_var = tk.StringVar()
city_list = [
    "台北市", "新北市", "基隆市", "桃園市", "新竹市", "新竹縣",
    "苗栗縣", "台中市", "彰化縣", "南投縣", "雲林縣", "嘉義市",
    "嘉義縣", "台南市", "高雄市", "屏東縣", "宜蘭縣", "花蓮縣",
    "台東縣", "澎湖縣", "金門縣", "連江縣"
    
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
    "天氣狀態": tk.StringVar(value="未知"),
    "氣溫": tk.StringVar(value="未知"),
    "降雨機率": tk.StringVar(value="未知"),
    "濕度": tk.StringVar(value="未知"),
    "紫外線": tk.StringVar(value="未知"),
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
suggestion_var = tk.StringVar(value="請查詢天氣後顯示建議。")
suggestion_display = tk.Label(root, textvariable=suggestion_var, font=("Arial", 12), wraplength=350, justify="left")
suggestion_display.pack(padx=20, pady=5)

# 提交按鈕
def fetch_weather_data():
    # 模擬 API 回應數據
    weather_data = {
        "天氣狀態": "晴天",
        "氣溫": "25°C",
        "降雨機率": "10%",
        "濕度": "65%",
        "紫外線": "中等"
    }
    # 更新介面數據
    for key, value in weather_data.items():
        weather_info[key].set(value)
    # 根據數據提供建議
    if int(weather_data["氣溫"][:-2]) > 20:
        suggestion_var.set("薄長袖，建議攜帶太陽眼鏡。")
    else:
        suggestion_var.set("建議穿著外套，並攜帶雨具。")

submit_button = tk.Button(root, text="提交查詢", font=("Arial", 12), command=fetch_weather_data)
submit_button.pack(pady=20)

# 啟動主視窗
root.mainloop()
