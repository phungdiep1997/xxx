#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import subprocess as spr

VENV_NAME = "bai11"

def main():
    # virtualenv bai11

    # spr.check_output(["virtualenv", VENV_NAME])

    path = os.path.abspath(os.path.join(VENV_NAME, "bin", "activate"))
    print path
    # print spr.check_output("ps -ef", shell=True)
    spr.check_output("source " + path + "; pip install six; pip freeze > /tmp/req.txt",  shell=True)
    #spr.check_output("pip freeze > /tmp/req.txt ",  shell=True)


if __name__ == "__main__":
    main()
