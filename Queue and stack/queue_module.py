import queue

custqueue = queue.Queue(maxsize=3)
custqueue.empty()
custqueue.put(10)
custqueue.put(20)
custqueue.put(30)
custqueue.full()
custqueue.qsize()