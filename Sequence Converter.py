#The below script converts single letter amino acids into 3-letter abbreviations, then sorts it into a SPARKY readable format
#This was written for python. To use, simply change 'seq.txt' to the name of your text file that contains your sequence
#Designed to work with any format (fafsta, uniprot, etc.) 

dic={'D':'Asp','T':'Thr','S':'Ser','E':'Glu','P':'Pro','G':'Gly','A':'Ala','C':'Cys','V':'Val',
'M':'Met','I':'Ile','L':'Leu','Y':'Tyr','F':'Phe','H':'His','K':'Lys','R':'Arg','W':'Trp','Q':'Gln','N':'Asn'}
#opens file and removes first line if it starts with >, for fafsta files
with open('seq.txt') as file:
    read=file.readlines()
    for lines,x in zip(read,range(len(read))):
        if lines.startswith('>'):
            sequence_file=read[(x+1):]
            break
        else:
            continue
seq_file="".join(sequence_file)
list=[]
#converts single letter amino acid to 3-letter abbreviation and sorts it into a column
for amino_acid in seq_file:
    abr = dic.get(amino_acid)
    if abr is None:
        continue
    spacer=abr+'\n'
    list.append(spacer)
joiner="".join(list)
print(joiner)
with open('seq_modified.txt', 'w') as f:
    f.write(joiner)
