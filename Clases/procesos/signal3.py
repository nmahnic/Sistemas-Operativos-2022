import signal, os
import time
import logging
from datetime import datetime
import multiprocessing

logging.basicConfig(format="%(module)s : %(funcName)s : (Process Details : (%(process)d, %(processName)s), Thread Details : (%(thread)d, %(threadName)s))\nLog Message : %(message)s\n",
                    datefmt="%d-%B,%Y %I:%M:%S %p",
                    level=logging.INFO)

def handler(sig_num, curr_stack_frame):
    logging.info("Signal : '{}' Received. Handler Executed @ {}".format(signal.strsignal(sig_num), datetime.now()))

def independent_process():
    logging.info("Start Time : {}".format(datetime.now()))

    signal.signal(signal.SIGHUP, handler)

    time.sleep(10)

    logging.info("End Time : {}".format(datetime.now()))

if __name__ == "__main__":
    logging.info("Start Time : {}".format(datetime.now()))

    ind_process = multiprocessing.Process(target=independent_process, name="Independent Process")
    ind_process.start()

    time.sleep(3)
    print("Process ID : {}".format(ind_process.pid))

    os.kill(ind_process.pid, signal.SIGHUP)

    ind_process.join()

    logging.info("End Time : {}".format(datetime.now()))