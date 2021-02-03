import os
import subprocess
import sys
import threading



def main(argv):
  global iter
  iter = 0
  jobid = sys.argv[1]
  directory = sys.argv[2]
  resultfile = sys.argv[3]
  machine = sys.argv[4]
  scheduler = sys.argv[5]
  print("HEY, {} {} {}".format(jobid,directory,resultfile))
  checkqueue(iter)

def checkqueue(i):
    threading.Timer(5.0, checkqueue, [i=i+1]).start() # called every minute
    print("Hello, World! {}".format(i))
    i = i+1

if __name__ == "__main__":
    main(sys.argv[1:])
