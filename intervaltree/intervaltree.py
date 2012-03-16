import sys

def binary_search(array, point, idx):
    lo = 0
    hi = len(array)

    while lo < hi:
        mid = (lo + hi) / 2
        midval = array[mid][idx]
        if midval < point:
            lo = mid+1
        elif midval > point:
            hi = mid
        else:
            return mid, mid

    return lo, hi

class Node(object):
    def __init__(self, midpoint, level, max_range):
        self.midpoint = midpoint
        self.level = level
        self.max_range = max_range

        self.left_tree = None
        self.right_tree = None
        self.sorted_start = []
        self.sorted_end = []

    def in_range(self, range):
        return self.midpoint >= range[0] and self.midpoint <= range[1]

    def is_smaller(self, range):
        return range[1] < self.midpoint

    def is_bigger(self, range):
        return self.midpoint < range[0]

    def get_left_tree(self):
        if not self.left_tree:
            diff = self.max_range / (2 ** self.level)
            self.left_tree = Node(self.midpoint - diff, self.level + 1, self.max_range)

        return self.left_tree

    def get_right_tree(self):
        if not self.right_tree:
            diff = self.max_range / (2 ** self.level)
            self.right_tree = Node(self.midpoint + diff, self.level + 1, self.max_range)

        return self.right_tree

    def add_range(self, range):
        self.sorted_start.append(range)
        self.sorted_end.append(range)

        self.sorted_start.sort(key=lambda x: x[0])
        self.sorted_end.sort(key=lambda x: x[1])

    def find_intersecting(self, point):
        if point == self.midpoint:
            return self.sorted_start

        if self.sorted_start and point < self.midpoint:
            lo, hi = binary_search(self.sorted_start, point, 0)
            for start in range(lo, hi + 1):
                if start < len(self.sorted_start) and self.sorted_start[start] > point:
                    break

            return self.sorted_start[:start]

        if self.sorted_end and point > self.midpoint:
            lo, hi = binary_search(self.sorted_end, point, 1)
            for end in range(lo, hi + 1):
                if end < len(self.sorted_end) and self.sorted_end[end] >= point:
                    break

            return self.sorted_end[end:]

        return []

class IntervalTree(object):
    def __init__(self, max_range):
        self.root = Node(max_range / 2, 1, max_range)
        self.max_range = max_range

    def add_range(self, range):
        node = self.root
        while not node.in_range(range):
            if node.is_smaller(range):
                node = node.get_left_tree()
            elif node.is_bigger(range):
                node = node.get_right_tree()
            else:
                print 'bad error!'
                sys.exit(1)

        node.add_range(range)

    def contains_point(self, point):
        ret = []
        node = self.root
        while node:
            ret.extend(node.find_intersecting(point))

            if point < node.midpoint:
                node = node.left_tree
            elif point > node.midpoint:
                node = node.right_tree
            else:
                node = None

        return ret

"""
def generate_point():
    import random
    
    start = int(random.random() * 10 * 1000)
    end = start + int(random.random() * 500)
    return (start, end)

tree = IntervalTree(10 * 1000 + 500)
for x in range(10):
    point = generate_point()
    print point
    tree.add_range(point)

print "Contains 5000? " + str(tree.contains_point(5000))
"""
