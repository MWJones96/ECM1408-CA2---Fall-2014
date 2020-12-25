from follow import follow
import turtle as exturtle

def dragon(S):
    new_str = ""
    for char in S:
        if char == 'A':
            new_str += 'ARBF'
        elif char == 'B':
            new_str += 'FALB'
        else:
            new_str += char
    return new_str

axiom = 'FA'
for _ in range(12):
    axiom = dragon(axiom)

t = exturtle.Turtle()
follow(t, axiom)