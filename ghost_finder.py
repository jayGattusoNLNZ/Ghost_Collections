import os
import hashlib

### set this folder to where you want you log files to end up.
logs_folder = "ghost_collections"

if not os.path.exists(logs_folder):
    os.makedirs(logs_folder)


def md5(my_file):
    hash_md5 = hashlib.md5()
    with open(my_file, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_files_and_folders_from_root(parent):

    my_files = {}

    for root, subs, files in os.walk(parent):
        for f in files:
            my_file_path = os.path.join(root, f)
            my_md5 = md5(my_file_path)
            my_files[my_file_path.replace(parent, "")[1:]] = my_md5
    
    print (len(my_files))
    return my_files

### set this to be the folder you want to capture
folder = r"X:\LD_Proj\social_media_collecting"

#### set this to be a collection label for the log files.
collection_name = "socials_master"

my_files = get_files_and_folders_from_root(folder)

rows = []
for k, v in my_files.items():
    rows.append(f"{k}|{v}")

with open(os.path.join(logs_folder, f"{collection_name}.log"), 'w') as data:
    data.write("\n".join(rows))
### ____________________


# folder = r"X:\LD_Proj\Social_media_collecting_temp_store\harvests"
# collection_name = "socials_sidecar"

# my_files = get_files_and_folders_from_root(folder)

# rows = []
# for k, v in my_files.items():
#     rows.append(f"{k}|{v}")

# with open(os.path.join(logs_folder, f"{collection_name}.log"), 'w') as data:
#     data.write("\n".join(rows))

# ### ____________________

# folder = r"Y:\NDHA\legaldep-ftp\nlnzcollecting\socials"
# collection_name = "socials_ftp"


# my_files = get_files_and_folders_from_root(folder)

# rows = []
# for k, v in my_files.items():
#     rows.append(f"{k}|{v}")

# with open(os.path.join(logs_folder, f"{collection_name}.log"), 'w') as data:
#     data.write("\n".join(rows))
# ### ____________________
