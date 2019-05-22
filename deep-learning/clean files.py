# from imutils import paths
import os 
# imagePaths = sorted(list(paths.list_images("images")))

directories = []

def fetch_directories(root):
    for root, dirs, files in os.walk(root):
        for d in dirs:
            # print (os.path.join(root, d))
            directories.append(os.path.join(root, d))
            pass
        pass

print("fetching directories")
fetch_directories("images")
x = 0
for directory in directories:
    for path, subdirs, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(path,name)
            x += 1
            if file_path[-4:] == ".PNG":
                new_name = os.path.join(path, "{}{}.PNG".format(directory, x))
                # print("File path {}".format(os.path.join(path, "{}{}.PNG".format(directory, x))))
                pass
            else: 
                new_name = os.path.join(path, "{}{}.TIFF".format(directory, x))
                # print("File path {}".format(os.path.join(path, "{}{}.TIFF".format(directory, x))))
                pass

            os.rename(file_path, new_name)
            pass
        pass
    print("finished renaming items in {}".format(directory))
    x = 0
    pass

