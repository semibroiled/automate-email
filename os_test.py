import os

print(os.listdir())
cwd = os.getcwd()
subdirs = []
for directory in os.listdir():
    if '.csv' in directory:
        filepath = cwd+'/'+directory
        print(filepath)
        full_path = os.path.join(cwd, directory)
	
    #if os.path.isdir(full_path): # i wonder what does this do. apparently shows folerds in this path ie deeper directories
	#    subdirs.append(full_path)
        
print(subdirs)