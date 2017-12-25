from copy import deepcopy
from sys import maxint
from Tree.segment_tree.base_segment_tree import SegmentTree

class SumRangeSegmentTree(SegmentTree):

    def __init__(self, input_arr):
        super(SumRangeSegmentTree, self).__init__(input_arr)

    def _build_tree_util_(self, low, high, pos):
        if low == high:
            self.seg_tree_arr[pos] = self.input_arr[low]
            return
        mid = (low + high)/2
        self._build_tree_util_(low, mid, 2*pos + 1)
        self._build_tree_util_(mid + 1, high, 2*pos + 2)
        self.seg_tree_arr[pos] = self.seg_tree_arr[2*pos + 1] + self.seg_tree_arr[2*pos + 2]

    def build_tree(self):
        self._build_tree_util_(0, len(self.input_arr)-1, 0)
        return deepcopy(self.seg_tree_arr)

    def _range_sum_query_(self, qs, qe, low, high, pos):
        # Complete overlap, query range (qs, qe) is completely overlapping (low, high). e.g. (0, 4) (1, 3)
        # return current value i.e. at index `pos`
        if qs <= low and qe >= high:
            return self.seg_tree_arr[pos]

        # No overlap, query range (qs, qe) is not overlapping (low, high). e.g. (3, 4) (0, 2)
        # Return 0
        elif qs > high or qe < low:
            return 0

        # Partial overlap, query range (qs, qe) is partially overlapping (low, high). e.g. (3, 5) (1, 3)
        # Go recursively in left & right subtree.
        else:
            mid = (low + high)/2
            return (self._range_sum_query_(qs, qe, low, mid, 2*pos + 1)
                   + self._range_sum_query_(qs, qe, mid+1, high, 2*pos + 2))

    def range_sum_query(self, qs, qe):
        range_sum = self._range_sum_query_(qs, qe, 0, len(self.input_arr)-1, 0)
        return range_sum

    def _update_value_(self, i, diff, low, high, pos):
        # If the input index `i` lies outside the range of this segment (low, high),
        # return
        if i < low or i > high:
            return

        # Leaf node: low and high are same,
        # update it's value.
        if low == high:
            if low == i:  # or high == i, as low & high are same
                self.seg_tree_arr[pos] += diff

        # If the input index `i` lies under the range of this segment (low, high), i.e.
        # low <= i && i <= high && low != high
        else:
            mid = (low + high) / 2
            self._update_value_(i, diff, low, mid, 2 * pos + 1)
            self._update_value_(i, diff, mid + 1, high, 2 * pos + 2)
            self.seg_tree_arr[pos] = self.seg_tree_arr[2 * pos + 1] + self.seg_tree_arr[2 * pos + 2]

    def updated_value(self, i, diff):
        self._update_value_(i, diff, 0, len(self.input_arr) - 1, 0)
        return deepcopy(self.seg_tree_arr)

if __name__ == '__main__':
    input_arr = [1, 4, -1, 0]
    seg_tree_obj = SumRangeSegmentTree(input_arr)
    seg_tree_arr = seg_tree_obj.build_tree()

    print "\n---------- Before modification ----------\n"
    print "Sum-Range-Segment tree is:", seg_tree_arr

    qs = 0; qe = 2
    range_sum = seg_tree_obj.range_sum_query(qs, qe)
    print "Sum of elements in range ({}, {}) is {}".format(qs, qe, range_sum)

    modify_index = 2; diff = 3
    print "\n---------- After modification (Adding {} at index {}) ----------\n".format(diff, modify_index)
    seg_tree_arr_modified = seg_tree_obj.updated_value(modify_index, diff)
    print "Sum-Range-Segment tree is:", seg_tree_arr_modified
    qs = 0; qe = 2
    min_elt = seg_tree_obj.range_sum_query(qs, qe)
    print "Sum of elements in range ({}, {}) is {}".format(qs, qe, min_elt)