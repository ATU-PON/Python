# List of 10 temperatures in Fahrenheit
temperatures_fahrenheit = [72, 65, 80, 90, 60, 75, 68, 85, 95, 70]

# Function to convert Fahrenheit to Celsius and Kelvin
def convert_temperature(temperature_fahrenheit):
    # Convert Fahrenheit to Celsius
    temperature_celsius = (temperature_fahrenheit - 32) * 5/9

    # Convert Celsius to Kelvin
    temperature_kelvin = temperature_celsius + 273.15

    return temperature_celsius, temperature_kelvin

# Convert and print the temperatures
for temp_fahrenheit in temperatures_fahrenheit:
    temp_celsius, temp_kelvin = convert_temperature(temp_fahrenheit)
    print(f'{temp_fahrenheit}°F is {temp_celsius:.2f}°C and {temp_kelvin:.2f}K')
