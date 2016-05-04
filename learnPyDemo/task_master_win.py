#task_master

import random, time,queue
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()


class QueueManager(BaseManager):
	pass

def return_task_queue():
	global task_queue
	return task_queue

def return_result_queue():
	global result_queue
	return result_queue

def test():
	#QueueManager.register('get_task_queue',callable=lambda: task_queue)
	#QueueManager.register('get_result_queue',callable=lambda: result_queue)
	QueueManager.register('get_task_queue',callable=return_task_queue)
	QueueManager.register('get_result_queue',callable=return_result_queue)

	manager = QueueManager(address=('192.168.0.150',5000),authkey=b'abc')

	manager.start()

	task = manager.get_task_queue()
	result = manager.get_result_queue()

	for i in range(10):
		n = random.randint(0,1000)
		print('put task %d...'%n)
		task.put(n)

	print('Try get results..')

	for i in range(10):
		r=result.get(timeout=20)
		print('result: %s'%r)

	manager.shutdown()
	print('master exit')

if __name__ == '__main__':
	freeze_support()
	test()