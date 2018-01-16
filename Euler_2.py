fibonacci_sequence = [1,2]
while fibonacci_sequence[-1] + fibonacci_sequence[-2] < 4*10**6:
    fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    
sum([f for f in fibonacci_sequence if f % 2])
