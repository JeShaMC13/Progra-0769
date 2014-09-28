#Mas sobre objetos

class particulaCompuesta(object):
    def __init__(self, name, setOfParticles): #Constructor
        self.name = name
        self.setOfParticles = setOfParticles

    def getMass(self):
        x = 0
        for i in self.setOfParticles:
            x += i.getMass()
        return x

    def getCharge(self):
        x = 0
        for i in self.setOfParticles:
            x += i.getCharge()
        return x

    def getSpin(self):
        x = 0
        for i in self.setOfParticles:
            x += i.getSpin()
        return x

    def getName(self):
        return self.name

    def setParticles(self, newParticles):
        self.setOfParticles = newParticles

    def getParticles(self):
        return self.setOfParticles

    def __str__(self):
        str2 = ''
        for i in self.getParticles():
            str2 += '\n'+i.getName()
        return "Particula: "+self.getName()+"\n"+\
               "Compuesta por: "+str2

class particulaFundamental(object):
    def __init__(self, name, charge, spin, mass): #Constructor
        self.name = name
        self.charge = charge
        self.spin = spin
        self.mass = mass

    def getName(self):
        return self.name

    def getCharge(self):
        return self.charge

    def getSpin(self):
        return self.spin

    def getMass(self):
        return self.mass

    def setName(self, newName):
        self.name = newName

    def setCharge(self, newCharge):
        self.charge = newCharge

    def setSpin(self, newSpin):
        self.spin = newSpin

    def setMass(self, newMass):
        self.mass = newMass
    
    def __str__(self):
        return str(self.getName())


def makeAntiParticle(fundamentalParticle):
    f = fundamentalParticle
    return(particulaFundamental("Anti"+f.getName(),-1.0*f.getCharge(),f.getSpin(),f.getMass()))

def makeProton():
    return particulaCompuesta("Proton", [up,up,down])

def makeNeutron():
    return particulaCompuesta("Neutron", [up,down,down])

def makeAntiProton():
    antiUP = makeAntiUP()
    antiDOWN = makeAntiDOWN()
    return particulaCompuesta("Antiproton", [antiUP,antiUP,antiDOWN])

def makeAntiUP():
    return makeAntiParticle(up)

def makeAntiDOWN():
    return makeAntiParticle(down)

def makePion():
    particles = []
    particles.append(up)
    particles.append(makeAntiParticle(down))
    return particulaCompuesta("Pion", particles)

def makeKaon():
    particles = []
    particles.append(strange)
    particles.append(makeAntiParticle(up))
    return particulaCompuesta("Kaon", particles)

up = particulaFundamental("Quark UP", 2.0/3.0, 1.0/2.0, 0.003)
down = particulaFundamental("Quark DOWN", -1.0/3.0, -1.0/2.0, 0.006)
charm = particulaFundamental("Quark CHARM", 2.0/3.0, 1.0/2.0, 1.3)
strange = particulaFundamental("Quark STRANGE", -1.0/3.0, -1.0/2.0, 0.1)
top = particulaFundamental("Quark TOP", 2.0/3.0, 1.0/2.0, 175)
bottom = particulaFundamental("Quark BOTTOM", -1.0/3.0, -1.0/2.0, 4.3)
