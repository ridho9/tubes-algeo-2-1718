import numpy as np
from model import *
from config import *
import math
import queue

command_q = queue.Queue()

def update_command(main_obj, command):
    if command[0] == "translate":
        set_state('anim')
        set_anim('type', 'translate')
        set_anim('t_x', float(command[1]))
        set_anim('t_y', float(command[2]))
        set_anim('f_c', 0)
        set_anim('mat', main_obj.mat.copy())

    elif command[0] == "dilate":
        set_state('anim')
        set_anim('type', 'dilate')
        set_anim('t_f', float(command[1]))
        set_anim('f_c', 0)
        set_anim('mat', main_obj.mat.copy())

    elif command[0] == "rotate":
        set_state('anim')
        set_anim('type', 'rotate')
        set_anim('t_a', float(command[1]))
        set_anim('t_x', float(command[2]))
        set_anim('t_y', float(command[3]))
        set_anim('f_c', 0)
        set_anim('mat', main_obj.mat.copy())

    elif command[0] == "reflect":
        set_state('anim')
        if(command[1] == 'x'):
            set_anim('type', 'custom')
            set_anim('t_m', np.array([[1,0],[0,-1]]))
        elif(command[1] == 'y'):
            set_anim('type', 'custom')
            set_anim('t_m', np.array([[-1,0],[0,1]]))
        elif(command[1] == 'y=x'):
            set_anim('type', 'custom')
            set_anim('t_m', np.array([[0,1],[1,0]]))
        elif(command[1] == 'y=-x'):
            set_anim('type', 'custom')
            set_anim('t_m', np.array([[0,-1],[-1,0]]))
        else:
            set_anim('type', 'reflect')
            set_anim('t_x', float(command[1]))
            set_anim('t_y', float(command[2]))
        set_anim('f_c', 0)
        set_anim('mat', main_obj.mat.copy())

    elif command[0] == "shear":
        set_state('anim')
        set_anim('type', 'shear')
        set_anim('t_ax', command[1])
        set_anim('t_f', float(command[2]))
        set_anim('f_c', 0)
        set_anim('mat', main_obj.mat.copy())

    elif command[0] == "stretch":
        set_state('anim')
        set_anim('type', 'stretch')
        set_anim('t_ax', command[1])
        set_anim('t_f', float(command[2]))
        set_anim('f_c', 0)
        set_anim('mat', main_obj.mat.copy())

    elif command[0] == "custom":
        m = np.array([[float(command[1]), float(command[2])],
                      [float(command[3]), float(command[4])]])
        set_state('anim')
        set_anim('type', 'custom')
        set_anim('t_m', m)
        set_anim('f_c', 0)
        set_anim('mat', main_obj.mat.copy())

    else:
        print("invalid command")

def update_input(objects):
    try:
        command = input().strip()
    except KeyboardInterrupt:
        print("Closing...")
        exit()

    main_obj = objects[0]
    assert isinstance(main_obj, Polygon)

    if command != '':
        command = command.split()
        if command[0] == "exit":
            print("Closing...")
            exit()
        elif command[0] == "polygon":
            point = int(command[1])
            mat = np.zeros((point, 2))
            for i in range(0, point):
                c = input().split()
                mat[i] = [float(c[0]), float(c[1])]
            main_obj.create_from_np(mat)

        elif command[0] == "reset":
            set_state('free')
            main_obj.reset()

        elif command[0] == "multiple":
            point = int(command[1])
            for i in range(0, point):
                command_q.put(input().strip().split())

        else:
            command_q.put(command)

def update_anim(objects):
    main_obj = objects[0]
    assert isinstance(main_obj, Polygon)

    if get_anim('type') == 'translate':
        d = math.sqrt(get_anim('t_x')**2 + get_anim('t_y')**2)
        s = int(d) / 5
        main_obj.mat = get_anim('mat').copy()
        s_x = get_anim('t_x') * get_anim('f_c') / s
        s_y = get_anim('t_y') * get_anim('f_c') / s

        if get_anim('f_c') >= s:
            set_state('free')
            main_obj.mat = main_obj.translate(get_anim('t_x'), get_anim('t_y'))
            return

        main_obj.mat = main_obj.translate(s_x, s_y)
        set_anim('f_c', get_anim('f_c') + 1)

    elif get_anim('type') == 'dilate':
        main_obj.mat = get_anim('mat').copy()
        d = math.fabs(get_anim('t_f') - 1) + 1
        s = int(d * 20)
        if(get_anim('t_f') >= 1):
            s_f = 1 + (((get_anim('t_f') - 1) * get_anim('f_c')) / s)
        elif (get_anim('t_f') < 1):
            s_f = 1 + ((-(1 - get_anim('t_f')) * get_anim('f_c')) / s)

        if get_anim('f_c') >= s:
            set_state('free')
            main_obj.mat = main_obj.dilate(get_anim('t_f'))
            return

        main_obj.mat = main_obj.dilate(s_f)
        set_anim('f_c', get_anim('f_c') + 1)

    elif get_anim('type') == 'rotate':
        main_obj.mat = get_anim('mat').copy()
        s = int(math.fabs(get_anim('t_a')))
        s_a = get_anim('t_a') * get_anim('f_c') / s

        if get_anim('f_c') >= s:
            set_state('free')

        main_obj.mat = main_obj.rotate(s_a, get_anim('t_x'), get_anim('t_y'))
        set_anim('f_c', get_anim('f_c') + 1)

    elif get_anim('type') == 'reflect':
        main_obj.mat = get_anim('mat').copy()
        s = 60
        f = 1 - (2 * get_anim('f_c') / s)

        if get_anim('f_c') >= s:
            set_state('free')
            main_obj.mat = get_anim('mat').copy()
            main_obj.mat = main_obj.rotate(180, get_anim('t_x'), get_anim('t_y'))
            return


        m = np.array([[f, 0],
                      [0, f]])
        main_obj.mat = main_obj.translate(-get_anim('t_x'), -get_anim('t_y'))
        main_obj.mat = main_obj.custom(m)
        main_obj.mat = main_obj.translate(get_anim('t_x'), get_anim('t_y'))
        set_anim('f_c', get_anim('f_c') + 1)

    elif get_anim('type') == 'shear':
        main_obj.mat = get_anim('mat').copy()
        d = math.fabs(get_anim('t_f'))
        s = int(d * 20)
        s_f = get_anim('t_f') * get_anim('f_c') / s

        if get_anim('f_c') >= s:
            set_state('free')

        main_obj.mat = main_obj.shear(get_anim('t_ax'), s_f)
        set_anim('f_c', get_anim('f_c') + 1)

    elif get_anim('type') == 'stretch':
        main_obj.mat = get_anim('mat').copy()
        d = math.fabs(get_anim('t_f') - 1) + 1
        s = int(d * 20)
        if(get_anim('t_f') >= 1):
            s_f = 1 + (((get_anim('t_f') - 1) * get_anim('f_c')) / s)
        elif (get_anim('t_f') < 1):
            s_f = 1 + ((-(1 - get_anim('t_f')) * get_anim('f_c')) / s)

        if get_anim('f_c') >= s:
            set_state('free')
            main_obj.mat = main_obj.stretch(get_anim('t_ax'), get_anim('t_f'))
            return

        main_obj.mat = main_obj.stretch(get_anim('t_ax'), s_f)
        set_anim('f_c', get_anim('f_c') + 1)

    elif get_anim('type') == 'custom':
        main_obj.mat = get_anim('mat').copy()
        s = 60
        d_m = get_anim('t_m') - np.array([[1,0],
                                          [0,1]])
        s_m = np.array([[1,0],[0,1]]) + (d_m * get_anim('f_c') / s)

        if get_anim('f_c') >= s:
            set_state('free')

        main_obj.mat = main_obj.custom(s_m)
        set_anim('f_c', get_anim('f_c') + 1)


def update_all(objects):
    if command_q.empty():
        if get_state() == 'free':
            update_input(objects)
        elif get_state() == 'anim':
            update_anim(objects)
    else:
        if get_state() == 'free':
            update_command(objects[0], command_q.get())
        elif get_state() == 'anim':
            update_anim(objects)
