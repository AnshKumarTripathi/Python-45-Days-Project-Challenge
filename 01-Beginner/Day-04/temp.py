# Temperature Converter Project

# Theory:
# Temperature conversion involves converting a temperature reading from one unit (Celsius, Fahrenheit, or Kelvin) to another.
# The formulas for converting between these temperature units are as follows:
# 1. Celsius to Fahrenheit: (Celsius * 9/5) + 32
# 2. Fahrenheit to Celsius: (Fahrenheit - 32) * 5/9
# 3. Celsius to Kelvin: Celsius + 273.15
# 4. Kelvin to Celsius: Kelvin - 273.15
# 5. Fahrenheit to Kelvin: (Fahrenheit - 32) * 5/9 + 273.15
# 6. Kelvin to Fahrenheit: (Kelvin - 273.15) * 9/5 + 32

# Logic:
# 1. Define functions for each conversion formula.
#    - Function for Celsius to Fahrenheit
#    - Function for Fahrenheit to Celsius
#    - Function for Celsius to Kelvin
#    - Function for Kelvin to Celsius
#    - Function for Fahrenheit to Kelvin
#    - Function for Kelvin to Fahrenheit

# 2. Create a user interface to select the input temperature unit and the target temperature unit.
#    - Prompt the user to enter the temperature value.
#    - Prompt the user to choose the input temperature unit (Celsius, Fahrenheit, Kelvin).
#    - Prompt the user to choose the target temperature unit (Celsius, Fahrenheit, Kelvin).

# 3. Based on the user's input, call the appropriate conversion function.
#    - Use conditional statements (if-elif-else) to determine which conversion function to call.

# 4. Display the converted temperature value to the user.
#    - Print the converted temperature along with the target unit.

# Example Conversion Functions:
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9

# def celsius_to_kelvin(celsius):
#     return celsius + 273.15

# def kelvin_to_celsius(kelvin):
#     return kelvin - 273.15

# def fahrenheit_to_kelvin(fahrenheit):
#     return (fahrenheit - 32) * 5/9 + 273.15

# def kelvin_to_fahrenheit(kelvin):
#     return (kelvin - 273.15) * 9/5 + 32


userTemp = int(input("Enter the number corresponding to the unit of temperature. \n 1:Celsius \n 2:Fahrenheit \n 3:Kelvin \n"))
tempValue = float(input("Enter the value of temprature: "))
changeTemp = int(input("Enter the number corresponding to the unit of temperature  you want to change to. \n 1:Celsius \n 2:Fahrenheit \n 3:Kelvin \n"))

def celsius_to_fahrenheit(celsius):
  print("Your conversion from celsius to fahrenheit is: ",(celsius * 9/5) + 32)

def fahrenheit_to_celsius(fahrenheit):
  print("Your conversion from fahrenheit to celsius is: ",(fahrenheit - 32) * 5/9)

def celsius_to_kelvin(celsius):
  print("Your converiosn from celsius to kelvin is: ",celsius + 273.15)

def kelvin_to_celsius(kelvin):
  print("Your converiosn from kelvin to celsius is: ",kelvin - 273.15)

def fahrenheit_to_kelvin(fahrenheit):
  print("Your conversion from fahrenheit to kelvin is: ",(fahrenheit - 32) * 5/9 + 273.15)

def kelvin_to_fahrenheit(kelvin):
  print("Your converison from kelvin to fahrenheit is: ",(kelvin - 273.15) * 9/5 + 32)


if(userTemp == 1):
  
  if(changeTemp == 1):
    print("Your celsius to celsius conversion is: ",tempValue)
  elif(changeTemp == 2):
    celsius_to_fahrenheit(tempValue)
  elif(changeTemp == 3):
    celsius_to_kelvin(tempValue)
  else:
    print("Bruh! choose from the option...")
    
elif(userTemp == 2):
  
  if(changeTemp == 1):
    fahrenheit_to_celsius(tempValue)
  elif(changeTemp == 2):
    print("Your fahrenheit to fahrenheit conversion is: ",tempValue)
  elif(changeTemp == 3):
    fahrenheit_to_kelvin(tempValue)
  else:
    print("Bruh! choose from the option...")
    
elif(userTemp == 3):
  
  if(changeTemp == 1):
    kelvin_to_celsius(tempValue)
  elif(changeTemp == 2):
    kelvin_to_fahrenheit
  elif(changeTemp == 3):
    print("Your kelvin to kelvin conversion is: ",tempValue)
  else:
    print("Bruh! choose from the option...")
    
else:
  print("Try choosing valid number for temperature")