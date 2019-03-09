import sys
import math

def table(inp, width):
    for k in inp:
            pos, *club, p, w, d, l, gf, ga, gd, pts, =  k.split()
            club = " ".join(club)
            print('{:>3s} {:<{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format(pos, club, width, p, w, d, l, gf, ga, gd, pts))

def main():
    inp = sys.stdin.readlines()
    width = 0
    for line in inp:
        club_name = line.split()
        club_name = " ".join(club_name[1:-8])
        if len(club_name) > width:
            width = len(club_name)
    print('{:>3s} {:<{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format("POS", "CLUB", width, "P", "W", "D", "L", "GF", "GA", "GD", "PTS"))
    return table(inp, width)


if __name__ == '__main__':
    main()
