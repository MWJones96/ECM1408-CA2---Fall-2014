import re
import sys

def histogram(x, percentage, resolution=1):
    for (num, index) in enumerate(x):
        hist_line = str(num)
        hist_line += ' '
        hist_line += '*' * int(percentage[index] / resolution)
        hist_line += ' ' * 5
        hist_line += str(round(percentage[index], 5))

        print(hist_line)

def histogram_lengths(L):
    max_length = len(max(L, key=lambda x: len(x)))
    lengths = [0] * (max_length + 1)
    for word in L:
        lengths[len(word)] += 1
    return lengths

def draw_histogram(words, resolution=1):
    H = histogram_lengths(words)
    total_words = sum(H)
    percentages = [(x / total_words) * 100 for x in H]
    histogram(range(len(percentages)), percentages, resolution)

if __name__ == "__main__":
    file_name = sys.argv[1]
    with open(file_name) as f:
        words = re.sub(r'[^A-Za-z]', ' ', f.read().lower()).split()
        draw_histogram(words, resolution=0.25)