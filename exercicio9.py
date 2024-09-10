def fibonacci_sequence(n):
    vetor = [0,1]
    while(len(vetor)<n):
        index = len(vetor)-1
        sub = index -1
        vetor.append(vetor[index]+vetor[sub])
    return vetor        

print(fibonacci_sequence(7))
