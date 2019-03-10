
def build_dictionary(f):
    dictionary = {}
    with open(f, "r") as src:
        for line in src.readlines():
            line = line.strip().split()
            dictionary[line[0]] = int(line[1])
        return dictionary

def extract_range(d, low, high):
    new_dict = {}
    for k in d:
        if d[k] >= low and d[k] <= high:
            new_dict[k] = d[k]
    return new_dict

if __name__ == '__main__':
    main()
