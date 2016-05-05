#task_worker
import time,queue,sys
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
	pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#server_addr = '192.168.0.150'
server_addr = '127.0.0.1'
print('connect to server %s'%server_addr)
manager = QueueManager(address=(server_addr,5000),authkey=b'abc')

manager.connect()

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
	try:
		n=task.get(timeout=1)
		print('run task %d*%d...'%(n,n))
		r='%d*%d=%d'%(n,n,n*n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('task queue is empty.')
print('work exit.')
