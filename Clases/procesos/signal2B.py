import signal
import os

pid = int(input("ingrese pid:"))

os.kill(pid, signal.SIGINT)