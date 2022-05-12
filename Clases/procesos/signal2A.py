import signal
import time
import logging
from datetime import datetime

logging.basicConfig(format="%(module)s : %(funcName)s : (Process Details : (%(process)d, %(processName)s), Thread Details : (%(thread)d, %(threadName)s))\nLog Message : %(message)s\n",
                    datefmt="%d-%B,%Y %I:%M:%S %p",
                    level=logging.INFO)

def handler(sig_num, curr_stack_frame):
    logging.info("Signal : '{}' Received. Handler Executed @ {}".format(signal.strsignal(sig_num), datetime.now()))

if __name__ == "__main__":
    logging.info("Start Time : {}".format(datetime.now()))

    signal.signal(signal.SIGINT, handler)

    signal.pause()

    logging.info("End Time : {}".format(datetime.now()))