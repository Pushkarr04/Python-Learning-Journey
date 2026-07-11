number=int(input("Enter a positive number : "))
square=number**2
cube=number**3
double=number*2
half=number/2
integer_division_by2=number//2
remainder_by2=number%2
remainder_by5=number%5

print("="*30)
print("    NUMBER ANALYSIS TOOL")
print("="*30)
print(f"\nEntered number : {number}\n")
print(f"Square  : {square}")
print(f"cube    : {cube}")
print(f"Double  : {double}")
print(f"Half    : {half:.2f}")

print(f"\nInteger divison by 2 : {integer_division_by2}")
print(f"Remainder with 2     : {remainder_by2}")
print(f"remainder with 5     : {remainder_by5}")

print("="*30)
