import pygame
import time

def getJoystick():
    #NAME = ["4Axis 12Button USB Vibration Gamepad", " Device V.:MOTE"]
    NAME = ["4Axis 12Button USB Vibration Gamepad", "4-Axis,12-Button with POV","USB, 3-axis, 4-button joystick", "Logitech Extreme 3D Pro USB"]

    pygame.init()

    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

    joy = pygame.joystick
    idx = 0
    found = False

    while not found:
        print "Buscando joystick compatible..."
        #found = True
        for item in range(joy.get_count()):
            if joy.Joystick(item).get_name() in NAME:
                idx = joy.Joystick(item).get_id()
                found = True
                break
        time.sleep(1)
    gamePad = joy.Joystick(idx)
    return gamePad

def getPositions(gPad):
    pygame.event.pump()
    out = []
    for i in range(gPad.get_numaxes()):
        out.append(int(gPad.get_axis(i)*100)/100.0)
    for i in range(gPad.get_numbuttons()):
        out.append(gPad.get_button(i))
    return out


gpad = getJoystick()
print "Se encontro: " + str(gpad.get_name())
print "Enumerado como Joystick #" + str(gpad.get_id())

gpad.init()
print "Numero de ejes: " + str(gpad.get_numaxes())

try:
    while True:
        dt = getPositions(gpad)
        print dt
        #print "(" + str(gpad.get_axis(0)) + "," + str(gpad.get_axis(1)) + ")"
        time.sleep(0.2)
except KeyboardInterrupt:
    print "\nAdios"

