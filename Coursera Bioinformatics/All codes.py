##Biology Meets Programming Bioinformatics for Beginners##

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

def FrequentWords(Text, k):
    words=[]
    freq=FrequencyMap(Text,k)
    m=max(freq.values())
    for pattern in freq:
        if freq[pattern]==m:
            words.append(pattern)
    words.sort()
    return words

def FrequencyMap(Text, k):
    freq={}
    for i in range(len(Text)-k+1):
        Pattern=Text[i:i+k]
        freq[Pattern]=0
        for i in range(len(Text)-k+1):
            if Text[i:i+k]==Pattern:
                freq[Pattern]+=1
    return freq

def Complement(Pattern):
    comp=""
    compbp={'A':'T','G':'C','C':'G','T':'A'}
    for bp in Pattern:
	comp+=compbp[bp]
    return comp

def Reverse(Pattern):
    rev_pattern=""
    for ch in Pattern:
        rev_pattern=ch+rev_pattern
    return rev_pattern

Pattern="AAAACCCGGT"
def Count(Motifs):
    count = {} # initializing the count dictionary
    for symbol in "ACGT":
        count[symbol]=[]
        for i in range(len(Motifs[0])):
            count[symbol].append(0)
    for i in range(len(Motifs)):
        for j in range(len(Motifs[i])):
            symbol=Motifs[i][j]
            count[symbol][j]+=1           
    return count

Reverse(Pattern)

def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)]==Pattern:
            positions.append(i)
    return positions

Genome="GATATATGCATATACTT"
Pattern="ATAT"

PatternMatching(Pattern,Genome)

def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(symbol, Genome[0:n//2])

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

#Hamming distance:
#We say that position i in k-mers p and q is a mismatch if the symbols at position i of the two strings are not the same. The total number of mismatches between strings p and q is called the Hamming distance between these strings. 

def HammingDistance(p,q):
	mismatch=0
	for i in range(len(p)):
		if p[i]!=q[i]:
			mismatch+=1
	return mismatch
###########################################################################
def Count(Motifs):
    count = {} 
    for symbol in "ACGT":
        count[symbol]=[]
        for i in range(len(Motifs[0])):
            count[symbol].append(0)
    for i in range(len(Motifs)):
        for j in range(len(Motifs[i])):
            symbol=Motifs[i][j]
            count[symbol][j]+=1           
    return count

def Profile(Motifs):
    t=len(Motifs)
    k=len(Motifs[0])
    profile={}
    arr=Count(Motifs)
    for c in "ACGT":
        profile[c]=[]
        for i in range(k):
            profile[c].append(0)
    for i in range(k):
        for c in "ACGT":
            profile[c][i]=float(arr[c][i])/t
    return profile

def Consensus(Motifs):
    k=len(Motifs[0])
    t=len(Motifs)
    arr=Count(Motifs)
    str=""
    for i in range(k):
        maxd=0
        for char in "ACGT":
            if arr[char][i]>maxd:
                maxd=arr[char][i]
        for char in "ACGT":
            if arr[char][i]==maxd:
                str+=char
                break
    return str

def Score(Motifs):
    arr=Count(Motifs)
    consensus=Consensus(Motifs)
    t=len(Motifs)
    k=len(Motifs[0])
    score=0
    for i in range(k):
        for char in "ACGT":
            if char !=consensus[i]:
                score+=arr[char][i]
    return score

def Pr(Text, Profile):
    p=1
    k=len(Text)
    for i in range(k):
        char = Text[i]
        p*=Profile[char][i]
    return p

def ProfileMostProbableKmer(text, k, profile):
    maxp=-1
    mpstr=""
    for i in range(len(text)-k+1):
        pattern=text[i:i+k]
        p=Pr(pattern,profile)
        if p>maxp:
            maxp=p
            mpstr=pattern
    return mpstr

def GreedyMotifSearch(Dna, k, t):
    #Greedy Algorithm for motif search.
    bestmotifs=[]
    for i in range(t):
        bestmotifs.append(Dna[i][0:k])
    n=len(Dna[0])
    for i in range(n-k+1):
        motif=[]
        motif.append(Dna[0][i:i+k])
        for j in range(1,t):
            profile=Profile(motif)
            mpstr=ProfileMostProbableKmer(Dna[j],k,profile)
            motif.append(mpstr)
        if Score(motif)<Score(bestmotifs):
            bestmotifs=motif
    return bestmotifs

###########################################################################
def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count={}
    for char in "ACGT":
        count[char]=[]
        for i in range(k):
            count[char].append(1)
    for i in range(k):
        for j in range(t):
            count[Motifs[j][i]][i]+=1
    return count

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {} 
    for char in "ACGT":
        profile[char]=[]
        for i in range(k):
            profile[char].append(0)
    arr=CountWithPseudocounts(Motifs)
    total=[]
    for i in range(k):
        total.append(0)
        for char in "ACGT":
            total[i]+=arr[char][i]        
    for i in range(k):
        for char in "ACGT":
            profile[char][i]=arr[char][i]/total[i]
    return profile


def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    bestmotifs=[]
    for i in range(t):
        bestmotifs.append(Dna[i][0:k])
    n=len(Dna[0])
    for i in range(n-k+1):
        motif=[]
        motif.append(Dna[0][i:i+k])
        for j in range(1,t):
            profile=ProfileWithPseudocounts(motif)
            mpstr=ProfileMostProbableKmer(Dna[j],k,profile)
            motif.append(mpstr)
        if Score(motif)<Score(bestmotifs):
            bestmotifs=motif
    return bestmotifs


def Motifs(Profile, Dna):
    Motifs=[]
    for i in range(len(Dna)):
        Motifs.append(ProfileMostProbableKmer(Dna[i],k,Profile))
    return Motifs

def RandomMotifs(Dna, k, t):
    t_string=[]
    for i in range(t):
        num=random.randint(0,len(Dna[i])-k)
        pattern=""
        pattern=Dna[i][num:num+k]
        t_string.append(pattern)
    return t_string
t=len(Dna)


def RandomizedMotifSearch(Dna, k, t):
    M=RandomMotifs(Dna,k,t)
    BestMotifs=M
    while True:
        profile=ProfileWithPseudocounts(M)
        M=Motifs(profile,Dna)
        if Score(M)<Score(BestMotifs):
            BestMotifs=M
        else:
            return BestMotifs

def Normalize(Probabilities):
    sumd=sum(Probabilities.values())
    for key in Probabilities.keys():
        Probabilities[key]/=sumd
    return Probabilities

def WeightedDie(Probabilities):
    kmer = '' # output variable
    num=random.uniform(0,1)
    sumd=0
    for key in Probabilities.keys():
        sumd+=Probabilities[key]
        if num<sumd:
            kmer=key
            break
    return kmer


def ProfileGeneratedString(Text, profile, k):
    n=len(Text)
    probabilities={}
    for i in range(n-k+1):
        probabilities[Text[i:i+k]]=Pr(Text[i:i+k],profile)
    probabilities=Normalize(probabilities)
    return WeightedDie(probabilities)






