import sys

def main():
    word = list(sys.argv[1].strip())

    for i in range(1, len(word), 2):
        word[i - 1], word[i] = word[i], word[i - 1]

    print("".join(word))

if __name__ == '__main__':
    main()
