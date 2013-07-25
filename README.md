# Segment Tree

## Problem
Given an array `a[0..n-1]` we want to:

* find the sum of all elements between `s` and `e`.
* change the value of a given element, such that `a[i] = x`

We could just sum all numbers `sum(a[s..e])` on every request. This would leave us
with `O(n)` for queries and `O(1)` for inserts.

An other option would be to calculate the sum `sum(a[i..n-1])` for all `i`. This
would yield `O(1)` for queries and `O(1)` for updates.

What if, however, we have an equal amount of queries and updates?

## Data structure
* Every leaf in the tree coreponds to an element `a[i]`
* Every internal node contains the sum of its children and the range of `a` it covers
<pre>      28
       17   11
     5   13   11
    1 4 5  8 8  3
</pre>

### Query
Consider the tree above. Say we want to sum `s = 1, e = 3`.

* first query the root, are we in that interval, we are
* now query both nodes in the second level in the tree. The right node will return `0` and the left will tell us to go on
* the node with value 13 in thrid level, will simply return 13, as it is completly contained in the query interval, the left node will tell us to keep looking
* the leaf will value 4 will return 4
* and so we end up with `13+4 = 17`, as expected

### Update
Say, we want to update element `i` to the value `x`. We retrieve the element `i` (in `O(1)`, we have the array), and calculate the delta `x-a[i]`, which we apply to all nodes which are a parent to `i`.

### Time complexity
Both query and update is `O(log n)`. The proof is left as an exercise for the reader :)

## Further reading
[Segment Trees on Wikipedia](http://en.wikipedia.org/wiki/Segment_tree)
