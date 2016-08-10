import time
import methods as m

from multiprocessing.dummy import Pool as ThreadPool
from words import split_words, print_result

def work_method(dir_path):
	
	for file in m.get_files_in_dir(m.dataset_dir() + dir_path + m.get_sep()):
		print counter
		with open(file) as f:
			try:
				split_words(f.read().decode('utf-8'))
			except Exception, e:
				print str(e)


if __name__ == "__main__":
	print "2 variant. Every directory in another THREAD"
	start_time = time.time()

	dirs_arr = m.get_dirs_in_dir(m.dataset_dir())
	
	pool = ThreadPool(len(dirs_arr))
	pool.map(work_method, dirs_arr)

	pool.close()
	pool.join()
	
	print_result()
	print "Time - ", time.time() - start_time 
