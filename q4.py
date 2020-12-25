def algae(S):
    new_str = ''
    for char in S:
        if char == 'A':
            new_str += 'AB'
        elif char == 'B':
            new_str += 'A'
    return new_str

if __name__ == "__main__":
    axiom = 'A'
    for _ in range(30+1):
        print(len(axiom))
        axiom = algae(axiom)