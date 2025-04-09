splice_gene=['GTAG','GCAG','ATAC']
print('please choose one of three donor/acceptor combinations(GTAG,GCAG,ATAC)')
while True:
    inpu=input('enter your choice:')
    if inpu in splice_gene:
        break
    else:
        print("please enter again:")
filename=inpu +'_spliced_genes.fa'
output=open('/Users/xuqiufan/Desktop/IBI/IBI1_2024-25/practical7/'+filename,'w')

splice_donor=inpu[0:2]
splice_acceptor=inpu[2:4]
import re
input1=open('/Users/xuqiufan/Desktop/IBI/IBI1_2024-25/practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
inp=input1.read()

single_line=re.sub(r'\n(?=>)','||',inp)
add_name=re.sub(r']\n','||',single_line)
add_space=re.sub(r'\n','',add_name)
delete_name=re.sub(r'\|\|','\n', add_space)

spliced_line=[]
lines = re.split(r'\n',delete_name)
for line in lines:
    if line[0]=='>':
        gene_name=line[0:8]
    else:
        if re.search(rf'{splice_donor}.+{splice_acceptor}',line):
            sequence=re.findall(rf'{splice_donor}.+{splice_acceptor}',line)
            if re.search(r'TATA(A|T)A(A|T)',sequence[0]):
                count=len(re.findall(r'TATA(A|T)A(A|T)',sequence[0]))
                spliced_line.append([gene_name,count,line])


for line in spliced_line:
    output.write(line[0]+' tata_count:'+str(line[1])+'\n'+line[2]+'\n')


