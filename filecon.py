import os, glob

input_files_location = r'C:\Users\juan\Documents\dev'
consolidated_file_loc = r'C:\Users\juan\Documents\dev\consolidation'

## Calculate the minimum value of a list with '' elements in it
def ext_min(x_list):
    return min([x for x in x_list if x != ''])

def none_list(x_list):
	return([x for x in x_list if x != ''] == [])

## Prepare consolidated file
os.chdir(consolidated_file_loc)
if os.path.isfile('conFile.txt'): os.remove('conFile.txt')
con_file = open('conFile.txt', 'w+')

## Read input files
os.chdir(input_files_location)
verb_files = glob.glob('*.txt')
print(verb_files)
N = len(verb_files) # number of input files

# List of input file objects 
f = [open(verb_files[i], 'r') for i in range(N)]
print(f)

## buffer. It is represent with a list
## each element is the stack of each input file
buff = [int(f[i].readline()) for i in range(N)]

while not none_list(buff):
    min_ind = buff.index(ext_min(buff))
    con_file.write(str(buff[min_ind])+'\n')
    next = f[min_ind].readline()
    if next == '':
        buff[min_ind] = ''
    else:
        buff[min_ind] = int(next)


## Close files
con_file.close()
for fichero in f:
    fichero.close()