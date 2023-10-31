weight = None
fnum = 0.45

while not weight or weight < 1:
    weight = int(input("Weight: "))

unit = input("Convert to (L)bs or (K)g: ").upper()
while unit != 'L' and unit != 'K':
    print("Invalid input. Please enter 'L' or 'K'.")
    unit = input("Convert to (L)bs or (K)g: ").upper()

if unit == 'L':
    unit_weight = weight / fnum
else:
    unit_weight = weight * fnum

if not unit_weight.is_integer():
    unit_weight = "{:.2f}".format(unit_weight)
else:
    unit_weight = int(unit_weight)

if unit == 'L':
    print(f"Converted weight: {unit_weight}Lbs")
else:
    print(f"Converted weight: {unit_weight}Kg")
