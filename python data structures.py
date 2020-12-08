#6.5
# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475";
startPos = text.find(':')
piece = text[startPos+1:]
end = float(piece)
print(end)


#7.1
#Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
file = input('enter file name:')
fname = 'words.txt'
try:
	fhandle = open(fname)
except:
	print('Cannot open the file ',fname ,'please try again')
	quit()

for line in fhandle:
	line = line.upper()
	line = line.rstrip()
	print(line)


#7.2
#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
fname = input("Enter file name: ")
fh = open(fname)
count = 0
average = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    average += float(line[20:-1].strip())
    count = count + 1
    #print(line)
    
print("Average spam confidence:", (average/count))
# file name : mbox-short.txt

#8.4
#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    line = line.split()
    for i in line: # observe indentation here
        if i not in lst:
            lst.append(i)
            
lst.sort() # observe indentation here.  this is where i made mistakes..
print(lst)
#file name : romeo.txt

#8.5
#Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    else:
        line = line.split()
        line = line[1]
        print(line)
    count += 1
print("There were",count,"lines in the file with From as the first word")
#filename : mbox-short.txt

#9.4
#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input("Enter file:")
if len(fname) < 1 : name = "mbox-short.txt"
hand = open(fname)

lst = list()

for line in hand:
    if not line.startswith("From:"): continue
    line = line.split()
    lst.append(line[1])

counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items(): 
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print(bigword,bigcount)
#filename : mbox-short.txt

#10.2
#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

name = input("Enter file:")
open_file=open(name)
file_dict={}
for line in open_file :
    line=line.rstrip()
    if line.startswith("From ") : 
            words=line.split()
            time=words[5]
            hours=time[:2]
            file_dict[hours]=file_dict.get(hours,0)+1
for k,v in sorted (file_dict.items()) :
    print(k,v)
#filename : mbox-short.txt



