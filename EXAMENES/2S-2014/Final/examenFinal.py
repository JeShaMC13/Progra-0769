import random

class Dictionary(object):

    '''
    Everything related to the words being used
    along this game.
    '''

    FIELD_SYMBOL = '!'
    END_OF_LINE = 'EOL'
    NEW_FIELD = 'NFLD'
    SPACE     = '-'
    VALID_CHARACTERS = [chr(x) for x in range(65,91)]

    '''Static methods'''

    def __init__(self, fName = 'examenFinal.txt'):
        self.fName = fName

    def __str__(self):
        return str(self.parseFields(self.readFile()))

    def __repr__(self):
        return self.__str__()

    '''Public methods'''

    def readFile(self):
        data = []
        try:
            f = open(self.fName, 'r')
            for line in f:
                data.append(line.rstrip('\r\n'))
            return data
        except IOError:
            print "Archivo inexistente: " + self.fName
            exit()
  
    def parseFields(self, fileData):
        dic = {} #Dictionary
        currentField = None
        for line in fileData:
            fieldOrData = self.__checkFieldOrData(line)
            if fieldOrData == self.NEW_FIELD:
                currentField = line.lstrip(self.FIELD_SYMBOL).upper()
                dic[currentField] = []
            elif fieldOrData == self.END_OF_LINE:
                currentField = None
            elif fieldOrData == None: #If current line contains a single word
                if currentField:
                    ln = line.replace(' ', self.SPACE) #Replace spaces
                    dic[currentField].append(ln.upper()) #Convert to uppercase
        return dic

    def validCharacter(self, char):
        return char in self.VALID_CHARACTERS


    '''Private methods'''

    def __checkFieldOrData(self, line):
        if len(line):
            if self.FIELD_SYMBOL in line: #If a new field was found
                return self.NEW_FIELD
            else:
                return None #If a word that belongs to current field was found
        else:
            return self.END_OF_LINE #If there's anything on this line
                                    #it means field ends here


    
class Game(object):

	'''Game functionality implemented here'''

    '''CONSTANTS'''

    UNDERSCORE = '_'

    '''Static methods'''

    def __init__(self):
        self.Dict = Dictionary()
        self.wordsAndFields = self.Dict.parseFields(self.Dict.readFile())
        self.DASH = self.Dict.SPACE
        self.failedAttempts = 0

    '''Public methods'''

    def getCurrentField(self):
        return self.currentField

    def getFailedAttempts(self):
        return self.failedAttempts

    def getAvailableFields(self):
        return self.wordsAndFields.keys()

    def setDesiredField(self, field):
        self.currentField = field
        
    def setPlayerWord(self, field):
        currentWord = self.__chooseRandomWord(field)
        self.currentWord = []
        self.playerWord = []
        self.usedChars = []
        self.failedAttempts = 0
        for letter in currentWord:
            self.currentWord.append(letter)
            if letter == self.Dict.SPACE:
                self.playerWord.append('-')
            else:
                self.playerWord.append(self.UNDERSCORE)
        del currentWord
    
    def getUsedChars(self):
        return self.usedChars

    def getCharInWord(self, char): #Is this character taking part in the currentWord?
        return str(char).upper() in self.getCurrentWord()

    def addToUsedChars(self, char):
        char = str(char).upper()
        if self.__validateInputChar(char): #Is it a valid character?
            if char not in self.usedChars: #Hasn't it already been used before?
                self.usedChars.append(char)
                if not self.getCharInWord(char): #Doesn't it figure in the currentWord?
                    self.failedAttempts += 1
                self.fillUserWord()
                return char
            else:
                print 'Ya utilizo esta letra anteriormente'
        return None
                
    def fillUserWord(self): #Fill up players's word with used characters
        currentWord = self.getCurrentWord()
        player = self.getPlayerWord()
        for i in range(len(player)):
            if player[i] == self.UNDERSCORE:
                if currentWord[i] in self.getUsedChars():
                    self.__addPlayerLetter(currentWord[i], i)

    def getPlayerWord(self):
        return self.playerWord

    def getCurrentWord(self):
        return self.currentWord

    def getWon(self):
        return self.getPlayerWord() == self.getCurrentWord()

    def getLost(self, maxTries):
        return self.getFailedAttempts() >= maxTries

    '''Private methods'''
    
    def __chooseRandomWord(self, field):
        field = str(field).upper() #Make sure field is in uppercase
        try:
            N = len(self.wordsAndFields[field]) #Which field are we dealing with?
            x = random.randint(0, N - 1) #Choose randomly a word from a field
            word = self.wordsAndFields[field][x]
            return word
        except KeyError:
            return None

    def __validateInputChar(self, char):
        return self.Dict.validCharacter(char)

    def __copyList(self, source):
        dest = []
        for x in source:
            dest.append(x)
        return dest

    def __addPlayerLetter(self, letter, index):
        self.playerWord[index] = letter

class Interface(object):

	'''Interface between functionality and user'''

    '''CONSTANTS'''
    HUNG_MAN = (' '*3+'_'*5,' '*2+'|' ,' '+'0|', '/|\\', ' '+'|', '/ \\')
    FLOOR = ('_____')

    '''Static methods'''
    
    def __init__(self):
        self.game = Game()
        self.__showIntro()
        self.setDesiredField()
        self.setRandomWord(self.game.getCurrentField())
        while ((not self.game.getWon()) and (not self.__checkLost())):
            self.__showCurrentStatus()
        if self.__checkLost():
            self.__showLost()
        else:
            self.__showWon()

    def __str__(self):
        a = ''
        for i in self.HUNG_MAN:
            a += i + '\n'
        return a

    def __repr__(self):
        return self.__str__()

    '''Public methods'''
        
    def getDesiredField(self):
        x = 1
        available = self.game.getAvailableFields()
        N = len(available)
        for i in available:
            print str(x) + ') ' + i
            x += 1
        idx = self.__validateNumber('Seleccione una categoria: ', (1,N)) - 1
        return available[idx]

    def setDesiredField(self):
        self.game.setDesiredField(self.getDesiredField())

    def setRandomWord(self, field):
        self.game.setPlayerWord(field)


    '''Private methods'''
    def __showCurrentStatus(self):
        self.__showHungMan()
        self.__showCurrentField()
        self.__showPlayerWord()
        self.__showUsedChars()
        self.__showFailedAttempts()
        self.__inputCharacter()

    
    def __validateNumber(self, request, intRange):
        while True:
            x = raw_input(request)
            if x.isdigit():
                x = int(x)
                if x >= intRange[0] and x <= intRange[1]:
                    break
        return x

    def __validateChar(self, request, length):
        while True:
            c = raw_input(request)
            if len(c) == length:
                break
        return c

    def __showIntro(self):
        print 'Ahorcado!'

    def __showHungMan(self, previousSpaces = 12):
        print '\n'*previousSpaces
        N = len(self.HUNG_MAN)
        failed = self.game.getFailedAttempts()
        for i in range(failed):
            print self.HUNG_MAN[i]

        for _ in range(N - failed):
            print ' '

        print self.FLOOR
        print '\n'*2

    def __showCurrentField(self):
        fld = self.game.getCurrentField()
        print '\n'*1 + 'Categoria: ' + fld + '\n'

    def __showPlayerWord(self):
        for x in self.game.getPlayerWord():
            print str(x),
        #print [_ for _ in self.game.getPlayerWord()],
        print '\n'*2

    def __showCurrentWord(self):
        for x in self.game.getCurrentWord():
            print str(x),

    def __showUsedChars(self):
        print 'Caracteres utilizados: '
        car = self.game.getUsedChars()
        if len(car):
            for x in self.game.getUsedChars():
                print str(x) + ' ',
        else:
            print 'NINGUNO'
        print '\n'*1

    def __checkLost(self):
        return self.game.getLost(len(self.HUNG_MAN))

    def __inputCharacter(self):
        c = self.__validateChar('Ingrese caracter: ', 1)
        self.game.addToUsedChars(c)

    def __showFailedAttempts(self):
        print 'Intentos fallidos: ' + str(self.game.getFailedAttempts()) + '/' + str(len(self.HUNG_MAN))
        
    def __showWon(self):
        print '\n'*3
        print '-'*6 + 'GANASTE' + '-'*6
        print ' '
        print 'La palabra era:   ',
        self.__showCurrentWord()

    def __showLost(self):
        self.__showHungMan(2)
        print '-'*6 + 'AHORCADO - PERDISTE' + '-'*6
        print ' '
        print 'La palabra era:   ',
        self.__showCurrentWord()

if __name__ == '__main__':
    Interface()
