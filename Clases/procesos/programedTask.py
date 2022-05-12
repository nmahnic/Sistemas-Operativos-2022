from datetime import datetime

f = open("output.txt", 'w')
f.write("{}".format(datetime.now()))
f.close()

#https://medium.com/analytics-vidhya/automating-and-scheduling-python-script-as-cronjobs-in-ubuntu-6b31fdbce3d1