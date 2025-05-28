input1=open('/Users/xuqiufan/Desktop/IBI/IBI1_2024-25/practical13/P09671.fasta','r')
input2=open('/Users/xuqiufan/Desktop/IBI/IBI1_2024-25/practical13/P04179.fasta','r')
input3=open('/Users/xuqiufan/Desktop/IBI/IBI1_2024-25/practical13/BLOSUM62.txt','r')
input4=open('/Users/xuqiufan/Desktop/IBI/IBI1_2024-25/practical13/Random sequence.fasta','r')

def analysed_seq (seq):
    analysed_seq=''
    for line in seq:
        if not line.startswith('>'):
            analysed_seq+=line.strip()
    return analysed_seq




blosum62={}
matrix=[]
for line in input3:
    if not line.startswith('#') and line.strip():
        matrix.append(line.strip())
aa_row=matrix[0].split()
        
for line in matrix[1:]:
    row=line.split()
    aa1=row[0]
    scores=row[1:]

    for i in range (len(aa_row)):
        aa2=aa_row[i]
        score=scores[i]
        blosum62 [(aa1,aa2)]=int(score)


def compare_pro(seq1, seq2):
    total_score=0
    for i in range(len(seq1)):
        aa1=seq1[i]
        aa2=seq2[i]
        if (aa1, aa2) in blosum62:
            score = blosum62[(aa1, aa2)]
        else:
            score=0
        total_score+=score   
    return total_score

def identity(seq1,seq2):
    identical=0
    for i in range(len(seq1)):
        aa1=seq1[i]
        aa2=seq2[i]
        if aa1==aa2:
            identical+=1
    identity=identical/len(seq1)*100
    return identity



seq1 = analysed_seq(input1)
seq2 = analysed_seq(input2)
seq3 = analysed_seq(input4) 

print("Mouse Seqence:", seq1)
print("Human Seqence:", seq2)
print("Random Sequence:", seq3)

print("Score between Mouse sequence and Human sequence:", compare_pro(seq1, seq2),'Identity between Rat sequence and Human sequence:',identity(seq1,seq2),'%')
print("Score between Mouse sequence and random sequence:", compare_pro(seq1, seq3),'Identity between Rat sequence and random sequence:',identity(seq1,seq3),'%')
print("Score between Human sequence and random sequence:", compare_pro(seq2, seq3),'Identity between Human sequence and random sequence:',identity(seq2,seq3),'%')



