weight = int(input("What's your weight?: "))
conversion = str(input("(K)g's or (L)bs?: "))
conversion.upper()

if conversion.upper() == "K":
  print(weight * 2.205)
elif conversion.upper() == "L":
   print(weight // 2.205)