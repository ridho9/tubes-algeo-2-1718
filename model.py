from OpenGL.GL import *
import numpy as np
import math

#class polygon adalah model data yang akan digunakan untuk menyimpan
#titik-titik yang ada dan mentransformasikannya. Terdapat juga fungsi
#untuk menggambar titik-titik yang terdapat pada object berclass polygon
#ke layar
class Polygon:
    #mat = Current Matrix
    #_mat = Previous matrix
    def __init__(self):
        self.trans = None
        self.mat = None
        self.defined = False

    #inisialisasi dari matrix numpy
    def create_from_np(self, mat):
        self.defined = True
        self.mat = mat
        self._mat = mat

    #menggambar polygon ke layar
    def draw(self):
        if not self.defined:
            return

        glColor3f(0., 0., 1.0)
        glBegin(GL_POLYGON)
        for i in self.mat:
            glVertex2f(*(i))
        glEnd()

    #menambahkan state x dan y terakhir
    def translate(self, x, y):
        m = self.mat.copy()
        for i in m:
            i += np.array([x, y])
        return m

    #sama seperti fungsi di atas, namun tidak mengubah
    #matriks yang menjadi properti dari object
    def _translate_m(self, m, x, y):
        for i in m:
            i += np.array([x, y])
        return m

    #mengembalikan matriks titik-titik dikalikan dengan faktor pengali skalar
    def dilate(self, factor):
        return self.mat * factor

    #mengembalikan matriks hasil rotasi
    def rotate(self, angle, x, y):
        m = self.mat.copy()
        angle = -math.radians(angle)
        rot = np.array([[math.cos(angle), -math.sin(angle)],
                        [math.sin(angle), math.cos(angle)]])
        m = self._translate_m(m, -x, -y)
        m = m.dot(rot)
        m = self._translate_m(m, x, y)
        return m

    #mengembalikan matriks pencerminan yang merupakan
    #matriks rotasi
    def reflect(self, x, y):
        return self.rotate(180, x, y)

    #mengembalikan matriks hasil shear
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

    #mengembalikan matriks hasi stretch
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

    #menerima input matriks transformasi custom
    def custom(self, custom):
        return self.mat.dot(custom)

    #untuk mengembalikan matriks yang ada ke sebelum
    #perintah terakhir dilakukan
    def reset(self):
        self.mat = self._mat
