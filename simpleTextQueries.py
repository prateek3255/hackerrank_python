def textQueries(sentences, queries):
    for i in range(len(sentences)):
        sentences[i]=' '+sentences[i]+' '
    res=[]
    for i in queries:
        words=[' '+word+' ' for word in i.split(' ')]
        r=[]
        for sentence in range(len(sentences)):
            if all(word in sentences[sentence] for word in words):
                r.append(str(sentence))
        res.append(r)
    for i in res:
        if len(i)!=0:
            print(' '.join(i))
        else:
            print(-1)




textQueries(["how it was done","are you how","it goes to","goes done are it"],["done it","it"])