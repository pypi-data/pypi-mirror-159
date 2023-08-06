import time

class Timer:
	def start(self):
		self.start_time = time.time()

	def end(self):
		print(" -- %s (s) -- " % round(time.time() - start_time, 2))