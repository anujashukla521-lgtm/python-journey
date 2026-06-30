# Method Overriding in Python

## 📌 Overview

This folder contains programs demonstrating **Method Overriding** in Python using **Single Inheritance**. Method overriding allows a child class to provide its own implementation of a method that is already defined in the parent class, enabling **runtime polymorphism** and customized behavior.

---

## 📚 Topics Covered

* Method Overriding
* Single Inheritance
* Parent and Child Class Relationship
* Runtime Polymorphism
* Method Resolution
* Using `super()` with Overridden Methods
* Constructor Overriding (`__init__`)

---

## 💻 Programs Implemented

| File Name                        | Concept Practiced                              |
| -------------------------------- | ---------------------------------------------- |
| `animal_sound.py`             | Basic Method Overriding                        |
| `student_introduction.py`     | Overriding Parent Methods                      |
| `vehicle_start.py`            | Customizing Child Class Behavior               |
| `super_method.py`             | Calling Parent Method using `super()`          |
| `constructor_and_override.py` | Constructor with Method Overriding             |
| `mobile_phone.py`             | Extending Parent Functionality using `super()` |
| `library_member.py`           | Extending Member access using `super()`        |

---

## 🎯 Key Learnings

* Understood how a child class can redefine a method inherited from its parent.
* Learned that Python always checks the child class first before searching the parent class for a method.
* Practiced using the `super()` function to invoke the parent class implementation within an overridden method.
* Explored how constructor overriding works and when the parent constructor needs to be called explicitly.
* Improved understanding of runtime polymorphism through practical examples.

---

## 🚀 Outcome

After completing these programs, I gained hands-on experience with **Method Overriding** in Python and learned how inheritance enables flexible and reusable object-oriented designs. I also strengthened my understanding of method lookup, overriding behavior, and the proper use of `super()`.

---

## 📖 Interview Takeaways

* Method Overriding requires **inheritance**.
* The child class defines a method with the **same name** as the parent class.
* The overridden method is selected **at runtime**, making it an example of **runtime polymorphism**.
* `super()` allows access to the parent class implementation from within the overridden method.
* If the child class does not override a method, Python automatically uses the parent's implementation.

---

## 📂 Folder Purpose

This folder is part of my **Python Learning Journey**, where I practice object-oriented programming concepts through hands-on coding exercises and build a strong foundation in Python OOP.
