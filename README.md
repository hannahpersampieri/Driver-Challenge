# Driver-Challenge
Driver Coding Challenge for Summer 2017 Internship

## The Problem:
The input to the problem is at most 50 DNA sequences (i.e, the character set is limited to T/C/G/A) whose length does not exceed 1000 characters. The sequences are given in FASTA format [https://en.wikipedia.org/wiki/FASTA_format]. These sequences are all different fragments of one chromosome.

The specific set of sequences you will get satisfy a very unique property:  there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length. An example set of input strings is attached.

The output of your program should be this unique sequence that contains each of the given input strings as a substring.

## My approach: 
We need to find the overlaps in these reads and join based on these overlaps. 
This means:
   0. Properly parsing the input file.
   1. Detect what portion of two subsequent reads are overlapped. Handle any edge cases that may come with that.
   2. Add to the result string: This needs to be done methodically, in order to avoid repetitions. 
      - I can approach this inductively: For the first read, we can add the entire string. For the next read, we would only need to add what is after the overlap. That can be continued until the end. 
   3. Print the result.  
   
### Testing:
In addition to the provided test file, I will write a few unit tests to cover edge cases. Although some of these edge cases may not be found in production (e.g., We wouldn't expect to find a sequence that is only one read), it is important to make sure the code works for any possible input. 
