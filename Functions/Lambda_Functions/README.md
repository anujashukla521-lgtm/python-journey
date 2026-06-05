# Lambda Functions – Python Practice

## Overview

This section of my Python learning repository focuses on **Lambda Functions**, a powerful concept used to create small anonymous functions in Python.

The goal of this practice is to understand how lambda functions work, how they differ from normal functions, and how they can be used for simple operations in a concise way.

---

## Topics Covered

* Introduction to Lambda Functions
* Syntax of Lambda Functions
* Single-expression functions
* Conditional expressions in lambda
* Difference between `def` functions and lambda functions
* Limitations of lambda functions (single expression only)

---

## Key Concepts

### 1. Basic Lambda Function

```python
square = lambda x: x * x
```

### 2. Lambda with Multiple Arguments

```python
add = lambda a, b: a + b
```

### 3. Lambda with Condition

```python
greater = lambda a, b: a if a > b else b
```

---

## Key Learnings

* Lambda functions are used for **short and simple operations**.
* They are **anonymous functions** (no function name required).
* They can only contain **one expression**.
* They improve code conciseness but reduce readability for complex logic.
* Best used when functions are required temporarily or inline.

---

## Limitations

* Cannot contain multiple statements
* Not suitable for complex logic
* Harder to debug compared to normal functions

---

## Conclusion

This practice helped me understand how lambda functions simplify small operations in Python and where they are most effectively used. This is a stepping stone before learning higher-order functions like `map()`, `filter()`, and `reduce()`.

---

## Next Step

* Learn `map()` function
* Learn `filter()` function
* Learn `reduce()` function
* Apply lambda with these functions in real examples
