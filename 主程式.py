#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def process_weather_data(weather_data, activity_type):
    """
    處理天氣數據並生成穿衣建議。
    
    Args:
        weather_data (dict): 包含天氣狀態、氣溫、降雨機率、紫外線等信息的字典。
        activity_type (str): 活動類型，例如 "室內" 或 "戶外"。
    
    Returns:
        str: 穿衣建議。
    """
    # 提取必要資訊
    weather_status = weather_data.get("天氣狀態", "未知")
    temperature = weather_data.get("氣溫", "未知")
    rain_prob = weather_data.get("降雨機率", "0%")
    uv_index = weather_data.get("紫外線", "未知")
    
    try:
        temp_value = int(temperature[:-2])  # 移除 "°C" 並轉換為整數
        rain_value = int(rain_prob[:-1])   # 移除 "%" 並轉換為整數
    except ValueError:
        return "天氣數據處理出錯，請檢查數據來源。"

    # 根據數據生成建議
    suggestions = []

    # 溫度建議
    if temp_value < 15:
        suggestions.append("建議穿著厚外套，注意保暖。")
    elif 15 <= temp_value <= 20:
        suggestions.append("建議穿著輕便外套或毛衣。")
    elif temp_value > 20:
        suggestions.append("薄長袖或短袖即可。")

    # 降雨機率建議
    if rain_value > 50:
        suggestions.append("降雨機率較高，請攜帶雨具。")
    elif rain_value > 20:
        suggestions.append("可能有小雨，建議攜帶輕便雨具。")

    # 紫外線建議
    if uv_index == "高":
        suggestions.append("紫外線強，請攜帶防曬用品並佩戴遮陽帽。")
    elif uv_index == "中等":
        suggestions.append("建議塗抹防曬霜，避免長時間曝曬。")

    # 活動類型建議
    if activity_type == "戶外":
        suggestions.append("戶外活動建議準備充足的水分。")
    elif activity_type == "室內":
        suggestions.append("室內活動建議選擇舒適的衣物。")

    # 整合建議
    return " ".join(suggestions)

# 示例測試
if __name__ == "__main__":
    # 假設從 API 獲取的數據
    example_weather_data = {
        "天氣狀態": "晴天",
        "氣溫": "25°C",
        "降雨機率": "30%",
        "紫外線": "中等"
    }
    example_activity_type = "戶外"

    # 處理數據並生成建議
    suggestion = process_weather_data(example_weather_data, example_activity_type)
    print(f"穿衣建議：{suggestion}")

