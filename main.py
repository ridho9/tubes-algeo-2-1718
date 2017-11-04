from OpenGL.GLUT import *
from config import *
from view import draw

def hiasan():
    print(
        '''
#######   ########  ######## ##    ##  ######   ##
##     ## ##     ## ##       ###   ## ##    ##  ##
##     ## ##     ## ##       ####  ## ##        ##
##     ## ########  ######   ## ## ## ##   #### ##
##     ## ##        ##       ##  #### ##    ##  ##
##     ## ##        ##       ##   ### ##    ##  ##
 #######  ##        ######## ##    ##  ######   ########
 =======================================================
 Ridho Pratama - 13516032
 Gabriel Bentara Raphael - 13516119
 =======================================================
        '''
    )



if __name__ == "__main__":
    hiasan()
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(window['width'], window['height'])
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow(window['title'])
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()
