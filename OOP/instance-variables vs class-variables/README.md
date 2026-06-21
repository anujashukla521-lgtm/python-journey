# Instance Variables vs Class Variables

## Overview

This folder contains Python programs created to understand the difference between **instance variables** and **class variables**. The examples demonstrate how data can be stored either separately for each object or shared across all objects of a class.

## Topics Covered

* Instance Variables
* Class Variables
* Object Creation
* Constructors (`__init__`)
* Attribute Access
* Shared Data Across Objects
* Variable Shadowing
* Basic OOP Design

## Programs Included

### 1. Student Counter (`student_counter.py`)

**Concepts Practiced:**

* Class variables
* Instance variables
* Object counting

**Purpose:**
Tracks the total number of student objects created while storing individual student names.

---

### 2. Employee Company (`employee_company.py`)

**Concepts Practiced:**

* Shared class data
* Instance-specific attributes
* Class vs instance variable behavior

**Purpose:**
Demonstrates how modifying class variables and instance variables affects different objects.

---

### 3. Library Membership (`library_membership.py`)

**Concepts Practiced:**

* Class-level counters
* Object attributes
* Data organization using classes

**Purpose:**
Stores library member information and maintains the total number of registered members.

## Key Learnings

* Instance variables belong to individual objects.
* Class variables are shared among all objects of a class.
* Changing a class variable affects all objects that use it.
* Creating an instance variable with the same name as a class variable overrides access for that specific object.
* Class variables are useful for maintaining data shared across all instances.

## Outcome

Successfully implemented multiple programs to understand the practical usage of instance variables and class variables in Python and strengthened foundational Object-Oriented Programming concepts.

## Future Improvements

* Explore `@classmethod`
* Explore `@staticmethod`
* Learn advanced OOP concepts
* Implement larger projects using class and instance variables
