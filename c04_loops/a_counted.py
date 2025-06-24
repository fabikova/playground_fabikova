ITER_STOP = 10
ITER_START = 0


def step_print(name, i):
    print(f'[{name}] Step #{i:02d}')


def counted_while(start, stop, step=1):
    i = start
    loop_name = 'while'

    while i < stop:  # just run condition, loops while it is true
        i += 1  # need to increment by myself
        step_print(loop_name, i)  # some actual work
        # i+= 1 # increment could be useful at the end of the loop, if we want to start from 0


if __name__ == '__main__':
    counted_while(ITER_START, ITER_STOP)
