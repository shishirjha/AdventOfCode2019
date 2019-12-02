l = []

with open('input.txt') as inp:
  for i in inp:
    l.append(int(i))
solution = 0
for i in l:
  num = i//3
  num-=2
  solution+=num
print(solution)
