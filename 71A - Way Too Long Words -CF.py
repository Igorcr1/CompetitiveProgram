n = int(input())
matriz = [] 

i=1
while(i <= n):
    palavra = input()
    if (len(palavra) > 10):
        toolong = palavra[0] + str(len(palavra[1:(len(palavra)-1)])) + palavra[len(palavra)-1]
        matriz.append(toolong)        
    else:
        matriz.append(palavra)
    i += 1

for l in matriz:
    print(l)
