def calculate_endurance(fuel, fuel_consumption):
    try:
        if fuel_consumption == 0:
            raise ValueError("Fuel consumption cannot be zero when the motor is idling.")
        else:
            endurance = fuel / fuel_consumption
            return endurance
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except ZeroDivisionError:
        print("Error: Division by zero (fuel consumption is zero).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

# Get fuel level input from the user
while True:
    try:
        fuel_litres = float(input("Enter the fuel level in litres: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the fuel level.")

# Example fuel consumption value (you can replace it with your actual value)
fuel_consumption_per_minute = 2.0

endurance = calculate_endurance(fuel_litres, fuel_consumption_per_minute)

if endurance is not None:
    print(f"Remaining Endurance: {endurance} minutes")
