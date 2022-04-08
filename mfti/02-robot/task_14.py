#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    stop = False
    while not stop:
        if wall_is_on_the_right():
            stop = True
        if wall_is_beneath() and wall_is_above():
            fill_cell()
        if not wall_is_above() and wall_is_beneath:
            move_up()
            fill_cell()
            move_down()
        if not wall_is_beneath() and wall_is_above():
            move_down()
            fill_cell()
            move_up()
        if not wall_is_beneath() and not wall_is_above():
            move_up()
            fill_cell()
            move_down()
            move_down()
            fill_cell()
            move_up()
        if not wall_is_on_the_right():
            move_right()


if __name__ == '__main__':
    run_tasks()
