import random

class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self):
        return f"<Line ({self.a})x+({self.b})y+({self.c})=0>"

    def slope(self):
        return -self.a/self.b

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

class ModelSolution:
    @staticmethod
    def get_product_def(p1, q1, p2, q2):
        return p1*q2 - p2*q1

    @staticmethod
    def get_ab(a1, b1, a2, b2):
        return ModelSolution.get_product_def(a1, b1, a2, b2)

    @staticmethod
    def get_bc(b1, c1, b2, c2):
        return ModelSolution.get_product_def(b1, c1, b2, c2)

    @staticmethod
    def get_ca(c1, a1, c2, a2):
        return ModelSolution.get_product_def(c1, a1, c2, a2)

    @staticmethod
    def get_x(a1, b1, c1, a2, b2, c2):
        return ModelSolution.get_bc(b1, c1, b2, c2) / ModelSolution.get_ab(a1, b1, a2, b2)

    @staticmethod
    def get_y(a1, b1, c1, a2, b2, c2):
        return ModelSolution.get_ca(c1, a1, c2, a2) / ModelSolution.get_ab(a1, b1, a2, b2)

    @staticmethod
    def find_intersection(line1: Line, line2: Line) -> Point:
        x = ModelSolution.get_x(line1.a, line1.b, line1.c, line2.a, line2.b, line2.c)
        y = ModelSolution.get_y(line1.a, line1.b, line1.c, line2.a, line2.b, line2.c)
        return Point(x, y)

class Testcase:
    def __init__(self, a1, b1, c1, a2, b2, c2):
        self.line1 = Line(a1, b1, c1)
        self.line2 = Line(a2, b2, c2)
    
    def __repr__(self):
        return f"{self.line1} | {self.line2}"
    
    def is_valid(self) -> bool:
        return abs(self.line1.slope() - self.line2.slope()) > 1
    
    def get_answers(self):
        a1 = self.line1.a
        b1 = self.line1.b
        c1 = self.line1.c
        a2 = self.line2.a
        b2 = self.line2.b
        c2 = self.line2.c

        return {
            "ab": ModelSolution.get_ab(a1, b1, a2, b2),
            "bc": ModelSolution.get_bc(b1, c1, b2, c2),
            "ca": ModelSolution.get_ca(c1, a1, c2, a2),
            "x": ModelSolution.get_x(a1, b1, c1, a2, b2, c2),
            "y": ModelSolution.get_y(a1, b1, c1, a2, b2, c2),
        }

def gen_testcase():
    while True:
        a1, b1, c1, a2, b2, c2 = [random.choice([x for x in range(-100,100) if x != 0]) for _ in range(6)]
        testcase = Testcase(a1, b1, c1, a2, b2, c2)
        if testcase.is_valid():
            return testcase

NUM_TEST_CASES = 30
testcases = [ gen_testcase() for _ in range(NUM_TEST_CASES) ]