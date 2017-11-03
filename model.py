import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math
from config import *


class Polygon:
    def __init__(self):
        self.trans = None
        self.mat = None
        self.defined = False

    def create_from_np(self, mat):
        self.defined = True
        self.mat = mat
        self._mat = mat

    def draw(self):
        if not self.defined:
            return

        glColor3f(0., 0., 1.0)
        glBegin(GL_POLYGON)
        for i in self.mat:
            glVertex2f(*(i))
        glEnd()

    def translate(self, x, y):
        m = self.mat.copy()
        for i in m:
            i += np.array([x, y])
        return m

    def _translate_m(self, m, x, y):
        for i in m:
            i += np.array([x, y])
        return m

    def dilate(self, factor):
        return self.mat * factor

    def rotate(self, angle, x, y):
        m = self.mat.copy()
        angle = -math.radians(angle)
        rot = np.array([[math.cos(angle), -math.sin(angle)],
                        [math.sin(angle), math.cos(angle)]])
        m = self._translate_m(m, -x, -y)
        m = m.dot(rot)
        m = self._translate_m(m, x, y)
        return m

    def reflect(self, x, y):
        return self.rotate(180, x, y)

    def shear(self, axis, factor):
        if axis == 'y':
            s = np.array([[1, factor],
                          [0, 1]])
        elif axis == 'x':
            s = np.array([[1, 0],
                          [factor, 1]])
        else:
            raise Exception("error")
        return self.mat.dot(s)

    def stretch(self, axis, factor):
        if axis == 'x':
            s = np.array([[factor, 0],
                          [0, 1]])
        elif axis == 'y':
            s = np.array([[1, 0],
                          [0, factor]])
        else:
            raise Exception("error")
        return self.mat.dot(s)

    def custom(self, custom):
        return self.mat.dot(custom)

    def reset(self):
        self.mat = self._mat
