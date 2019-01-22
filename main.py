'''Created on 17 Aug 2011 @author: Matthew'''
#encoding: utf-8
from tkinter import *
import DictManager
import string
import tkinter.messagebox as tkMessageBox
import tkinter.filedialog as tkFileDialog
#TODO: Add accenter, FR list for making accents when letter followed by ~ (or '/"/^+~ for alt in FR)
#############Globals##############
Mode='GBEnglish'
BackupTimer=5 #spaces
charRow=[]
EsperantoChar=[['Cx', '\u0108'],['CX', '\u0108'], ['cx', '\u0109'], ['cX', '\u0109'], 
               ['Gx', '\u011C'],['GX', '\u011C'], ['gx', '\u011D'], ['gX', '\u011D'],
               ['Hx', '\u0124'],['HX', '\u0124'], ['hx', '\u0125'], ['hX', '\u0125'],
               ['Jx', '\u0134'],['JX', '\u0134'], ['jx', '\u0135'], ['jX', '\u0135'],
               ['Sx', '\u015C'],['SX', '\u015C'], ['sx', '\u015D'], ['sX', '\u015D'],
               ['Ux', '\u016C'],['UX', '\u016C'], ['ux', '\u016D'], ['uX', '\u016D']]
EsperantoButtons=[]
EsperantoLabels=[]
RussianChar=[['~', '\u0301'], ['~', '\u0301'], ['A', '\u0410'],['a', '\u0430'], ['B', '\u0411'],['b', '\u0431'], ['V', '\u0412'],['v', '\u0432'], 
             ['G', '\u0413'],['g', '\u0433'], ['D', '\u0414'],['d', '\u0434'], ['E', '\u0415'],['e', '\u0435'],
             ['xE', '\u0401'],['xe', '\u0451'], ['xZ', '\u0416'],['xz', '\u0436'], ['Z', '\u0417'],['z', '\u0437'], 
             ['I', '\u0418'],['i', '\u0438'], ['J', '\u0419'],['j', '\u0439'], ['K', '\u041A'],['k', '\u043A'], 
             ['L', '\u041B'],['l', '\u043B'], ['M', '\u041C'],['m', '\u043C'], ['N', '\u041D'],['n', '\u043D'], 
             ['O', '\u041E'],['o', '\u043E'], ['P', '\u041F'],['p', '\u043F'], ['R', '\u0420'],['r', '\u0440'], 
             ['S', '\u0421'],['s', '\u0441'], ['T', '\u0422'],['t', '\u0442'], ['U', '\u0423'],['u', '\u0443'], 
             ['F', '\u0424'],['f', '\u0444'], ['H', '\u0425'],['h', '\u0445'], ['C', '\u0426'],['c', '\u0446'], 
             ['xC', '\u0427'],['xc', '\u0447'], ['xS', '\u0428'],['xs', '\u0448'], ['XS', '\u0429'],['Xs', '\u0449'], 
             ['X"', '\u042A'],['x"', '\u044A'], ['Y', '\u042B'],['y', '\u044B'], ["X'", '\u042C'],["x'", '\u044C'], 
             ['€', '\u042D'],['£', '\u044D'], ['xU', '\u042E'],['xu', '\u044E'], ['xA', '\u042F'],['xa', '\u044F']]
            #X notation above is not ideal, in fact it is confusing, esp with caps and non caps
RussianButtons=[]
RussianLabels=[]
RussianCharOrder=[64,65,66,67,14,15,54,55,52,53,50,51,0,1,2,3,4,5,6,7,8,9,10,11,12,13,16,17,18,19,20,21,23,24,25,26,27,
                  28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,56,57,58,59,60,61,62,63]
FrenchChar=[['<<', '\u00AB'], ['>>', '\u00BB'], ['A~','À'],['a~','à'], ['A^','Â'],['a^','â'], ["E'~",'É'],["e'~",'é'], 
            ['E~','È'],['e~','è'], ['I"~','Ï'],['i"~','ï'], ['I^','Î'],['i^','î'], ['O^','Ô'],['o^','ô'], 
            ['U~','Ù'],['u~','ù'], ["'~",'\u00B0'],['','']]
FrenchConv=[['!',' !'], ['?',' ?'], [':',' :']]
FrenchButtons=[]
FrenchLabels=[]
Flags=[]
GBEnglish={}
USEnglish={}
GermanChar=[['A~', '\u00C4'], ['a~','\u00E4'], ['O~','\u00D6'], ['o~', '\u00F6'],
             ['U~', '\u00DC'], ['u~','\u00FC'], ['ss~', '\u00DF'], ["'~",'\u00B0'],
             ['"~', '“'],['~"', '”'], [',,', '„'],['s~', '§'], ['<<', '\u00AB'],['>>', '\u00BB']]
GermanButtons=[]
GermanLabels=[]
TranslitStartPoint='0.0'
#############Classes###�###########
class Callable(object):
    def __init__(self, func, *args, **kwds):
        self.func = func
        self.args = args
        self.kwds = kwds

    def __call__(self, *args, **kwds):
        d = dict(self.kwds)
        d.update(kwds)
        return self.func(*self.args+args, **d)

    def __str__(self):
        return self.func.__name__

#############Functions############
def backuper(dump='normal'):
    global BackupTimer
    mainText.edit_separator()
    if BackupTimer==10 or dump=='invokeSave':
        backupLabel.config(text='Saving...'+' '*218)
        f=open('text.bak', mode='w', encoding='utf-8')
        f.write(mainText.get(0.0, END))
        f.flush
        f.close
        BackupTimer=0
        backupLabel.config(text='Text backed-up'+' '*218)
    else:
        BackupTimer+=1
        backupLabel.config(text=' '*246)
def binder(mode='setup'):
    if mode=='setup':
        for i in range(4):
            if i!=0:
                mainText.bind('<F'+str(i)+'>', Callable(focuser, i))
                DictSearch.bind('<F'+str(i)+'>', Callable(focuser, i))
                DictResults.bind('<F'+str(i)+'>', Callable(focuser, i))
        if open('text.bak', encoding='utf-8'):
            fin=open('text.bak', encoding='utf-8')
            for line in fin:
                mainText.insert(0.0, line.strip('EOF'))
def breakInserter(*options):
    global TranslitStartPoint
    TranslitStartPoint=mainText.index(INSERT)
    insertBreak.flash()
def chMode(newMode='Esperanto'):
    destroyCharButtons()
    global Mode
    Mode=newMode
    createCharButtons()
    for i in range(6):
        Flags[i].config(state=NORMAL)
    if Mode=='German':
        DictLabel.config(text='Wörterbuch')
        DictSearchButton.config(text='Entdecken')
        Flags[0].config(state=DISABLED)
    elif Mode=='GBEnglish':
        #flagSpan(2)
        DictLabel.config(text='Dictionary')
        DictSearchButton.config(text='Search')
        Flags[1].config(state=DISABLED)
    elif Mode=='USEnglish':
        #flagSpan(2)
        DictLabel.config(text='Dictionary')
        DictSearchButton.config(text='Search')
        Flags[2].config(state=DISABLED)
    elif Mode=='Esperanto':
        #flagSpan(2)
        DictLabel.config(text='Vortaro')
        DictSearchButton.config(text='Ser'+'\u0109'+'i')
        Flags[3].config(state=DISABLED)
    elif Mode=='French':
        #flagSpan(2)#May need adjustment eventually
        DictLabel.config(text='Dictionaire')
        DictSearchButton.config(text='Chercher')
        Flags[4].config(state=DISABLED)
    elif Mode=='Russian':
        #flagSpan(2)
        DictLabel.config(text='Словарь')
        DictSearchButton.config(text='Узнавать')
        Flags[5].config(state=DISABLED)
def createCharButtons():
    if Mode=='German':
        i=0
        while i < len(GermanChar):
            GermanButtons.append(Button(Master, text=GermanChar[i][1], command=Callable(insertChar, GermanChar[i][1])))
            GermanButtons.append(Button(Master, text=GermanChar[i+1][1], command=Callable(insertChar, GermanChar[i+1][1])))
            GermanLabels.append(Label(Master, text=GermanChar[i][0]+'/'+GermanChar[i+1][0]))
            GermanButtons[i].grid(row=4, column=i//2+6, columnspan=1, sticky=E+W)
            GermanButtons[i+1].grid(row=5, column=i//2+6, columnspan=1, sticky=E+W)
            GermanLabels[i//2].grid(row=6, column=i//2+6, columnspan=1, sticky=E+W)
            i+=2
        for i in range(len(GermanLabels)):
            if i%2==0:
                GermanButtons[2*i].config(fg='blue')
                GermanButtons[2*i+1].config(fg='blue')
                GermanLabels[i].config(fg='blue', width=3)
            else:
                GermanButtons[2*i].config(fg='navy blue')
                GermanButtons[2*i+1].config(fg='navy blue')
                GermanLabels[i].config(fg='navy blue', width=3)
    if Mode=='Esperanto':
        i=0
        for item, item2 in EsperantoChar[0:-1:2]:
            EsperantoButtons.append(Button(Master, text=item2, command=Callable(insertChar, item2)))
            EsperantoLabels.append(Label(Master, text=item+'/'+EsperantoChar[i*2+1][0]))
            EsperantoButtons[i].grid(row=4, column=i+5, columnspan=1, sticky=E+W)
            EsperantoLabels[i].grid(row=5, column=i+5, columnspan=1, sticky=E+W)
            i+=1
        for i in range(len(EsperantoLabels)):
            if i%2==0:
                EsperantoButtons[i].config(fg='blue')
                EsperantoLabels[i].config(fg='blue', width=3)
            else:
                EsperantoButtons[i].config(fg='navy blue')
                EsperantoLabels[i].config(fg='navy blue', width=3)
    if Mode=='French':
        i=0
        while i < len(FrenchChar):
            FrenchButtons.append(Button(Master, text=FrenchChar[i][1], command=Callable(insertChar, FrenchChar[i][1])))
            FrenchButtons.append(Button(Master, text=FrenchChar[i+1][1], command=Callable(insertChar, FrenchChar[i+1][1])))
            FrenchLabels.append(Label(Master, text=FrenchChar[i][0]+'/'+FrenchChar[i+1][0]))
            FrenchButtons[i].grid(row=4, column=i//2+6, columnspan=1, sticky=E+W)
            FrenchButtons[i+1].grid(row=5, column=i//2+6, columnspan=1, sticky=E+W)
            FrenchLabels[i//2].grid(row=6, column=i//2+6, columnspan=1, sticky=E+W)
            i+=2
        for i in range(len(FrenchLabels)):
            if i%2==0:
                FrenchButtons[2*i].config(fg='blue')
                FrenchButtons[2*i+1].config(fg='blue')
                FrenchLabels[i].config(fg='blue', width=3)
            else:
                FrenchButtons[2*i].config(fg='navy blue')
                FrenchButtons[2*i+1].config(fg='navy blue')
                FrenchLabels[i].config(fg='navy blue', width=3)
    if Mode=='Russian':
        for j in range(2):
            for i in range(17):
                i+=1
                RussianButtons.append(Button(Master, text=RussianChar[(i-1)*2+(j*34)][1], command=Callable(insertChar,RussianChar[(i-1)*2+(j*34)][1])))
                RussianButtons.append(Button(Master, text=RussianChar[-1+i*2+(j*34)][1], command=Callable(insertChar,RussianChar[-1+i*2+(j*34)][1])))
                RussianLabels.append(Label(Master, text=RussianChar[(i-1)*2+(j*34)][0]+'/'+RussianChar[-1+i*2+(j*34)][0]))
                RussianButtons[(i-1)*2+(j*34)].grid(row=(4+j*3), column=i+2, sticky=E+W)
                RussianButtons[-1+i*2+(j*34)].grid(row=5+j*3, column=i+2, sticky=E+W)
                RussianLabels[-1+i+(j*17)].grid(row=6+j*3, column=i+2, sticky=E+W)
        RussianButtons.append(Button(Master, text=FrenchChar[0][1], command=Callable(insertChar, FrenchChar[0][1]),width=3))
        RussianButtons.append(Button(Master, text=FrenchChar[1][1], command=Callable(insertChar, FrenchChar[1][1]),width=3))
        FrenchLabels.append(Label(Master, text=FrenchChar[0][0]+'/'+FrenchChar[1][0], width=3))
        RussianButtons[-2].grid(row=7, column=21, sticky=E+W)
        RussianButtons[-1].grid(row=8, column=21, sticky=E+W)
        FrenchLabels[-1].grid(row=9, column=21, sticky=E+W)
        FrenchLabels[-1].config(fg='navy blue')
        for i in range(len(RussianLabels)):
            if i%2==0:
                RussianLabels[i].config(fg='blue')
            else:
                RussianLabels[i].config(fg='navy blue')
        for i in range(len(RussianButtons)//2):
            if i%2==0:
                RussianButtons[i*2+1].config(fg='blue')
                RussianButtons[i*2].config(fg='blue')
            else:
                RussianButtons[i*2+1].config(fg='navy blue')
                RussianButtons[i*2].config(fg='navy blue')
def destroyCharButtons():
    if Mode=='German':
        for i in range(len(GermanButtons)):
            GermanButtons[0].destroy()
            GermanButtons.pop(0*i) #empties lists
        for i in range(len(GermanLabels)):
            GermanLabels[0].destroy()
            GermanLabels.pop(0*i) #*i is just so it won't warm me of unused i
    if Mode=='Esperanto':
        for i in range(len(EsperantoButtons)):
            EsperantoButtons[0].destroy()
            EsperantoButtons.pop(0*i) #empties lists
        for i in range(len(EsperantoLabels)):
            EsperantoLabels[0].destroy()
            EsperantoLabels.pop(0*i) #*i is just so it won't warm me of unused i
    if Mode=='French':
        for i in range(len(FrenchButtons)):
            FrenchButtons[0].destroy()
            FrenchButtons.pop(0*i) #empties lists
        for i in range(len(FrenchLabels)):
            FrenchLabels[0].destroy()
            FrenchLabels.pop(0*i) #*i is just so it won't warm me of unused i
    if Mode=='Russian':
        for i in range(len(RussianButtons)):
            RussianButtons[0].destroy()
            RussianButtons.pop(0*i) #empties lists
        for i in range(len(RussianLabels)):
            RussianLabels[0].destroy()
            RussianLabels.pop(0*i) #*i is just so it won't warm me of unused i
        for i in range(len(FrenchLabels)):
            FrenchLabels[0].destroy()
            FrenchLabels.pop(0*i) #*i is just so it won't warm me of unused i
def editChange(*options, Type=None):
    if Type=='undo':
        mainText.edit_undo()
        mainText.edit_undo()
    elif Type=='redo':
        mainText.edit_redo()
        mainText.edit_redo()
def fileManager(*options, action='save'):
    fileTypeList=[('All Files', '.*'), ('TransL backup files', '.bak'),('Plain Text', '.txt')]
    if action=='load':
        backuper(dump='invokeSave')
        file=tkFileDialog.askopenfilename(defaultextension='.txt', filetypes=fileTypeList, title='Open... - TransL')
        if file[-5:-1]=='.txt' or '.bak':
            fin=open(file, encoding='utf-8')
            replace= False
            if len(mainText.get(0.0, END))>=5:
                replace=tkMessageBox.askquestion(title='Replace Open Text?', message='Are you sure you want to open: \n'+file+'\n and replace any open text?')
            if replace=='yes' or len(mainText.get(0.0, END))<5:
                mainText.delete(0.0, END)
                mainText.insert(INSERT, fin.read())
                backupLabel.config(text='File Opened: '+file+' '*(230-len(file)*2))
    elif action=='save':
        file=tkFileDialog.asksaveasfilename(defaultextension='.txt', filetypes=fileTypeList, title='Save as... - TransL')
        fout=open(file, mode='w', encoding='utf-8')
        fout.write(mainText.get(0.0, END))
        fout.flush()
        fout.close()
        backupLabel.config(text='File Saved: '+file+' '*(230-len(file)*2))
def flagSpan(span=3):
    for i in range(len(Flags)):
        Flags[i].grid(column=i*span+2, row=0, columnspan=span)
def focuser(*func):
    if func[0]==1:
        mainText.focus_set()
    if func[0]==2:
        DictSearch.focus_set()
    if func[0]==3:
        DictResults.focus_set()
def displayHelp(*options):
    tkMessageBox.showinfo(title='About TransL', message='TransL by Matthew \n Version 0.3 (Alpha) \nOpen Readme.txt in current directory for detailed help.')
def insertChar(Char):
    mainText.insert('insert', Char)
def insertDictResult(*options):
    if DictResults.curselection():
        mainText.insert('insert', DictResults.get(DictResults.curselection()))
    transleterateText()
    mainText.focus_set()
def loadEnglishTypes():
    fin=open('english-types.txt', encoding='utf-8')
    for line in fin:
        line=line.strip()
        if '#' not in line and '*' not in line.split()[0]:
            GBEnglish[line.split()[0]]=line.split()[1].replace('*', '')
        if '#' not in line and '*' not in line.split()[1]:
            USEnglish[line.split()[1].replace('*', '')]=line.split()[0]
def searchTranslation(word=''):
    DictSearchButton.flash()
    if DictSearchTerm.get()!='':
        resultsList=DictManager.searchWord(word=DictSearchTerm.get(), lang=Mode)
        print(resultsList)
        if resultsList!=None:
            DictResultsIn.delete(0, END)
            DictResults.delete(0, END)
            DictResultsTopic.delete(0, END)
            for item in resultsList:
                DictResultsIn.insert(END, str(item[0]))
                DictResults.insert(END, str(item[1]))
                if len(item)>2:
                    DictResultsTopic.insert(END, str(item[2]))
        DictSearchButton.flash()
def transleterateText(*options):
    if inhibitTranslitCtrl.get()==0:
        textStr=mainText.get(TranslitStartPoint, END)
        here=mainText.index(INSERT)
        if Mode=='USEnglish':
            for item in USEnglish:
                textStr=textStr.replace(item.lower(), USEnglish[item].lower())
                textStr=textStr.replace(item.upper(), USEnglish[item].upper())
                textStr=textStr.replace(item.title(), USEnglish[item].title())
        elif Mode=='GBEnglish':
            for item in GBEnglish:
                textStr=textStr.replace(item.lower(), GBEnglish[item].lower())
                textStr=textStr.replace(item.upper(), GBEnglish[item].upper())
                textStr=textStr.replace(item.title(), GBEnglish[item].title())
        elif Mode=='French':
            for item in FrenchChar:
                textStr=textStr.replace(item[0], item[1])
            i=1
            while i<(len(textStr)-1):
                i+=1
                for item in FrenchConv:
                    if textStr[i]==item[0] and textStr[i-1] not in '!?: ':
                        textStr=textStr[0:i]+item[1]+textStr[i+1:]
        elif Mode=='Esperanto':
            for item in EsperantoChar:
                textStr=textStr.replace(item[0], item[1])
        elif Mode=='German':
            for item in GermanChar:
                textStr=textStr.replace(item[0], item[1])
        elif Mode=='Russian':
            for i in range(len(RussianCharOrder)):
                textStr=textStr.replace(RussianChar[RussianCharOrder[i]][0], RussianChar[RussianCharOrder[i]][1])
        diff=0
        if here!=mainText.index('end -1 chars'):
            diff=len(mainText.get(TranslitStartPoint, END))-len(textStr)
            print(here+':'+mainText.index('end -1 chars'))
        mainText.delete(TranslitStartPoint, TranslitStartPoint+' + ' +str(len(mainText.get(TranslitStartPoint,'end')))+' chars')
        mainText.insert(TranslitStartPoint, textStr)
        mainText.delete(TranslitStartPoint +'+'+str(len(textStr[0:-1]))+' chars', END)
        mainText.mark_set('insert', here+' -'+str(diff)+' chars') #TODO: there seems to be a problem where the cursor moves back a place then there is a replacement at the end of a line which is not the last line
        mainText.see('insert')
#############Layout#############
Master=Tk()
flagImgs={"DE":PhotoImage(file='de.gif'),"GB":PhotoImage(file='gb.gif'),"US":PhotoImage(file='us.gif'),
          "EO":PhotoImage(file='eo.gif'),"FR": PhotoImage(file='fr.gif'), "RU":PhotoImage(file='ru.gif')}
#Left hand side
Label(Master, text='Mode:').grid(column=0, row=0, columnspan=2, sticky=E+W)
Flags.append(Button(Master, compound=RIGHT, text=' DE  ', image=flagImgs['DE'],command=Callable(chMode, 'German'), width=104))
Flags.append(Button(Master, compound=RIGHT, text=' GB  ', image=flagImgs['GB'],command=Callable(chMode, 'GBEnglish'), width=104, state=DISABLED))
Flags.append(Button(Master, compound=RIGHT, text=' US  ', image=flagImgs['US'],command=Callable(chMode, 'USEnglish'), width=104))
Flags.append(Button(Master, compound=RIGHT, text=' EO  ', image=flagImgs['EO'],command=Callable(chMode, 'Esperanto'), width=104))
Flags.append(Button(Master, compound=RIGHT, text=' FR  ', image=flagImgs['FR'],command=Callable(chMode, 'French'), width=104))
Flags.append(Button(Master, compound=RIGHT, text=' RU  ', image=flagImgs['RU'],command=Callable(chMode, 'Russian'), width=104))
flagSpan()
helper=Button(Master, text='About', command= displayHelp)
helper.grid(column=20, columnspan=2, row=0, sticky=E+W)
mainTextYScroll=Scrollbar(Master)
mainTextYScroll.grid(row=1, column=22, rowspan=3, sticky=N+S+W)
mainText=Text(Master, yscrollcommand=mainTextYScroll.set, maxundo=-1, undo=True)
for letter in string.ascii_letters[1]+string.ascii_letters[3:24]+string.ascii_letters[26:]:
    mainText.bind('<KeyRelease - '+letter+'>', transleterateText)
mainText.bind('<space>', Callable(backuper))
mainText.bind('<Control-z>', Callable(editChange, Type='undo'))
mainText.bind('<Control-y>', Callable(editChange, Type='redo'))
mainText.grid(row=1,column=0, columnspan=22, rowspan=3)
mainTextYScroll.config(command=mainText.yview)
backupLabel=Label(Master, text='Ready'+' '*235, width=105)
backupLabel.grid(row=12, column=0, columnspan=22, sticky=E+W)
#Right hand side
DictSearchTerm=StringVar()
DictLabel=Label(Master, text='Vortaro')
DictLabel.grid(column=22, row=0, columnspan=3)
DictSearch=Entry(Master, textvariable=DictSearchTerm)
#DictSearch.bind('<Button-1>', Callable(focuser, 'ClickOnSearch'))
DictSearch.grid(column=23, row=1, rowspan=1, columnspan=2, sticky=N+E+W)
DictSearch.bind('<Return>', searchTranslation)
DictSearchButton=Button(Master, command=Callable(searchTranslation), text='Ser'+'\u0109'+'i', activebackground='grey')
DictSearchButton.grid(row=1, column=25, sticky=N+E+W)
##Dictionary Results##
DictResultsYScroll=Scrollbar(Master)
DictResultsYScroll.grid(column=26, row=1, sticky=N+S+W)

DictResultsInXScroll=Scrollbar(Master)
DictResultsInXScroll.grid(column=23, row=1, sticky=E+S+W)
DictResultsIn=Listbox(Master, activestyle='none', height=12, xscrollcommand=DictResultsInXScroll.set, yscrollcommand=DictResultsYScroll.set)
DictResultsIn.grid(column=23, row=1, rowspan=1, columnspan=1, sticky=None)
DictResultsInXScroll.config(command=DictResultsIn.xview, orient=HORIZONTAL)

DictResults=Listbox(Master, activestyle='dotbox', height=12, yscrollcommand=DictResultsYScroll.set)
DictResults.grid(column=24, row=1, rowspan=1, columnspan=1, sticky=None)
DictResults.bind('<Return>', insertDictResult)
DictResults.bind('<Double-Button-1>', insertDictResult)
DictResultsTopic=Listbox(Master, activestyle='none', height=12, yscrollcommand=DictResultsYScroll.set)
DictResultsTopic.grid(column=25, row=1, rowspan=1, columnspan=1, sticky=None)

DictResultsYScroll.config(command=DictResultsIn.yview and DictResults.yview and DictResultsTopic.yview) #doesn't work. Google it
loadFileBut=Button(Master, text='Open', command=Callable(fileManager, action='load'))
saveFileBut=Button(Master, text='Save', command=Callable(fileManager, action='save'))
loadFileBut.grid(column=23, row=11, sticky=E+W)
saveFileBut.grid(column=24, row=11, sticky=E+W)
insertBreak=Button(Master, text='Insert | Break', command=Callable(breakInserter))
insertBreak.grid(column=23, row=10, sticky=E+S+W)
inhibitTranslitCtrl=IntVar()
inhibitTranslit=Checkbutton(Master,text='Stop Transliteration', variable=inhibitTranslitCtrl)
inhibitTranslit.grid(column=24, row= 10, sticky=E+S+W)
#############Start up sequence ###
binder()
createCharButtons()
focuser(1)
loadEnglishTypes()
Master.mainloop()