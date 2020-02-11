import os 

def find_files(suffix, path, found_files = None):
	try:
		files = os.listdir(path)
		if found_files == None:
			found_files = []
		for file_item in files:
			if os.path.isdir(os.path.join(path, file_item)):
				found_files += find_files(suffix, os.path.join(path, file_item))
			elif file_item.endswith("." + suffix):
				found_files.append(path + "/" + file_item)
		return found_files
	except:
		return "Path must not be empty or not found"
		
# Test Case
print(find_files("c", "testdir")) 
# ['testdir/subdir3/subsubdir1/b.c', 'testdir/t1.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c']
print(find_files("h", "testdir"))
# ['testdir/subdir3/subsubdir1/b.h', 'testdir/subdir5/a.h', 'testdir/t1.h', 'testdir/subdir1/a.h']
print(find_files("c", "testdir/subdir1"))
# ['testdir/subdir1/a.c']

# Edge Case
print(find_files("c", "testdir/7"))
# Path must not be empty or not found
print(find_files("", "testdir/subdir2"))
# []
print(find_files("c", ""))
# Path must not be empty or not found