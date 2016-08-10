import methods as m
import time
from words import split_words, print_result

def work_method(dir_path):
	counter = 1
	for file in m.get_files_in_dir(dir_path):
		print counter
		with open(file) as f:
			try:
				split_words(f.read().decode('utf-8'))
			except Exception, e:
				print str(e)
		counter += 1


if __name__ == "__main__":
	
	print "1 variant. All in one MAIN THREAD"
	start_time = time.time()
	
	work_method(m.dataset_dir())

	print_result()
	print "Time - ", time.time() - start_time 
