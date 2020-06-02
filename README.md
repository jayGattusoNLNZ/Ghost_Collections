# Ghost Collections

A tool that builds a low data version of any folder based filestore based on folder names, file names and fixity.

This tool is based on reArranger. https://github.com/jayGattusoNLNZ/reArranger  

This tool is excellent for rehearsing file organisation moves before committing them to real files. 

This tool is excellent used in conjuntion with files_harmoniser, supporting the comparison of 2 folders, looking for duplicates and new files. https://github.com/jayGattusoNLNZ/files_harmoniser 

This tool is excellent used in conjuntion with rePeater, which allows a set of file mamangement operations to be logged, and repeated. https://github.com/jayGattusoNLNZ/rePeater 

### Example workflow

The work flow would be: 

log a file set with ghost_finder.py

Rebuild a new version with ghost_maker.py

Use file_harmoniser to figure out the changes you need to make - repeat until acceptanble results. 

Use rePeater to capture those moves. 

Use rePeater to replay the moves on the oroginal fileset. 

## ghost_finder.py

You point this at a folder, and it recursively logs every file name / path, and collects the MD5 of every path. 

Results in a text file [my_filename].log that contains newline seperated entreies for each file. 

Each entry is:

[filename]|[md5]

## ghost_maker.py

This takes a log file from the above process, and a starting folder location. 

It takes the item, and recreates the required folder structure the file started in, makes a new file (using the original filename and extension), and adds into the the file the digits that comprise its md5. 

This process relies on the uniqueness space of MD5 to assume that taking the MD5 of the new file will result in a reliably unique new md5, but from a much smaller file. 

The script checks this assumotion by counting / comparing the unique files in the log and the new folder, and counting / comparing the number of unique md5s in the log vs the new file set:


    Finished rebuild - checking outcome
    
    Master total logged files: 17681
    Master total rebuilt files: 17681
    OK: True

    Master unique logged files (by MD5): 17490
    Master unique rebuilt files (by MD5): 17490
    OK: True
