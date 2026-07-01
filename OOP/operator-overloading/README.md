# Operator Overloading in Python

## 📖 Overview

This folder contains practice programs demonstrating **Operator Overloading** in Python using special (dunder) methods. Operator overloading allows custom objects to behave like built-in data types by defining how operators such as `+`, `-`, `==`, `>`, and `len()` work for user-defined classes.

The programs in this folder focus on implementing arithmetic, comparison, and utility operators while strengthening Object-Oriented Programming (OOP) concepts.

---

## 📚 Topics Covered

* Introduction to Operator Overloading
* Special (Dunder) Methods
* `__add__()`
* `__sub__()`
* `__mul__()`
* `__eq__()`
* `__gt__()`
* `__lt__()`
* `__len__()`
* `__str__()`
* Returning New Objects from Overloaded Operators
* Object Comparison
* Custom Object Representation

---

## 💻 Programs Implemented

| File Name          | Concept Used                                                                                               |
| ------------------ | ---------------------------------------------------------------------------------------------------------- |
| `student.py`       | Overloaded `+` to add marks of two students                                                                |
| `bank_account.py`  | Overloaded `+` and `-` for deposit and withdrawal operations                                               |
| `rectangle.py`     | Compared rectangles using `>`, `<`, and `==` based on area                                                 |
| `shopping_cart.py` | Added prices of two products using `__add__()`                                                             |
| `book.py`          | Implemented `__len__()` to return the number of pages                                                      |
| `team.py`          | Implemented `__str__()` for a readable object representation                                               |
| `vector.py`        | Added two vectors using operator overloading                                                               |
| `fraction.py`      | Added two fractions and returned a new `Fraction` object                                                   |
| `complex.py`       | Implemented addition, subtraction, multiplication, equality, and string representation for complex numbers |

> **Note:** Matrix addition was studied as an advanced application of operator overloading but was intentionally postponed until learning matrices and 2D lists in depth.

---

## 🧠 Key Learnings

* Learned how Python internally maps operators to special methods.
* Understood the purpose of operator overloading in custom classes.
* Implemented arithmetic and comparison operators.
* Learned when to return primitive values and when to return new objects.
* Practiced overloading utility methods such as `__len__()` and `__str__()`.
* Improved understanding of Object-Oriented Programming through practical examples.
* Applied exception handling and input validation in the `Fraction` class.

---

## 🎯 Outcome

After completing this folder, I can:

* Create classes with overloaded operators.
* Customize the behavior of built-in operators for user-defined objects.
* Compare custom objects using relational operators.
* Return meaningful objects from overloaded methods.
* Improve object readability using special methods.
* Design cleaner and more intuitive OOP-based programs.

---

## 🚀 Next Topic

The next step in my Python learning journey is to continue with the upcoming Object-Oriented Programming concepts and apply them in larger real-world projects.
