'''Created on 17 Aug 2011 @author: Matthew'''
#encoding: UTF-8

allDicts={} #dict of dictionaries
dictFromModeTxt={'DEENt':'german-english','DEEOt':'german-esperanto', 'DEFRt':'german-french','DERUt':'german-russian',
                 'ENDEt':'english-german','ENEOt':'english-esperanto', 'ENFRt':'english-french','ENRUt':'english-russian',
                 'EODEt':'esperanto-german','EOENt':'esperanto-english', 'EOFRt':'esperanto-french', 'EORUt':'esperanto-russian',
                 'FRDEt':'french-german','FRENt':'french-english','FREOt':'french-esperanto', 'FRRUt':'french-russian',
                 'RUDEt':'russian-german','RUENt':'russian-english', 'RUEOt':'russian-esperanto', 'RUFRt':'russian-french'}
def loadEachDictTxt(dictname, filename):
    fin=open(filename+'.txt', encoding='utf-8')
    allDicts[dictname]={}
    for line in fin:
        line.strip()
        if '#' not in line:
            segments=line.split('\t')
            if len(segments)>1:
                for word in segments[0].split(';'):
                    word=word.strip()
                    if word.lower() not in allDicts[dictname]:
                        allDicts[dictname][word.lower()]=[]
                    for baseword in segments[0].split(';'):
                        allDicts[dictname][word.lower()].append(baseword.strip())
                    allDicts[dictname][word.lower()].append('#')
                    for transword in segments[1].split(';'):
                        allDicts[dictname][word.lower()].append(transword.strip())
                    allDicts[dictname][word.lower()].append('#')
                    if len(segments)>2:
                        for typeword in segments[2].split(';'):
                            allDicts[dictname][word.lower()].append(typeword.strip())
                    allDicts[dictname][word.lower()].append('###')
    fin.flush()
    fin.close()
def initialiser():
    for item in dictFromModeTxt:
        loadEachDictTxt(dictname=item, filename=dictFromModeTxt[item])
def searchWord(word, lang):
    word=word.lower()
    if lang=='German':
        return findWordPerDict(word, ['ENDEt', 'EODEt', 'FRDEt', 'RUDEt'])
    elif lang=='GBEnglish' or lang=='USEnglish':
        return findWordPerDict(word, ['DEENt','EOENt', 'FRENt', 'RUENt'])
    elif lang=='Esperanto':
        return findWordPerDict(word, ['DEEOt','ENEOt', 'FREOt', 'RUEOt'])
    elif lang == 'French':
        return findWordPerDict(word, ['DEFRt','ENFRt', 'EOFRt', 'RUFRt'])
    elif lang == 'Russian':
        return findWordPerDict(word, ['DERUt','ENRUt', 'EORUt', 'FRRUt'])
    
def findWordPerDict(word='', dictLst=()):
    word=word.lower()
    results=[]
    for dict in dictLst:
        if word in allDicts[dict]:
            results.append((word.upper(), dictFromModeTxt[dict].split('-')[0]+' -> '+dictFromModeTxt[dict].split('-')[1] ,"'"+dict+"'" ))
            i=0
            while i<len(allDicts[dict][word]):
                base=''
                trans=[]
                topic=''
                while allDicts[dict][word][i] !='#':
                    base+=allDicts[dict][word][i]+'; '
                    i+=1
                i+=1
                while allDicts[dict][word][i] !='#':
                    trans.append(allDicts[dict][word][i])
                    i+=1
                i+=1
                while allDicts[dict][word][i] !='###':
                    topic+=allDicts[dict][word][i]+';'
                    i+=1
                i+=1
                for j in range(len(trans)):
                    results.append((base, trans[j], topic))
    if len(results)>0:
        return results
    else:
        return [('WORD','NOT', 'FOUND')]
            

initialiser()
#print(allDicts['ENDEt']['word'])

#Obsolete code:
#loadDictsEsp()
#print(searchWord('flow', lang='French'))##test
'''ENFR={}
def loadDictsEsp():
    fin=open('english-french.txt')
    for line in fin:
        line.strip()
        if '#' not in line:
            segments=line.split('\t')
            if len(segments)>1:
                for word in segments[0].split(';'):
                    word=word.strip()
                    if word.lower() not in ENFR:
                        ENFR[word.lower()]=[]
                    for baseword in segments[0].split(';'):
                        ENFR[word.lower()].append(baseword.strip())
                    ENFR[word.lower()].append('#')
                    for transword in segments[1].split(';'):
                        ENFR[word.lower()].append(transword.strip())
                    ENFR[word.lower()].append('#')
                    if len(segments)>2:
                        for typeword in segments[2].split(';'):
                            ENFR[word.lower()].append(typeword.strip())
                    ENFR[word.lower()].append('###')'''#obsolete!!!!!!
'''if word in ENFR.keys():
            i=0
            results=[]
            while i<len(ENFR[word]):
                base=''
                trans=[]
                topic=''
                while ENFR[word][i] != '#':
                    base+=ENFR[word][i]+'; '
                    i+=1
                i+=1
                while ENFR[word][i] != '#':
                    trans.append(ENFR[word][i])
                    i+=1
                i+=1
                while ENFR[word][i] != '###':
                    topic+=ENFR[word][i]+'; '
                    i+=1
                i+=1
                for j in range(len(trans)):
                    results.append((base, trans[j], topic))
            if len(results)>0:
                return results'''