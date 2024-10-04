FAHRENHEIHT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
CELSIUS_FREEZING_POINT = 32

def convert_to_celsius(fahrenheit):
    global FAHRENHEIHT_TO_CELSIUS_FACTOR
    return (fahrenheit - CELSIUS_FREEZING_POINT) * FAHRENHEIHT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + CELSIUS_FREEZING_POINT

def main():
    try:

        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    unit = input("Is this temperature in celsius or Fahrenhait? (C/F): ").strip().upper()

    if unit == 'F':
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}0F is {celsius}0C")
    elif unit == 'C':
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}0C is {fahrenheit}0F")
    else:
        print("Invalid unit. Please enter 'C' for celsius or 'F' for Fahrenheit.")


if __name__ == "__name__":
    main()