import re
input=open('/Users/xuqiufan/Desktop/IBI/IBI1_2024-25/practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') 
inp=input.read()


single_line=re.sub(r'\n(?=>)','||',inp)
add_name=re.sub(r']\n','||',single_line)
add_space=re.sub(r'\n','',add_name)
delete_name=re.sub(r'\|\|','\n', add_space)

output_line=[]
lines = re.split(r'\n',delete_name)
for line in lines:
     if not line:
        continue
     if line[0]=='>':
         gene_name=re.findall(r'gene:(\S+)',line)
         if gene_name:
             gene_name=gene_name[0]
         else:
          continue
     else:
        if re.search(r'TATA(A|T)A(A|T)',line):
            output_line.append([gene_name,line])


output=open('/Users/xuqiufan/Desktop/IBI/IBI1_2024-25/practical7/tata_genes.fa', 'w') 
for line in output_line:
   output.write(str(line[0])+'\n'+str(line[1])+'\n')

   
   
      




