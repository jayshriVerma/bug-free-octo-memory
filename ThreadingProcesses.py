import threading
import multiprocessing as mp 
import os

def cpu_waster():
   while True:
     pass
if __name__=="__main__":
  print('\n prrocess id ',os.getpid())
  print(' Thread count ',threading.active_count())
  for thread in threading.enumerate():
     print(thread)

  for i in range(12):
     mp.Process(target=cpu_waster).start()	

  print('\n prrocess id ',os.getpid())
  print(' Thread count ',threading.active_count())
  for thread in threading.enumerate():
      print(thread)   


