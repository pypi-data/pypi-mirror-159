# directory_watcher

directory_watcher is a python module that will watch (via infinite loop) a directory.  When a file is encountered it will ensure the file isn't growing (by checking the file size, sleeping for 1 second, then checking the file size again), then passing it to a callback function to do whatever processing it needs to do on that file. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install directory_watcher.

```bash
pip install directory_watcher
```

## Usage

```python
from directory_watcher import directory_watcher as dir_watcher

def Setup():
    # Set the directory to watch
    dir_watcher.SetScanDirectory(d:\\data\\dir_to_watch)

    # Set the number of worker threads (to process files in parallel)
    dir_watcher.SetMaxWorkers(10)

    # Set the number of seconds to sleep between directory scans
    dir_watcher.SetSleepInterval(10)

def ProcessFile(full_path):
    print("The full path is %s" % (full_path))

if __name__ == '__main__':
    Setup()
    # The callback function to call for each file we process
    dir_watcher.SetFileProcessCallback(ProcessFile)

    # This setup function is called at the beginning of each run allowing changes to be made if necessary
    dir_watcher.SetSetupCallback(Setup)

    # Start the main thread which is an infinite loop walking the specified directory and sleeping
    dir_watcher.MainThread()


```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)