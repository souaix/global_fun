import logging
import os

from datetime import date


def set_logging(PATH):
    if not os.path.isdir(PATH):
        os.makedirs(PATH)

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] %(message)-s',
        filename=PATH+'/{}.log'.format(str(date.today()))
    )
    logging.debug('Debug log set up. Setting up console log.')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(message)-s', '%H:%M:%S')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.debug('Console log set up.')
