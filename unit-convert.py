num1 = input('Enter the value: ')
print("Your unit should be Metre --> m, Yard --> yd, Inch --> in, Feet --> ft, Kilometre --> km ")
unit1 = input('Which unit do you want it converted from:  ')
unit2 = input('Which unit do you want it converted to: ')

if unit1 == "m" and unit2 == "yd":
    ans = float(num1) * 1.093613
    print(ans)
elif unit1 == "m" and unit2 == "in":
    ans = float(num1) * 39.3701
    print(ans)
elif unit1 == "m" and unit2 == "km":
    ans = float(num1) / 1000
    print(ans)
elif unit1 == "m" and unit2 == "ft":
    ans = float(num1) / .3048
    print(ans)
elif unit1 == "yd" and unit2 == "m":
    ans = float(num1) / 1.093613
    print(ans)
elif unit1 == "yd" and unit2 == "in":
    ans = float(num1) * 36.0000
    print(ans)
elif unit1 == "yd" and unit2 == "km":
    ans = float(num1) * 0.0009
    print(ans)
elif unit1 == "yd" and unit2 == "ft":
    ans = float(num1) * 3.0000
    print(ans)
elif unit1 == "in" and unit2 == "m":
    ans = float(num1) / 39.3701
    print(ans)
elif unit1 == "in" and unit2 == "yd":
    ans = float(num1) / 36.0000
    print(ans)
elif unit1 == "in" and unit2 == "ft":
    ans = float(num1) / 12
    print(ans)
elif unit1 == "in" and unit2 == "km":
    ans = float(num1) * 2.5400
    print(ans)
elif unit1 == "ft" and unit2 == "m":
    ans = float(num1) * .3048
    print(ans)
elif unit1 == "ft" and unit2 == "in":
    ans = float(num1) * 12
    print(ans)
elif unit1 == "ft" and unit2 == "yd":
    ans = float(num1) / 3.0000
    print(ans)
elif unit1 == "ft" and unit2 == "km":
    ans = float(num1) * 0.0003
    print(ans)
elif unit1 == "km" and unit2 == "yd":
    ans = float(num1) / 0.0009
    print(ans)
elif unit1 == "km" and unit2 == "m":
    ans = float(num1) * 1000
    print(ans)
elif unit1 == "km" and unit2 == "in":
    ans = float(num1) * 39370.0999
    print(ans)
elif unit1 == "km" and unit2 == "ft":
    ans = float(num1) * 3280.8416
    print(ans)
else:
    print("Invalid input. You should input m, yd, in, km, ft")
