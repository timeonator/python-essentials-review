#!/usr/bin/env python
import platform

def main():
    message()

def message():
    print ('This is python version {}', platform.python_version())

if __name__ == '__main__':
    main()
    