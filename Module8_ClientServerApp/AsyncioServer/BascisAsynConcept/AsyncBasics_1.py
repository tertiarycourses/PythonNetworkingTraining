
"""This is pretty neat in the sense you could easily have this go 
execute some I/O bound tasks like fetching data over the local 
network or Internet. Once you’ve collected the data you can then
 set the result with the Future’s set_result."""

import asyncio
 
@asyncio.coroutine
def my_coroutine(future, task_name, seconds_to_sleep=3):
    print('{0} sleeping for: {1} seconds'.format(task_name, seconds_to_sleep))
    yield from asyncio.sleep(seconds_to_sleep)
    future.set_result('{0} is finished'.format(task_name))
 
 
def got_result(future):
    print(future.result())
 
loop = asyncio.get_event_loop()
future1 = asyncio.Future()
future2 = asyncio.Future()
 
tasks = [
    my_coroutine(future1, 'task1', 3),
    my_coroutine(future2, 'task2', 1)]
 
future1.add_done_callback(got_result)
future2.add_done_callback(got_result)
 
loop.run_until_complete(asyncio.wait(tasks))
loop.close()