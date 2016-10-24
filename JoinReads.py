# Driver challenge
# Created by: Hannah Voelker
# October 18, 2016

import string
# Currently using test data, with expected output:
# ATTAGACCTGCCGGAATAC
INPUT_FILENAME = 'test_data.txt'

# If the real data wants to be tested, use: 
# INPUT_FILENAME = 'coding_challenge_data_set.txt'

def main():
    initial_array = read_file()
    reads = data_cleanup(initial_array)
    print join_reads(reads)

#Step 1, read input
# make array of reads
def read_file():
    file = open(INPUT_FILENAME, 'r')
    inputs = file.read().splitlines()
    return inputs

# Step 2: Clean up data
# This gives us an array where each element is what is printed on a new line in the .txt file. 
# We now must join each fragment of the read: 

def data_cleanup(inputs):
    result = []
    currindex = 0
    for i in range(len(inputs)-1):
        if('>' in inputs[i]):
            result.append(inputs[i+1])
            if(i != 0):
                currindex = currindex + 1
        elif('>' not in inputs[i+1]):
            result[currindex] = result[currindex] + inputs[i+1]
    return result

# Step 3: Use a variation of the "Greedy algorithim" to find the longest substring 
# Given an array of strings, return the list of strings with the 
# two strings having maximum overlap merged, the rest of the array unchanged.

def join_overlap(reads):
    max_length = -1
    result = []
    for i in range(len(reads)):
        # Compare prefix of one with suffix of another 
        # Make sure they are not the same index in the array
        for j in [num for num in range(len(reads)) if num != i]:
            # Name the two selected strings for code readability.
            prefix = reads[i]
            suffix = reads[j]
            # Begin finding the maximum overlap between the prefix and suffix strings.
            k = 0
            while prefix[k:] != suffix[0:len(prefix[k:])]:
                k += 1
            # Store the overlap length and string indicies if they the longest thus far.
            if len(prefix) - k > max_length:
                max_length = len(prefix) - k
                overlap_index = [i, j]

    # Return all strings without maximum overlap, and then the merged string with maximum overlap.
    result = [reads[z] for z in range(len(reads)) if z not in overlap_index]
    result = result + [reads[overlap_index[0]] + reads[overlap_index[1]][max_length:]]
    return result

# We must call the above method until we have merged every read into one string
# Where each element in our original array is a substring of the previous

def join_reads(reads):
   
    while len(reads) > 1:
        reads = join_overlap(reads)

    return reads[0]

if __name__ == '__main__':
    main()

