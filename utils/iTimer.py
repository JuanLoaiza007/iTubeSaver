import time

debug = True


def print_debug(message):
    new_message = "[iTimer.py]: " + message
    if debug:
        print(new_message)


class iTimer():
    def __init__(self):
        self.start_time = time.time()
        self.end_time = None
        print_debug("instance started!")

    def end(self):
        self.end_time = time.time()
        total_time = self.end_time - self.start_time
        print_debug(
            "instance end after {:.2f} seconds!".format(total_time))
