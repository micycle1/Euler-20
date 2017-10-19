sequence = []
for a in range(2,101):
    for b in range(2,101):
        if not a ** b in sequence:
            sequence.append(a ** b)

print(len(sequence))
        
