#!/usr/bin/env python
from lib.daemons_1_3_1.daemons import daemonizer
import logging, time, sys, os, signal

PID_FILE = '/tmp/mydaemon.pid'
LOG_FILE = '/tmp/mydaemon.log'

# Setup logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

def kill_daemon():
    simpled.stop() # use force_kill_daemon() if daemon doesn't stop
    os.remove(PID_FILE)
    os.remove(LOG_FILE)
 
def force_kill_daemon():   
    with open(PID_FILE, 'r') as f:
        pid = int(f.read().strip())
    os.kill(pid, signal.SIGKILL)
    
@daemonizer.run(pidfile=PID_FILE)
def simpled():
    while True:
        logging.info("Daemon is running...")
        time.sleep(5)

def main():
    if os.path.exists(PID_FILE):
        print("Daemon is already running!")
        sys.exit(1)
    open(LOG_FILE, 'w').close() # create log file
    simpled() # start daemon

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} start|stop".format(sys.argv[0]))
        sys.exit(1)
    if sys.argv[1] == 'start':
        main()
    elif sys.argv[1] == 'stop':
        print('Stopping daemon...')
        kill_daemon()
    else:
        print("Invalid command. Use 'start' or 'stop'.")
        sys.exit(1)
