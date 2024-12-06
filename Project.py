def celcius_to_farenhite(C):
  F = (C * 9/5) + 32
  F = int(F)
  return print(f"{C}°C Celcius is Equal to  {F}°F Farenhite ")

def farenhite_to_celcius(F):
  C = (F - 32) * 5/9
  C = int(C)
  return print(f"{F}°F Farenhite is Equal to  {C}°C Celcius")


print("\033[1m Fahrenheit \u21CC Celsius \033[0m")
print("-----------------------\n")

print("Select the option Below ")
print("1 : For Celcius to Farenhite ")
print("2 : For Farenhite to Celcius ")

def main():
  try:
    choice : int = int(input("Enter your  Choice : "))
  except ValueError:
    print("Invalid Input")
  try:
    user_value = int(input("Enter your Temperature to Convert  : "))
  except ValueError:
    print("Invalid Temperature .. ")

  if choice == 1:
    celcius_to_farenhite(user_value)
  elif choice == 2:
    farenhite_to_celcius(user_value)
  else:
    print("Invalid Choice .")



if __name__ == '__main__':
  main()