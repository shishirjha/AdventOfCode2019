# Playground
l = []

with open('input.txt') as inp:
  for i in inp:
    l.append(int(i))
solution = 0
for i in l:
  while (i//3)-2 >= 0:
    i = i//3
    i-=2
    solution+=i
print(solution)