#https://www.hackerrank.com/challenges/bear-and-steady-gene/problem
def contains(gene,remove):
    for i in remove:
        if gene.count(i)<remove[i]:
            return False
    return True
def steadyGene(gene):
    genes={'C':0,'G':0,'A':0,'T':0}
    remove={'C':0,'G':0,'A':0,'T':0}
    for i in genes:
        genes[i]=gene.count(i)
        if genes[i]>len(gene)//4:
            remove[i]=genes[i]-len(gene)//4
    mi=len(gene)
    start=0
    print(genes,remove)
    for i in range(len(gene)):
        if contains(gene[start:i],remove):
            while contains(gene[start:i],remove):
                start+=1
            start-=1
            if mi>(i-start):
                mi=i-start
                print(gene[start:i])
            start+=1
    return mi




if __name__ == '__main__':

    n = int(input())

    gene = input()

    result = steadyGene(gene)
    print(result)