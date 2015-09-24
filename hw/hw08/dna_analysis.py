# Name: Jennifer N
# CSE 140
# Homework 2: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this program.")
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
at_count = 0

g_count = 0
c_count = 0
a_count = 0
t_count = 0

not_gcat = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1
        if bp == 'G':
            g_count = g_count + 1
        else:
            c_count = c_count + 1
    # next, if the bp is a A or a T,
    elif bp == 'A' or bp == 'T':
        # increment the count of ac
        at_count = at_count + 1
        if bp == 'A':
            a_count = a_count + 1
        else:
            t_count = t_count + 1
    else:
        not_gcat = not_gcat + 1

# Total sum of g, c, a, t _count's
gcatx_sum = g_count + c_count + a_count + t_count + not_gcat

# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count
at_content = float(at_count) / total_count

# Print the answer
print('AT/GC ratio:', at_content / gc_content)
print('GC-content:', gc_content)
print('AT-content:', at_content)
print('G-content:', g_count)
print('C-content:', c_count)
print('A-content:', a_count)
print('T-content:', t_count)

# Sanity check
print(total_count, len(seq), gcatx_sum)
print(total_count == len(seq) == gcatx_sum)
