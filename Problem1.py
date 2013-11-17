'''
You are to write a program that takes a list of strings containing
integers and words and returns a sorted version of the list.
 
The goal is to sort this list in such a way that all words are in
alphabetical order and all integers are in numerical order.
Furthermore, if the nth element in the list is an integer it must
remain an integer, and if it is a word it must remain a word.
 
 
Input:
------
 
The input will contain a single, possibly empty, line containing a
space-separated list of strings to be sorted. Words will not contain
spaces, will contain only the lower-case letters a-z. Integers will be
in the range -999999 to 999999, inclusive. The line will be at most 1000
characters long.
 
 
Output:
-------
 
The program must output the list of strings, sorted per the requirements
above. Strings must be separated by a single space, with no leading
space at the beginning of the line or trailing space at the end of the
line.
 
 
Constraints:
------------
 
The code you submit must take input from stdin and produce output to
stdout as specified above. No other output is permitted. You can
assume the input will be valid. Feel free to use standard libraries to
assist in sorting.
 

We modified these constraints to accept the string from an opened text file.
'''




import sys

# Opens file and creates list from contents
# using whitespace as entry delineator.
def organize(filename):
    file = open(filename, "r")
    input_list = file.read().split()
    file.close()

    alpha_list = []
    num_list = []

# Assigns alpha and numeric entries to their own
# respective sorted lists.

    for entry in input_list:
        if entry.isalpha():
            alpha_list.append(entry)
        else:
            num_list.append(entry)

    alpha_list = sorted(alpha_list, key = str.lower)
    num_list = sorted(num_list, key=int)
    

# Populates new list with entries, ensuring every
# nth element is same type as original.

    final_list=[]
    
    for entry in input_list:
        if entry.isalpha():
            final_list.append(alpha_list.pop(0))
        else:
            final_list.append(num_list.pop(0))

    return final_list

# Calls sort function, using cmd line arg as parameter
# and prints result as string.

def main():
  #  filename = sys.argv[1]

    print ' '.join(organize(sys.argv[1]))
    
# Checks to ensure module is being run directly, not imported.

if __name__ == '__main__':
    main()    
