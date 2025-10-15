def clothing_advice(temp, weather):   # Function decides clothes based on temp + weather
    weather = weather.lower()        
    if temp < 10 and "rain" in weather:
        return "Wear a coat and bring an umbrella."
    elif temp < 20:
        return "A light jacket should be fine."
    else:
        return "T-shirt weather!"

print(clothing_advice(8, "Rain"))     # Call the function with arguments
print(clothing_advice(15, "Cloudy"))
print(clothing_advice(25, "Sunny"))



# strings + logic based on text + numbers
