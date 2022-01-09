import os
name = input('Enter the default name for the folder: ')
ext = []
extensions = input("Enter comma separated file extensions for files to include inside: ")
if ',' not in extensions:
    ext.append(extensions)
else:
    ext_lis = extensions.split(',')
    for ex in ext_lis: 
        ext.append(ex)
num_of_dir = int(input("How many directories(folders) would you like to create: "))+1
        
for i in range(1,num_of_dir):
	folder=f'{name}{i}'
	os.mkdir(path = folder)
	for f_ext in ext:
		fname = f'{folder}/{folder}.{f_ext}'
		data = f'# {fname}'
		with open(fname,'w') as fn:
			try:
				fn.write(data)
				fn.close()
			except:
				fn.close()	
print('done')