from priority_queue_112 import PQ
import sys

def main():

    m = int(sys.argv[1])
    pq = PQ()
    i = 0
    for line in sys.stdin:
        if m < pq.size():
            pq.delMax()
        pq.insert(int(line.strip()))
        i += 1

    print(pq.d[3])
    print(pq.d[2])
    print(pq.d[6])
    print(pq.d[5])
    print(pq.d[4])


if __name__ == '__main__':
    main()
