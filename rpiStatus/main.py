from time import sleep

from psutil import cpu_percent
import blinkt


def main():
    while True:
        cpu = cpu_percent()
        if cpu < 33:
            blinkt.set_all(0, 255, 0)
        elif cpu < 66:
            blinkt.set_all(210, 179, 27)
        else:
            blinkt.set_all(255, 0, 0)
        blinkt.show()
        sleep(5)


if __name__ == "__main__":
    main()
