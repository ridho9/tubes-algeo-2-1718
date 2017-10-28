from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math
from config import *
from view import draw

if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(window['width'], window['height'])
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow(window['title'])
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()