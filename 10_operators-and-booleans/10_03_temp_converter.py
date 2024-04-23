# Fahrenheit to Celsius:
# ----------------------
# Write the necessary code to convert a degree in Fahrenheit
# to Celsius and print it to the console. Use variable names!

fahrenheit = float(input('Enter a temperature in fahrenheit to convert to celcius: '))
celcius = (fahrenheit - 32) * 5/9

print(f'{fahrenheit} degrees fahrenheit is equal to {celcius:.2f} degrees celcius')
