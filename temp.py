# Small utility for reading the temperature of the parallella board

import sys
import time


def read_temp():
    raw = float(open('/sys/bus/iio/devices/iio:device0/in_temp0_raw').read())
    offset = float(open('/sys/bus/iio/devices/iio:device0/in_temp0_offset').read())
    scale = float(open('/sys/bus/iio/devices/iio:device0/in_temp0_scale').read())
    return (raw + offset)*scale/1000


def main(interval):
    if interval:
        while True:
            main(0)
            time.sleep(interval)
    temp = read_temp()
    print('Temp is: {:.2f} C'.format(temp))


if __name__ == '__main__':

    interval = None
    try:
        interval = int(sys.argv[1])
    except IndexError:
        pass
    except ValueError:
        print('Error: Cannot parse interval. Displaying temp only once.')

    main(interval)
    
