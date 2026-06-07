# Quadratic Equation Solver

<p align="center">
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/></a>
  <a href="https://numpy.org"><img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/></a>
  <a href="https://matplotlib.org"><img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge" alt="Matplotlib"/></a>
  <a href="https://github.com/hrosicka/QuadraticEquationSolver/actions/workflows/tests.yml"><img src="https://img.shields.io/github/actions/workflow/status/hrosicka/QuadraticEquationSolver/tests.yml?branch=master&style=for-the-badge&logo=github&label=Tests" alt="Tests Status"/></a>
</p>

<p align="center">
  <a href="https://github.com/hrosicka/QuadraticEquationSolver/stargazers"><img src="https://img.shields.io/github/stars/hrosicka/QuadraticEquationSolver?style=for-the-badge&logo=github&color=ffee55&logoColor=white" alt="GitHub Stars"/></a>
  <a href="https://github.com/hrosicka/QuadraticEquationSolver/commits/master"><img src="https://img.shields.io/github/last-commit/hrosicka/QuadraticEquationSolver?style=for-the-badge&logo=git&color=990000" alt="Last Commit"/></a>
  <a href="https://github.com/hrosicka"><img src="https://img.shields.io/badge/Author-Hanka%20%F0%9F%91%A9%E2%80%8D%F0%9F%94%AC-deeppink?style=for-the-badge" alt="Author: Hanka"/></a>
  <a href="./LICENSE"><img src="https://img.shields.io/github/license/hrosicka/QuadraticEquationSolver?style=for-the-badge&color=yellow" alt="GitHub License"/></a>
</p>

**Effortlessly solve quadratic equations, visualize their graphs, and gain insights into their roots – all in one place!**

## ToC

- [Quadratic equations made easy!](#quadratic-equations-made-easy)
- [Visualizes the Solution](#visualizes-the-solution)
- [Discriminant - 3 solution are possible](#discriminant---3-solution-are-possible)
- [Solution](#solution)
  - [Equation with 2 real roots](#equation-with-2-real-roots)
  - [Equation with 1 real root](#equation-with-1-real-root)
  - [Equation with 2 complex roots](#equation-with-2-complex-roots)
- [Input validation](#input-validation)
  - [Only integers](#only-integers)
  - [Coefficient a must be non zero](#coefficient-a-must-be-non-zero)
- [Tech Stack](#tech-stack)
- [Unit tests](#unit-tests)
- [Licence](#licence)

## Quadratic equations made easy!
- Enter the coefficients and let us do the rest.
- We'll show you the assembled equation.
- Calculate the discriminant and roots.
- Visualize the parabola with a graph.

## Visualizes the Solution
This program isn't just limited to solving quadratic equations; it can also visualize them!  The code utilizes the matplotlib library to generate a graph of the equation based on the user's input.  This graphical representation can be particularly helpful in understanding the relationship between the coefficients and the solution's behavior.

## Discriminant - 3 solution are possible
Distriminant: D = b^2 - 4ac
- when dicriminant is positive, equation has two real solutions
- when dicriminant is zero, equation has just one solution
- when dicriminant is negative, equation has two complex solutions

## Solution
### Equation with 2 real roots
D > 0    ->     2 real roots

![](https://github.com/hrosicka/PyQtQuadraticEquationSolvePlot/blob/master/doc/MainWindow.PNG)

### Equation with 1 real root
D = 0    ->     1 real root (Root1 = Root2)

![](https://github.com/hrosicka/PyQtQuadraticEquationSolvePlot/blob/master/doc/OneRoot.PNG)

### Equation with 2 complex roots
D < 0    ->     2 complex roots

![](https://github.com/hrosicka/PyQtQuadraticEquationSolvePlot/blob/master/doc/ComplexRoots.PNG)

## Input validation
### Only integers
It is possible insert only integers.
![](https://github.com/hrosicka/PyQtQuadraticEquationSolvePlot/blob/master/doc/InputValidationInteger.PNG)

### Coefficient a must be non zero
![](https://github.com/hrosicka/PyQtQuadraticEquationSolvePlot/blob/master/doc/ANotZero.PNG)

## Tech Stack
- **Language:** Python
- **Libraries:**
  - Matplotlib – for graphing the equation.
  - NumPy – for precise mathematical calculations.

## Unit tests
Unit tests can be run using command
python -m unittest

## Author
Lovingly crafted by [Hanka Robovska](https://github.com/hrosicka)

## Licence
This project is licensed under the MIT License. See the [LICENSE](https://github.com/hrosicka/QuadraticEquationSolver/blob/master/LICENSE) file for more details.

