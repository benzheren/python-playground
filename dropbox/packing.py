import sys
from string import atoi

from packer import CygonRectanglePacker

def read_input(file):
    n = atoi(file.readline())
    def read_boxes(s):
        box = map(atoi, s.split())
        return (max(box[0], box[1]), min(box[0], box[1]))
    return map(lambda x: read_boxes(file.readline()), xrange(n))

def first_feasible_solution(boxes):
    '''here boxes are sorted boxes'''
    width = sum(box[1] for box in boxes)
    height = boxes[0][0]
    print 'area width %d' % width
    packer = CygonRectanglePacker(width, height)
    for box in boxes:
        print '%d %d' % (box[0], box[1])
        print 'try placement 1'
        placement1 = packer.TryPack(box[1], box[0])
        print 'try placement 2'
        placement2 = packer.TryPack(box[0], box[1])
        (placement2 and (placement1.x + box[1]) > (placement2.x + box[0])) and\
                packer.Pack(box[0], box[1]) or packer.Pack(box[1], box[0])

    return packer

def solve(boxes):
    sorted_boxes = sorted(boxes, key=lambda box: max(box[0], box[1]),
                          reverse=True)
    for box in sorted_boxes:
        print '%d %d' % (box[0], box[1])
    packer = first_feasible_solution(sorted_boxes)
    for i in packer.heightSlices:
        print '%d %d' % (i.x, i.y)

if __name__ == "__main__":
    solve(read_input(sys.stdin))
