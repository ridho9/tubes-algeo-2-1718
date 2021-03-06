from OpenGL.GLUT import *
from controller import *

width, height = window['width'], window['height']
first = True

#untuk mempertahankan perspektif 2d
def refresh2d(width, height):
    scale = window['scale']
    x = int(width * scale/ 2)
    y = int(height * scale/ 2)
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-x, x, -y, y, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

#fungsi untuk menggambar garis-garis koordinat
#pada layar glut
def draw_coordinate_line():
    glLineWidth(1)
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_LINES)

    space = 10
    x = 10
    scale = window['scale']
    line_height = height * scale / 2
    while x <= width * scale / 2:
        glVertex2f(x, line_height)
        glVertex2f(x, -line_height)
        glVertex2f(-x, line_height)
        glVertex2f(-x, -line_height)
        x += space

    y = 10
    line_height = width * scale / 2
    while y <= height * scale / 2:
        glVertex2f(line_height, y)
        glVertex2f(-line_height, y)
        glVertex2f(line_height, -y)
        glVertex2f(-line_height, -y)
        y += space

    glEnd()

    glColor3f(0.35, 0.35, 0.35)
    glBegin(GL_LINES)

    space = 100
    x = 50
    line_height = height * scale / 2
    while x <= width * scale / 2:
        glVertex2f(x, line_height)
        glVertex2f(x, -line_height)
        glVertex2f(-x, line_height)
        glVertex2f(-x, -line_height)
        x += space

    y = 50
    line_height = width * scale / 2
    while y <= height * scale / 2:
        glVertex2f(line_height, y)
        glVertex2f(-line_height, y)
        glVertex2f(line_height, -y)
        glVertex2f(-line_height, -y)
        y += space

    glEnd()

    glLineWidth(2)
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_LINES)

    space = 100
    x = 100
    line_height = height * scale / 2
    while x <= width * scale / 2:
        glVertex2f(x, line_height)
        glVertex2f(x, -line_height)
        glVertex2f(-x, line_height)
        glVertex2f(-x, -line_height)
        x += space

    y = 100
    line_height = width * scale / 2
    while y <= height * scale / 2:
        glVertex2f(line_height, y)
        glVertex2f(-line_height, y)
        glVertex2f(line_height, -y)
        glVertex2f(-line_height, -y)
        y += space

    glEnd()


    glColor3f(1.0, 1.0, 1.0)

    glLineWidth(3)
    glBegin(GL_LINES)

    glVertex2f(0, height * scale / 2)
    glVertex2f(0, -height * scale / 2)
    glVertex2f(width * scale / 2, 0)
    glVertex2f(-width * scale / 2, 0)
    glEnd()

#inisialisasi object polygon
objects = []
objects.append(Polygon())

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    refresh2d(width, height)
    draw_coordinate_line()

    global objects
    #Fungsi untuk menggambar bangun
    #i merupakan object Polygon yang terdapat pada model.py
    for i in objects:
        i.draw()
    glutSwapBuffers()

    #Mengecek input user, bila ada, maka perintah akan dijalankan
    update_all(objects)
