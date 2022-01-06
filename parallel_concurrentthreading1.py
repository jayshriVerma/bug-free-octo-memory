import threading
import time
import queue

serving_line = queue.Queue(maxsize=5)

def soup_producer():#servinng 20 bowls of soup
    for i in range(20):  
        serving_line.put_nowait("Bowl "+str(i))
        print('Served Bowl',str(i),'remaining capacity:',\
            serving_line.maxsize-serving_line.qsize())
        time.sleep(0.2)# time to serve the bowl of soup
    serving_line.put_nowait("No soup for you")# addinng to stop two consumer threads
    serving_line.put_nowait("No soup for you")

def soup_consumer():
	while True:
		bowl = serving_line.get()
		if bowl =="No soup for you":#here checking if there is no soup to consume it stop
	          break
		print("Ate",bowl)
		time.sleep(0.3) #time to eat a bowl of soup

if __name__=="__main__":
    for connsumer in range(2):#Now addinng 2 consumer with one producer, to overcome buffer overflow problem
       threading.Thread(target=soup_consumer).start()
    threading.Thread(target=soup_producer).start()    
	

