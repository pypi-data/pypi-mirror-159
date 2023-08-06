import sys

main_running = False


def entry(func):
    """
    invoke main func on running
    """

    getframe = getattr(sys, '_getframe')
    back = getframe().f_back

    global main_running

    if (back.f_locals['__name__'] == '__main__') and not main_running:
        main_running = True
        func()

    return func
