from bs4 import BeautifulSoup
from datetime import datetime
import requests
import itertools
import threading

alphabet1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
alphabet2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "_"]
alphabet3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lists = [alphabet1, alphabet2, alphabet2, alphabet2, alphabet3]
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
count = 0
threCh = True

code = list("aaaaa")
codes = list(itertools.product(*lists))

print(len(codes))

class myThread (threading.Thread):
	def __init__(self, name, n, nmax):
		threading.Thread.__init__(self)
		self.name = name
		self.n = n
		self.nmax = nmax

	def run(self):
		cycle(self.n, self.name, self.nmax)





			

def cycle(n, name, nmax):
	
	global threCh
	t = 0


	
	for i in range(n,len(codes)):
		if threCh:


			code = codes[i]
			global count
			url = "http://t.me/"+"".join(code)
			page = requests.get(url)
			soup = BeautifulSoup(page.text, "html.parser")
			child_soup = soup.find_all("i", {"class": "tgme_icon_user"})
			count=count+1
			now = datetime.now()
			current_time = now.strftime("%H:%M:%S")
			t=t+1
			if(t<nmax):
				threCh = True
			elif(t>nmax): 
				threCh = False			
			print(str(count)+" - "+url+" - " + current_time + " --- " + name + " "+ str(t)+str(threCh))


thread1 = myThread("Thread-1", 0, 20);
thread2 = myThread("Thread-2", 100, 20);


thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Exiting the Program")


