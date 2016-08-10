import time
import methods as m

from words import get_max
from tasks import work_method

if __name__ == "__main__":
	
	print "3 variant. Using celery"
	start_time = time.time()
	
	dirs_arr = m.get_dirs_in_dir(m.dataset_dir())
	results = []

	for d in dirs_arr:
		results.append(work_method.delay(m.dataset_dir() + d + m.get_sep()))

	waiting = True
	while waiting:
		waiting = False
		for r in results:
			if not r.ready():
				waiting = True
		time.sleep(1)

	print_result()
	print "Time - ", time.time() - start_time 