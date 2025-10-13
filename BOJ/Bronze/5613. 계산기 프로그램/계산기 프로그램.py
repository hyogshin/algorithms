total = int(input())

while True:
  operator = input()
  if operator == '=':
    break
  num = int(input())

  if operator == '+':
    total += num
  elif operator == '-':
    total -= num
  elif operator == '*':
    total *= num
  elif operator == '/':
    total //= num

print(total)