n = int(input())
soma = 0

i=1
while(i <= n):
  s = list(input())
  if(s.count('1') >= 2):
    soma += 1
  i += 1

print(soma)
