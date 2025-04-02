import re
input=open('/Users/xuqiufan/Desktop/IBI/IBI1_2024-25/practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') 
inp=input.read()

single_line=re.sub(r'\n(?=>)','||',inp)
add_name=re.sub(r']\n','||',single_line)
add_space=re.sub(r'\n','',add_name)
delete_name=re.sub(r'\|\|','\n', add_space)
'''
single_line=re.sub(r'\n','',inp)
add_name=re.sub(r'>','\n>',single_line)
delete_name=re.sub(r']',']\n',add_name)
'''

output_line=[]
lines = re.split(r'\n',delete_name)
for line in lines:
     if line[0]=='>':
         gene_name= line[0:8]
     else:
        if re.search(r'TATA(A|T)A(A|T)',line):
            output_line.append([gene_name,line])


output=open('/Users/xuqiufan/Desktop/IBI/IBI1_2024-25/practical7/tata_genes.fa', 'w') 
for line in output_line:
   output.write(line[0]+'\n'+line[1]+'\n')

   
   
      




