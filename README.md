A modular command-line calculator built using clean architecture principles, factory pattern design, and a REPL (Read–Eval–Print Loop) interface.

This project includes:
- Modular package structure
- Operation factory pattern
- Session-based command handling
- Full pytest test suite
- 100% test coverage enforcement
- GitHub Actions CI pipeline

Overview

The calculator supports basic arithmetic operations and interactive commands through a REPL interface. It demonstrates:

- Separation of concerns (calculation, operations, REPL)
- Object-oriented design
- Factory pattern implementation
- Automated testing with coverage validation
- Continuous Integration with GitHub Actions

Running the Application

To start the calculator REPL: python -m app.calculator.repl

Available commands
help- display available commands
history- show calculation history
exit - exit the application

arithmetic operations supported:
add
subtract
multiply
divide

all functionality is tested using pytest

The assignment uses Gihub actions to:
automatically run tests on every push
enforce 100% coverage
fail the build if coverage drops

Project structure
app/
calculation/
calculator/
operation/
tests/
.github/workflows/
