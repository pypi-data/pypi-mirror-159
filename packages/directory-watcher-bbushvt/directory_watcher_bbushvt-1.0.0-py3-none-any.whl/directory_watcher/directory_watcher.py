import signal
import os
from concurrent.futures import ThreadPoolExecutor
from time import sleep
import logging

g_log = logging.getLogger(__name__)


g_directory = ""
g_ignore_list = []
g_max_workers = 50
g_sleep_interval = 30
g_file_process_callback = None
g_setup_callback = None
g_cleanup_callback = None

def Handler(signum, frame):
    print("Exiting...")
    os.kill(os.getpid(), 9)

signal.signal(signal.SIGINT, Handler)


def SetIgnoreList(ignore_list):
    global g_ignore_list
    g_log.debug("SetIgnoreList() called")
    if(isinstance(ignore_list, list)):
        g_ignore_list = ignore_list   
        g_log.debug("g_ignore_list = " + ' / '.join(map(str,g_ignore_list)))
    else:
        g_log.error("SetIgnoreList() called with invalid option")

def SetScanDirectory(directory):
    global g_directory
    g_log.debug("SetScanDirectory() called")
    if(isinstance(directory, str) and os.path.isdir(directory)):
        g_directory = directory   
        g_log.debug("g_directory = " + g_directory)
    else:
        g_log.error("SetScanDirectory() called with invalid option")

def SetSleepInterval(sleep_interval):
    global g_sleep_interval
    g_log.debug("SetSleepInterval() called")
    if(isinstance(sleep_interval, int) and sleep_interval > 0):
        g_sleep_interval = sleep_interval   
        g_log.debug("g_sleep_interval = " + str(g_sleep_interval))
    else:
        g_log.error("SetSleepInterval() called with invalid option")

def SetMaxWorkers(max_workers):
    global g_max_workers
    g_log.debug("SetMaxWorkers() called")
    if(isinstance(max_workers, int) and max_workers > 0):
        g_max_workers = max_workers   
        g_log.debug("g_max_workers = " + str(g_max_workers))
    else:
        g_log.error("SetMaxWorkers() called with invalid option")

def SetFileProcessCallback(callback_function):
    global g_file_process_callback
    g_log.debug("SetFileProcessCallback() called") 
    if callable(callback_function):
        g_file_process_callback = callback_function       
        g_log.debug("g_file_process_callback = " + g_file_process_callback.__name__)
    else:
        g_log.error("SetFileProcessCallback() was called with invalid callback function")

def SetSetupCallback(callback_function):
    global g_setup_callback
    g_log.debug("SetSetupCallback() called") 
    if callable(callback_function):
        g_setup_callback = callback_function       
        g_log.debug("g_setup_callback = " + g_setup_callback.__name__)
    else:
        g_log.error("SetSetupCallback() was called with invalid callback function")

def SetCleanupCallback(callback_function):
    global g_cleanup_callback
    g_log.debug("SetCleanupCallback() called") 
    if callable(callback_function):
        g_cleanup_callback = callback_function       
        g_log.debug("g_cleanup_callback = " + g_cleanup_callback.__name__)
    else:
        g_log.error("SetCleanupCallback() was called with invalid callback function")

def CheckFile(file):
    # check to make sure the file isn't currenly being written to (ie the size isn't changing)
    try:   
        g_log.debug("Getting file size for: " + file)
        curSize = os.path.getsize(file)
        sleep(1)
        while(curSize != os.path.getsize(file)):
            g_log.debug("File size is increasing, checking again in 1 second")
            curSize = os.path.getsize(file)
            sleep(1)
        g_log.debug("File is not changing size, continuing")
        return True
    except:
        g_log.error("Error getting file size for: " + file)
        return False

def FileProcessThread(file):
    global g_file_process_callback
    if CheckFile(file):
        if(callable(g_file_process_callback)):
            g_log.debug("Calling callback function: " + g_file_process_callback.__name__)
            g_file_process_callback(file)
        else:
            g_log.error("g_file_process_callback has not been set")
    else:        
        return


def MainThread():
    global g_directory, g_max_workers, g_ignore_list, g_sleep_interval
    
    while True:
        g_log.debug("Starting scan of %s" % (g_directory))
        file_count = 0
        if callable(g_setup_callback):
            g_log.debug("Calling setup function: " + g_setup_callback.__name__)
            g_setup_callback()
        
        g_log.debug("Creating Thread Pool with %d workers" % (g_max_workers))
        executor = ThreadPoolExecutor(max_workers=g_max_workers)
        
        for root, sub_dir_list, file_list in os.walk(g_directory):
            # Remove directories in the ignore list
            for ignore in g_ignore_list:
                if ignore in sub_dir_list:
                    g_log.debug("Removing %s from sub_dir_list" % (ignore))
                    sub_dir_list.remove(ignore)

            for file in file_list:
                full_path = os.path.join(root, file)
                g_log.debug("Submitting %s to be processed" % (full_path))
                executor.submit(FileProcessThread, full_path)
                file_count += 1

        g_log.debug("Waiting on threads to finish...")
        executor.shutdown()
        g_log.debug("Threads finished")

        g_log.info("Processed %d files" % (file_count))
        g_log.info("Sleeping for %d seconds" % (g_sleep_interval))

        if callable(g_cleanup_callback):
            g_cleanup_callback()
        
        sleep(g_sleep_interval)


