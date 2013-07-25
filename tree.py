class SegmentTree(object):
    """Naiv implementation of a segment tree"""
    def __init__(self, points):
        self._points = points
        self._tree = self._construct()

    def sum(self, start, end):
        range = Range(start, end)
        return self._tree.get_sum(range)

    def set(self, index, value):
        range = Range(index, index)
        delta = value - self._points[index]
        self._tree.applyDeltaToRange(delta, range)

    def _construct(self):
        return self._construct_node(Range(0, len(self._points)-1))

    def _construct_node(self, range):
        if range.size() < 1:
            return Node.leaf(range, range.sum(self._points))
        else:
            return self._construct_internal_node(range)

    def _construct_internal_node(self, range):
        left_range, right_range = range.split()

        left_node = self._construct_node(left_range)
        right_node = self._construct_node(right_range)

        return Node.internal(left_node, right_node)

class Node(object):
    def __init__(self, range, sum):
        self._range = range
        self._sum = sum
    
    @staticmethod
    def leaf(range, sum):
        return Leaf(range, sum)

    @staticmethod
    def internal(left, right):
        return Internal(left, right)

    def get_range(self):
        return self._range

class Leaf(Node):
    def __init__(self, range, sum):
        Node.__init__(self, range, sum)
        
    def applyDeltaToRange(self, delta, range):
        self._sum = self._sum + delta

    def get_sum(self, range):
        if range.contains(self._range):
            return self._sum
        else:
            return 0

class Internal(Node):
    def __init__(self, left, right):
        range = left.get_range().merge(right.get_range())
        sum = left._sum+right._sum

        Node.__init__(self, range, sum)
        self._set_children(left, right)
    
    def _set_children(self, left, right):
        self._left = left    
        self._right = right
    
    def get_sum(self, range):
        if range.contains(self._range):
            return self._sum
        elif self._range.partially_contains(range):
            return self._left.get_sum(range) + self._right.get_sum(range)
        else:
            return 0
    
    def applyDeltaToRange(self, delta, range):
        self._sum = self._sum + delta
        self.applyDeltaRecursivly(delta, range)

    def applyDeltaRecursivly(self, delta, range):
        if self._left._range.contains(range):
            self._left.applyDeltaToRange(delta, range)
        else:
            self._right.applyDeltaToRange(delta, range)
        
class Range(object):
    def __init__(self, start, end):
        self._start = start
        self._end = end
        
    def size(self):
        return self._end-self._start

    def split(self):
        pivot = self.center()
        left = Range(self._start, pivot)
        right = Range(pivot+1, self._end)
        return left, right

    def center(self):
        return ((self._end-self._start)/2)+self._start

    def sum(self, list):
        return sum(list[self._start:(self._end+1)])

    def merge(self, other):
        start = min(self._start, other._start)
        end = max(self._end, other._end)
        return Range(start, end)

    def contains(self, other):
        return self._start <= other._start and self._end >= other._end 

    def partially_contains(self, other):
        return self._start <= other._start or self._end >= other._end 

    def __repr__(self):
        return str((self._start, self._end))

    def __eq__(self, other):
        return self._start == other._start and self._end == other._end
