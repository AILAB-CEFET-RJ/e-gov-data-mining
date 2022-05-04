import logging
from datetime import datetime


def init_log(dataset_name, col):
    col = col or 'non_col'
    log_file = 'data_augmentation_{}_{}.log'.format(dataset_name, col)
    logging.basicConfig(filename=log_file, level=logging.INFO)
    msg = 'Log started. Log file: {}'.format(log_file)
    register_log(msg)
    print(msg)


def register_log(msg, print_msg=False):
    dt = datetime.now().isoformat()
    logging.info('[{}] {}'.format(dt, msg))
    if print_msg:
        print(msg)
