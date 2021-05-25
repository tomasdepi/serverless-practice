import time

def hello(event, context):
    print('Hi Version 3')
    time.sleep(4)
    return 'Hello World!!!'
