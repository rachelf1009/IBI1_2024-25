seq='ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
import re
a=re.findall(r'GT.+AG',seq)
if a:
    longest = max(a, key=len)
    print("The intron sequence is", longest, "and the length is", len(longest))
else:
    print("No intron found.")

