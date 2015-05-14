def weather():
    import pywapi
    location_id = input("Enter your zip code: ")
    weather_com_result = pywapi.get_weather_from_weather_com(location_id)
    if "error" in weather_com_result.keys():
        print(weather_com_result["error"])
    else:
        print("Weather.com says: It is ", weather_com_result["current_conditions"]["text"], " and ", ((int(weather_com_result["current_conditions"]["temperature"])*(9/5))+32), " degrees F now at ", str(int(location_id)))
weather()
