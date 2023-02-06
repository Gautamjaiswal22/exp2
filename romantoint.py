roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
roman1 = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
print(roman1.values())
print(type(roman1.values()))
a = tuple(roman1.values())
print(a)
s = input("enter roman : ")
print(s[-len(s):-(len(s)+1)])
for i in range(1, len(s)+1):
    print(-i, s[-i:-(i+1)])
