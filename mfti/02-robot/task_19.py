#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    for i in range(4):
        move_left()

    if not wall_is_on_the_left():
        move_left()
        while not wall_is_above():
            move_up()
    else:
        for i in range(8):
            move_right()
        if not wall_is_on_the_right():
            move_right()
            while not wall_is_above():
                move_up()
            else:
                while not wall_is_on_the_left():
                    move_left()


if __name__ == '__main__':
    run_tasks()
