# task 1
with open('myfile.txt', 'r') as file_object:
    print(file_object.readline()) # this is reading one line only
    print(file_object.readline()) # By calling readline() two times, you can read the two first lines:

# By looping through the lines of the file, you can read the whole file, line by line:
----------------------------------------
#file_object =  open('myfile.txt', 'r')
#for x in file_object:
#    print(x)
