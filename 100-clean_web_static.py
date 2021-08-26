#!/usr/bin/python3
""" a Fabric script that deletes out-of-date archives """
from fabric.api import env, put, run, local, lcd, cd
from datetime import datetime
import os

env.hosts = ['34.139.184.21', '34.74.230.21']
env.key_filename = "~/.ssh/holberton"
env.user = "ubuntu"


def do_clean(number=0):
    ''' number is the number of the archives, including the most recent, to keep.
    If number is 0 or 1, keep only the most recent version of your archive.
    if number is 2, keep the most recent, and second most recent
    '''
    number = int(number)
    if number == 0 or number == 1:
        number = 1

    files = sorted(os.listdir("versions"))
    size = len(files)
    for i in range(number):
        if size > i:
            files.pop()
    with lcd("versions"):
        for file_name in files:
            local("rm -f {}".format(file_name))

    with cd("/data/web_static/releases"):
        all_files = run("ls -tr -1").split("\r\n")
        files = [name for name in all_files if "web_static_" in name]
        size = len(files)
        for i in range(number):
            if size > i:
                files.pop()
        for file_name in files:
            run("rm -rf {}".format(file_name))
