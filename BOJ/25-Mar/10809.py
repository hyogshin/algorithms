from string import ascii_lowercase
alphabet_list = list(ascii_lowercase)

w = input()

ans = []

for i in range(len(alphabet_list)):
  if alphabet_list[i] not in w:
    alphabet_list[i] = -1
  else:
    alphabet_list[i] = w.index(alphabet_list[i])

answer = " ".join(str(s) for s in alphabet_list)
print(answer)
