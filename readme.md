# Project: OOP Concepts

## Overview

This project demonstrates the principles of Object-Oriented Programming (OOP) using a simple calculator application. The codebase is structured to highlight key OOP concepts such as classes, instances, methods, inheritance, and decorators.

## Object-Oriented Programming (OOP)

OOP is a programming paradigm that uses "objects" to design applications and computer programs. It utilizes several key concepts:

### Classes

A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have. In this project, we have a `Product` class that represents a product with attributes like `name`, `price`, and `quantity`.

### Instances

An instance is a specific object created from a class. Each instance can have different attribute values. For example, `product1` and `product2` are instances of the `Product` class, each with its own set of attribute values.

### Methods

Methods are functions defined within a class that describe the behaviors of the objects. They can manipulate object data and perform operations. In our project, methods like `sell` and `restock` are defined to manage product inventory.

### Inheritance

Inheritance allows a class to inherit attributes and methods from another class. This promotes code reuse and logical hierarchy. In this project, `DiscountProduct` is a subclass of `Product`, inheriting its attributes and methods while adding a `discount` attribute and overriding the `sell` method to apply a discount.

### Decorators

Decorators are a powerful feature in Python that allows you to modify the behavior of a function or method. They are applied using the `@decorator_name` syntax. In this project, the `@log_transaction` decorator is used to log the execution of methods, providing insights into method calls and completions.

## Project Structure

- **calculator/oop.py**: Contains the implementation of the `Product` and `DiscountProduct` classes, along with the `log_transaction` decorator.
- **calculator/operations.py**: Includes basic arithmetic operations like addition and subtraction.
- **tests/test_operations.py**: Contains test cases for the operations using pytest.

## Getting Started

To run this project, ensure you have Python 3.10 installed. You can install the necessary packages using the provided `Pipfile`.


Run the application and tests using:


## Conclusion

This project serves as a practical introduction to OOP concepts, demonstrating how classes, instances, methods, inheritance, and decorators can be used to build a structured and maintainable codebase.

Feel free to explore and modify the code to deepen your understanding of OOP!



