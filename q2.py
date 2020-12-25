import random

def shuffle(L):
    for i in range(len(L) - 1, 0, -1):
        j = random.randint(0, i)
        L[i], L[j] = L[j], L[i]

def check_shuffle(shuffle):
    L = [i for i in range(1, 21)]
    to_shuffle = L[:]
    shuffle(to_shuffle)

    if len(L) != len(to_shuffle):
        return False

    shuffle_set = set(to_shuffle)
    for item in L:
        if item not in shuffle_set:
            return False

    return True

def quality(L):
    num_greater = 0
    for i in range(1, len(L)):
        if L[i] > L[i-1]:
            num_greater += 1

    return num_greater / (len(L) - 1)

def average_quality(L, num_trials):
    total = 0
    for i in range(num_trials):
        shuffle(L)
        total += quality(L)
    return total / num_trials

if __name__ == "__main__":
    L = [i for i in range(1, 21)]
    shuffle(L)
    print(L)
    print(quality(L))
    print(quality([0, 1, 2, 3, 4, 5, 6]))
    print(quality([1, 4, 2, 3, 6, 5, 0]))

    greek = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta",
    "theta", "iota", "kappa", "lambda", "mu"]
    shuffle(greek)
    print(greek)
    print(quality(greek))

    print(check_shuffle(shuffle))

    print(average_quality([i for i in range(100)], 1000))
