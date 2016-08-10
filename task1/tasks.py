import methods as m

from celery import Celery
from words import split_words

BROKER_URL = 'redis://localhost:6379/0'

app = Celery('tasks', backend="redis", broker=BROKER_URL)

@app.task
def work_method(dir_path):
	print "run Task - ", dir_path
	counter = 1
	for file in m.get_files_in_dir(dir_path):
		print counter
		with open(file) as f:
			try:
				split_words(f.read().decode('utf-8'))
			except Exception, e:
				return None
		counter += 1