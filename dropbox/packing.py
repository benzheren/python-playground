import sys
from string import atoi

def read_input(file):
    n = atoi(file.readline())
    def read_boxes(s):
        return map(atoi, s.split())
    return map(lambda x: read_boxes(file.readline()), xrange(n))

def solve(boxes):
    sorted_boxes = sorted(boxes, key=lambda box: max(box[0], box[1]),
                          reverse=True)
     

if __name__ == "__main__":
    solve(read_input(sys.stdin))
