# QuadraticEquationSolvePlot
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

## Unit tests
Unit tests can be run using command
python -m unittest

[MIT LICENSE](https://github.com/hrosicka/QuadraticEquationSolver/blob/master/doc/LICENSE.txt)

