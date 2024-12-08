def provide_comprehensive_clothing_recommendation(temp, rain_probability, wind_speed, uv_index):
    # 初始化穿搭建議
    head_recommendation = ""
    top_recommendation = ""
    bottom_recommendation = ""
    shoes_recommendation = ""
    accessory_recommendation = "無建議。"
    additional_recommendation = ""

    # 根據溫度和紫外線指數決定頭部穿戴
    if uv_index >= 8:
        head_recommendation = "戴太陽帽或輕便的帽子以遮陽和防曬。"
    elif temp >= 30:
        head_recommendation = "戴輕便的帽子以遮陽。"
    elif 20 <= temp < 30:
        head_recommendation = "戴帽子防曬。"
    elif 10 <= temp < 20:
        head_recommendation = "可以戴輕便的帽子或耳罩保暖。"
    elif 0 <= temp < 10:
        head_recommendation = "戴毛帽或圍巾保暖。"
    else:
        head_recommendation = "戴厚重的帽子和圍巾保暖。"

    # 根據溫度決定基本穿搭
    if temp >= 30:
        top_recommendation = "短袖T恤。"
        bottom_recommendation = "短褲。"
        shoes_recommendation = "穿透氣的涼鞋或輕便鞋。"
    elif 20 <= temp < 30:
        top_recommendation = "T恤。"
        bottom_recommendation = "牛仔褲或洋裝。"
        shoes_recommendation = "穿輕便運動鞋或休閒鞋。"
    elif 10 <= temp < 20:
        top_recommendation = "夾克或毛衣。"
        bottom_recommendation = "長褲。"
        shoes_recommendation = "穿保暖的運動鞋或短靴。"
    elif 0 <= temp < 10:
        top_recommendation = "大衣和圍巾。"
        bottom_recommendation = "厚長褲。"
        shoes_recommendation = "穿防水的保暖靴。"
        accessory_recommendation = "戴手套以保暖。"
    else:
        top_recommendation = "厚重的大衣。"
        bottom_recommendation = "保暖長褲。"
        shoes_recommendation = "穿雪地靴或保暖靴。"
        accessory_recommendation = "戴手套和圍巾以保暖。"

    # 根據風速添加防風建議
    if wind_speed > 20:
        additional_recommendation += "風速較大，建議穿防風外套以減少風寒效應。"

    # 根據降雨率添加防水建議
    if rain_probability > 50:
        additional_recommendation += " 降雨機率較高，建議攜帶雨傘或雨衣，並選擇防水鞋款。"

    # 根據紫外線指數添加防曬與配件建議
    if uv_index >= 11:
        additional_recommendation += " 紫外線極強，建議使用高強度防曬霜 SPF 50+，穿透氣防曬衣，佩戴太陽眼鏡。"
        accessory_recommendation = "建議佩戴太陽眼鏡。"
    elif 8 <= uv_index < 11:
        additional_recommendation += " 紫外線非常強，建議使用防曬霜 SPF 50，穿透氣防曬衣並佩戴帽子。"
        accessory_recommendation = "建議佩戴太陽眼鏡。"
    elif 6 <= uv_index < 8:
        additional_recommendation += " 紫外線較強，建議使用防曬霜 SPF 30，並注意適度遮陽。"
    elif 3 <= uv_index < 6:
        additional_recommendation += " 紫外線中等，建議使用防曬霜 SPF 15。"

    # 結合所有建議
    return (f"頭部建議：{head_recommendation}\n"
            f"上衣建議：{top_recommendation}\n"
            f"下身建議：{bottom_recommendation}\n"
            f"鞋子建議：{shoes_recommendation}\n"
            f"配件建議：{accessory_recommendation}\n"
            f"其他建議：{additional_recommendation}")

def provide_color_recommendation(temp, rain_probability, uv_index):
    # 初始化顏色建議
    color_recommendation = ""

    # 根據溫度提供顏色建議
    if temp >= 30:
        color_recommendation = "建議選擇淺色（如白色、米色），減少吸熱效果。"
    elif 20 <= temp < 30:
        color_recommendation = "建議選擇中性色調（如灰色、卡其色），保持舒適耐看。"
    elif 10 <= temp < 20:
        color_recommendation = "建議選擇暖色調（如深棕色、橄欖綠），增加視覺暖意。"
    elif temp < 10:
        color_recommendation = "建議選擇深色（如黑色、深藍色），吸熱且保暖。"

    # 根據降雨機率添加建議
    if rain_probability > 50:
        color_recommendation += " 同時建議選擇深色衣物，避免雨水濕透後透光。"

    # 根據紫外線指數添加建議
    if uv_index >= 8:
        color_recommendation += " 由於紫外線強，建議選擇淺色和密織布料的衣物，提升防曬效果。"

    return color_recommendation

def main():
    
    clothing_recommendation = provide_comprehensive_clothing_recommendation(temp, rain_probability, wind_speed, uv_index)
    color_recommendation = provide_color_recommendation(temp, rain_probability, uv_index)

    print("穿搭建議：")
    print(clothing_recommendation)
    print("\n顏色建議：")
    print(color_recommendation)

if __name__ == "__main__":
    main()
