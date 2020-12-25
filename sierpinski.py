from follow import follow
import turtle as exturtle

def sierpinski(S):
    new_str = ""
    for char in S:
        if char == 'E':
            new_str += 'FLELF'
        elif char == 'F':
            new_str += 'ERFRE'
        else:
            new_str += char
    return new_str

axiom = 'E'
for _ in range(8):
    axiom = sierpinski(axiom)

t = exturtle.Turtle()
follow(t, axiom, step=2, angle=60)