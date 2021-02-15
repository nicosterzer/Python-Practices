# Conversor from both Lbs and Kgs.
weight = int(input("What's your weight?: "))
conversion = str(input("(K)g's or (L)bs?: "))

# Converts the inserted letter to uppercase.
conversion.upper()

# Conditional statement used to convert measurement units.
if conversion.upper() == "K":
  print(weight * 2.205)
elif conversion.upper() == "L":
   print(weight // 2.205)