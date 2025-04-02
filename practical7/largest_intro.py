seq='ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
import re
a=re.findall(r'GT.+AG',seq)
b=len(a[0])
print('The intro sequence is',(a),'and the length is',b)
