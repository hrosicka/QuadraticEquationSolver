# PyQtQuadraticEquationSolvePlot
Simple application for solving and plotting Quadratic Equations

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


