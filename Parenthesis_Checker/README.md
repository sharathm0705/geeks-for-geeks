# Parenthesis Checker

## Problem Statement
Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']'. Determine whether the Expression is balanced or not.An expression is balanced if:

Each opening bracket has a corresponding closing bracket of the same type.
Opening brackets must be closed in the correct order.

## Examples
**Example 1:**
```text
Input: s = "[{()}]"
Output: true
Explanation: All the brackets are well-formed.
```

**Example 2:**
```text
Input: s = "[()()]{}"
Output: true
Explanation: All the brackets are well-formed.
```

**Example 3:**
```text
Input: s = "([]"
Output: false
Explanation: The expression is not balanced as there is a missing ')' at the end.
```

**Example 4:**
```text
Input: s = "([{]})"
Output: false
Explanation: The expression is not balanced as there is a closing ']' before the closing '}'.
```

## Constraints
```text
1 ≤ s.size() ≤ 106s[i] ∈ {'{', '}', '(', ')', '[', ']'}
```

## Source
[GeeksforGeeks Problem Link](https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1?page=1&sortBy=submissions)

## Solutions

- [Python Solution (solution.py)](./solution.py)

## Solved On
2026-08-14
