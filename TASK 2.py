
choice = input("Convert C to F or F to C? ")

temperature = float(input("Enter temperature: "))

if choice == "C":
    result = temperature * 1.8 + 32
    print(temperature, "°C =", result, "°F")

elif choice == "F":
    result = (temperature - 32) / 1.8
    print(temperature, "°F =", result, "°C")

else:
    print("Invalid choice!")
