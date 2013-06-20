#!/usr/bin/env python
# encoding: utf-8
from task import Task

class Job:
    
    def __init__(self, tasks):
        self.tasks = tasks
        self.last_done_task = None
    
    def get_total_work(self):
        return sum(task.time for task in self.tasks if task.status == "ok")
