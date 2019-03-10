import sys

def peak(a):
    index = []
    for i in range(1, len(a) - 1):
        if int(a[i]) > int(a[i - 1]) and int(a[i]) > int(a[i + 1]):
            index.append(i)
    return index

def main():
    for line in sys.stdin:
        line = line.strip().split()
        print(peak(line))


if __name__ == '__main__':
    main()
