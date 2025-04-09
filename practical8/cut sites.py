def find_cut(DNA,enzyme):
    for i in DNA:
        if i not in ['A','C','G','T']:
            return 'invalid DNA sequence'
    for j in enzyme:
        if j not in ['A','C','G','T']:
            return 'invalid enzyme sequence'
    cut_site=[]    
    for i in range(len(DNA)-len(enzyme)+1):
        if DNA[i:i+len(enzyme)]==enzyme:
            cut_site.append(i)
    return cut_site
            

        

DNA_seq='AGTCCCAGTCAGT'
enzyme='AGT'      
print(find_cut(DNA_seq,enzyme))
