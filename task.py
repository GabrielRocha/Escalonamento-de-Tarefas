#!/usr/bin/env python
# encoding: utf-8
from machine import Machine

class Task():

    def __init__(self, time, machine):
        self.time = time
        self.machine = machine
        self.status = "ok"
        
def task(time, machine):
    return Task(time,machine)