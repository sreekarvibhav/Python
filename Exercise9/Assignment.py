#Idea is to loop through a file and get the the email id of the sender who sent email most times by reading email logs from a flat file
#Get Filename input
name = input("Enter file:")
#IF filename is blank, assign default name
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


#create dictionary
email = dict()
#read file contents
for line in handle:
#check for email ids - All sender email ids start with "From ". Look for the string and add to dictionary
    if not line.startswith("From "):continue
    line = line.split()
    line = line[1]
    email[line] = email.get(line, 0) +1

#count the occurances of each key value pair in the dictionary and loop to find most used one
bigcount = None
bigword = None
for word,email in email.items():
    if bigcount == None or email > bigcount:
        bigword = word
        bigcount = email

print (bigword, bigcount)
