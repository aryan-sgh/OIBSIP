city = input("Enter city name: ")

temperature = float(input("Enter temperature (°C): "))
humidity = int(input("Enter humidity (%): "))

print("\nWeather Report")
print("City:", city)
print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")

if temperature > 35:
    print("Condition: Very Hot")
elif temperature > 25:
    print("Condition: Warm")
elif temperature > 15:
    print("Condition: Pleasant")
else:
    print("Condition: Cold")
