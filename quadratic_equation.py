import math
import cmath

class QuadraticEquation:
    """ 
    Calculation of quadratic equation including complex roots
    """

    def __init__(self, a, b, c):
        """
        Constructor
        a, b, c - coefficients - integers
        ax^2 - quadratic term
        bx - linear term
        c - constant term
        """
        self.a = a
        self.b = b
        self.c = c
        self.x1 = 0
        self.x2 = 0
        self.vertex_x = 0
        self.vertex_y = 0


    def discriminant(self):
        """
        D = b^2 - 4*a*c
        3 possibilities:
        D < 0 - 2 complex roots
        D = 0 
        D > 0 - 2 roots
        """
        D = pow(self.b,2) - 4*self.a*self.c
        return D


    def equation_type(self, D):
        """
        D - discriminant
        return equation type as a string
        """
        if self.a == 0:
            return "Not a quadratic equation (a = 0)."
        elif self.b == 0 and self.c == 0:
            return "Equation has a double root at zero (b = 0, c = 0)."
        elif D < 0:
            return "The roots are complex."
        elif D == 0:
            return "Equation has 1 root - the two roots are real and equal to each other."
        else:
            return "Equation has 2 roots - real and unequal."


    def solve(self):
        """
        Solution of quadratic equation
        """
        # --- EDGE CASE 1: If a = 0, it is not a quadratic equation ---
        if self.a == 0:
            raise ValueError("Coefficient 'a' cannot be zero in a quadratic equation.")

        # --- EDGE CASE 2: If b = 0 and c = 0 => x^2 = 0 => x = 0 ---
        if self.b == 0 and self.c == 0:
            self.x1 = self.x2 = 0.0
            self.vertex_x = 0.0
            self.vertex_y = 0.0
            return  # Early return to skip unnecessary calculations

        # --- Standard calculation ---
        D = self.discriminant()

        if D == 0:
            self.x1 = self.x2 = round(-self.b / (2 * self.a), 3)
            
        elif D > 0:
            self.x1 = round((-self.b + math.sqrt(D)) / (2 * self.a), 3)
            self.x2 = round((-self.b - math.sqrt(D)) / (2 * self.a), 3)

        else:
            self.x1 = (-self.b + cmath.sqrt(D)) / (2 * self.a)
            self.x2 = (-self.b - cmath.sqrt(D)) / (2 * self.a)
            self.x1 = complex(round(self.x1.real, 3), round(self.x1.imag, 3))
            self.x2 = complex(round(self.x2.real, 3), round(self.x2.imag, 3))

        # Vertex calculation for standard cases
        self.vertex_x = -self.b / (2 * self.a)
        self.vertex_y = self.a * self.vertex_x * self.vertex_x + self.b * self.vertex_x + self.c