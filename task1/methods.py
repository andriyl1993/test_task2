import os

def get_dirs_in_dir(path):
	return os.listdir(path)

def get_sep():
	return os.sep

def parent_dir():
	return os.getcwd() + os.sep

def dataset_dir():
	return parent_dir() + "edrmv2txt-v2" + os.sep

def get_files_in_dir(main_path):
	files = list()
	for path, subdirs, files in os.walk(main_path):
		for name in files:
			yield os.path.join(path, name)
	# return files