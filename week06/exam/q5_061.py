import sys

scores = {}

def names(a):
    i = 0
    while i < len(a):
        if a[i].isalpha():
            i += 1
        else:
            break
    scores[" ".join(a[:i])] = score(a[i:])

def score(a):
    total = 0
    for n in a:
        total += int(n)
    return str(total)

def sorter(t):
    return int(t[1])

def main():
    for line in sys.stdin:
        line = line.strip().split()
        names(line)

    name_width = len(max(scores.keys(), key=len))
    num_width = len(max(scores.values(), key=len))
    for k, v in sorted(scores.items(), key=sorter):
        print("{:>{}s}: {:>{}s}".format(k, name_width, v, num_width))

if __name__ == '__main__':
    main()
