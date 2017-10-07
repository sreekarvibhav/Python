#Get Filename input
name = input("Enter file:")
#IF filename is blank, assign default name
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


#create dictionary
hour = dict()
#read file contents
for line in handle:
#check for email ids - All sender email ids start with "From ". Look for the string and add to dictionary
    if not line.startswith("From "):continue
    line = line.split()
    line = line[5].split(':')
    hour[line[0]] = hour.get(line[0], 0) +1

#create a list to hold values
temp = list()

#append values in tuple to the list
for k,v in hour.items():
    temp.append ((k,v))
#sort
temp.sort()

#print
for hr, count in temp:
    print (hr, count)
