import time

start_time = time.time()

def end(message = "Ended"):
	print(message, "- %s (s)" % round(time.time() - start_time, 2))