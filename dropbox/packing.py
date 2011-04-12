import sys
from string import atoi

from packer import CygonRectanglePacker

class Box(object):
    """docstring for Box"""
    def __init__(self, x, y):
        self.s = min(x, y)
        self.l = max(x, y)
    
    def __cmp__(self, other):
        return (self.l - other.l) and self.l - other.l or self.s - other.s 
        
def read_input(file):
    n = atoi(file.readline())
    def read_boxes(s):
        box = map(atoi, s.split())
        return Box(box[0], box[1])
    return map(lambda x: read_boxes(file.readline()), xrange(n))

def first_feasible_solution(boxes):
    '''here boxes are sorted boxes'''
    width = sum(box.s for box in boxes)
    height = boxes[0].l
    print 'area width %d' % width
    packer = CygonRectanglePacker(width, height)
    for box in boxes:
        print '%d %d' % (box.s, box.l)
        print 'try placement 1'
        placement1 = packer.TryPack(box.s, box.l)
        print 'try placement 2'
        placement2 = packer.TryPack(box.l, box.s)
        (placement2 and (placement1.x + box.s) > (placement2.x + box.l)) and\
                packer.Pack(box.l, box.s) or packer.Pack(box.s, box.l)

    return packer

def solve(boxes):
    boxes.sort(reverse=True)
    for box in boxes:
        print '%d %d' % (box.s, box.l)
    packer = first_feasible_solution(boxes)
    for i in packer.heightSlices:
        print '%d %d' % (i.x, i.y)

if __name__ == "__main__":
    solve(read_input(sys.stdin))
