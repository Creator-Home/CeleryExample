from celery import shared_task, current_task
from celery.decorators import task

@shared_task
def add(x,y):
    #current_task.update_state(state='PROGRESS',meta={'process_percent':process_percent})
    print('your sum is :',x+y)
    return (x+y)

@task(name="sum_two_number")
def summ(x,y):
    return(x+y)
