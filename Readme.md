# Two Sum Problem

## Problem Statement

Given an array of integers `nums` and a target integer `target`, return the indices of the two numbers that add up to `target`.

## Example

```text
nums = [2, 7, 11, 15]
target = 9
```

Here:

- `2 + 7 = 9`

So the answer is:

```text
[0, 1]
```

## Simple Idea

Try each pair of numbers and check if their sum is equal to the target.

## Time Complexity

- `O(n^2)` in the simple approach

## Space Complexity

- `O(1)`

## Note

A faster solution can use a hash map and solve this in `O(n)` time.