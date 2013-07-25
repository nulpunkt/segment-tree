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
    
          28
       17   11
     5   13   11
    1 4 5  8 8  3
