import os
import hashlib


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def get_log(my_f):
	with open( my_f ) as data:
		return [x for x in data.read().split("\n") if x != ""]

def rebuild():
	my_list = get_log(log_f)
	for item in my_list:
		my_f_path, my_hash = item.split("|", 1)
		print (my_f_path)
		my_f_path = os.path.join(dest, root_name, my_f_path)
		my_f_root, my_f_name = my_f_path.rsplit(os.sep, 1)
		if not os.path.exists(my_f_root):
			os.makedirs(my_f_root)
		with open(my_f_path, "w") as data:
			data.write(my_hash)

	hash_counter_checker() 

def hash_counter_checker():
	print ()
	print ("Finished rebuild - checking outcome")
	print ()
	print ()

	master_hashes = {}
	master_hashes_list = []
	my_list = get_log(log_f)
	for item in my_list:
		my_f_path, my_hash = item.split("|", 1)
		if my_hash not in master_hashes:
			master_hashes[my_hash] = []
		master_hashes[my_hash].append(my_f_path)
		master_hashes_list.append(my_hash)


	new_hashes = {}
	new_hashes_list = []

	for root, subs, files in os.walk(os.path.join( dest, root_name)):
		for f in files: 
			my_file = os.path.join(root, f)
			my_hash = md5(my_file)
			if my_hash not in new_hashes:
				new_hashes[my_hash] = []
			new_hashes[my_hash].append(my_file)
			new_hashes_list.append(my_hash)

	print ()
	print (f"Master total logged files: {len(master_hashes_list)}")
	print (f"Master total rebuilt files: {len(new_hashes_list)}")
	print (f"OK: {len(master_hashes_list) == len(new_hashes_list)}")
	print()
	print (f"Master unique logged files (by MD5): {len(set(master_hashes_list))}")
	print (f"Master unique rebuilt files (by MD5): {len(set(new_hashes_list))}")
	print (f"OK: {len(set(master_hashes_list)) == len(set(new_hashes_list))}")
	print()



### Set this as the root parent folder  
dest = r"C:\projects\ghost_collections\rebuilds"

### set this tp point at the logfile you previously made
log_f = r"C:\projects\ghost_collections\logs\socials_sidecar.log"

### set this to be the root folder name for the rebuld. 
root_name = "side_car_1"

rebuild()
