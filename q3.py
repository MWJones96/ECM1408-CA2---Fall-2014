import random

from q2 import shuffle
from q1 import histogram

def many_plays(N):
    L = [0] * 53

    for i in range(N):
        deck = [i for i in range(1, 14)] * 4
        shuffle(deck)
        L[play(deck)] += 1

    percentages = [(x / N) * 100 for x in L]
    histogram(range(len(L)), percentages, resolution=0.25)

def play(deck, verbose=False):
    visible = []
    visible.append(deck.pop(0))
    visible.append(deck.pop(0))

    while len(deck) > 0:
        first = add_to_11(visible)
        second = jqk(visible)
        if len(first) == 2 and len(deck) >= 2:
            visible[first[0]] = deck.pop(0)
            visible[first[1]] = deck.pop(0)
        elif len(second) == 3 and len(deck) >= 3:
            visible[second[0]] = deck.pop(0)
            visible[second[1]] = deck.pop(0)
            visible[second[2]] = deck.pop(0)
        elif len(deck) > 0:
            if len(visible) == 9:
                break
            else:
                visible.append(deck.pop(0))

        if verbose:
            print(' '.join([str(i) for i in visible]))

    return len(deck)

def add_to_11(visible):
    seen = {}
    for (index, v) in enumerate(visible):
        seen[v] = index

    for v in seen:
        if 11 - v in seen:
            return (seen[v], seen[11-v])

    return ()

def jqk(visible):
    seen = {}
    for (index, v) in enumerate(visible):
        seen[v] = index
    return (seen[11], seen[12], seen[13]) \
        if 11 in seen and 12 in seen and 13 in seen \
        else ()

if __name__ == "__main__":
    many_plays(100000)