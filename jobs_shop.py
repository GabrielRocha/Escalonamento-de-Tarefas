#!/usr/bin/env python
# encoding: utf-8
from job import Job
from task import task
from machine import Machine

class JobsShop():

    def __init__(self, jobs, machines):
        self.jobs = jobs
        self.machines = machines

    def get_jobs(self):
        return self.jobs

    def get_job_with_most_work(self):
        max_work ,job = max((job.get_total_work(),job) for job in self.jobs)
        return job, max_work

    def get_task_not_done(self, job):
        return [task for task in job.tasks if task.status == 'ok'][0]

    def run(self):
        max_work = 1
        while True:
            job, max_work = self.get_job_with_most_work()
            if max_work == 0:
                break
            task = self.get_task_not_done(job)
            self.update_current_time_machine(job, task)
            task.status = "done"
            job.last_done_task = task
    
    def update_current_time_machine(self, job, task):
        if job.last_done_task == None or task.machine.current_time >= job.last_done_task.time:
            task.machine.current_time += task.time
        else:
            task.machine.current_time += (task.time + job.last_done_task.time)
    
    def print_time_machines(self):
        for machine in self.machines:
            print machine.numero, machine.current_time
            

if __name__ == '__main__':
    machine1 = Machine(1)
    machine2 = Machine(2)
    machine3 = Machine(3)
    job1 = Job([task(3,machine1), task(5,machine3)])
    job2 = Job([task(2,machine2), task(3,machine1), task(1,machine3)])
    job3 = Job([task(1,machine2), task(2,machine3)])
    jobs_shop = JobsShop([job1,job2,job3],[machine1,machine2,machine3])
    jobs_shop.run()
    jobs_shop.print_time_machines()