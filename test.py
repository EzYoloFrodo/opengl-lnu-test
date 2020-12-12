from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def general_init():
    light_ambient = [.0, .0, .0, 1.]
    light_diffuse = [1., 0., .0, 1.]
    light_specular = [1., 1., 1., 1.]
    light_position = [1., 1., 1., 0.]

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glEnable(GL_LIGHT0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glPushMatrix()
    glScalef(1.3, 1.3, 1.3)
    glRotatef(20.0, 1.0, 0.0, 0.0)

    glPushMatrix()
    glTranslatef(-0.75, 0.5, 0.0)
    glRotatef(90.0, 1.0, 0.0, 0.0)
    glutSolidTorus(0.275, 0.85, 10, 15)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.75, -0.5, 0.0)
    glRotatef(270.0, 1.0, 0.0, 0.0)
    glutSolidTetrahedron()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.75, 0.0, -1.0)
    glutSolidIcosahedron()
    glPopMatrix()

    glPopMatrix()
    glFlush()


def reshape(w: int, h: int):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if w <= h:
        glOrtho(-2.5, 2.5, -2.5 * h / w, 2.5 * h / w, -10.0, 10.0)
    else:
        glOrtho(-2.5 * w / h, 2.5 * w / h, -2.5, 2.5, -10.0, 10.0);
        glMatrixMode(GL_MODELVIEW)


def polygon_mode(value: int):
    if value == 1:
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glDisable(GL_BLEND)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    elif value == 2:
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_LIGHTING)
        glColor3f(1.0, 1.0, 1.0)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glutPostRedisplay()


def main_menu(value: int):
    if value == 666:
        exit(0)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(500, 500)
    glutCreateWindow("OpenGL Coding Practice")

    general_init()
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    submenu = glutCreateMenu(polygon_mode);

    glutAddMenuEntry("Filled", 1)
    glutAddMenuEntry("Outline", 2)
    glutCreateMenu(main_menu)
    glutAddMenuEntry("Quit", 666)
    glutAddSubMenu("Polygon mode", submenu)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    glutMainLoop()


if __name__ == '__main__':
    main()
