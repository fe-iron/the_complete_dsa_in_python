from multiprocessing import Queue

custqueue = Queue(maxsize=3)
custqueue.put(10)
custqueue.put(20)
custqueue.put(30)
custqueue.get()