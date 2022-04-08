#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    while not wall_is_on_the_left():
        move_left()
    else:
        while wall_is_above():
            move_right()
        else:
            while not wall_is_above():
                move_up()
            else:
                while not wall_is_on_the_left():
                    move_left()



if __name__ == '__main__':
    run_tasks()
