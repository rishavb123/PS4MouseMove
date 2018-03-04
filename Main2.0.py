from pynput.mouse import Button, Controller
import pygame

pygame.init()
pygame.joystick.init()
controller = pygame.joystick.Joystick(0)
controller.init()
mouse = Controller()



changeX = 0
changeY = 0

six = False
seven = False

end = False
exit = False

side = 0
updown = 0

while True:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYHATMOTION:
                side = -event.value[0]
                updown = event.value[1]
            if event.type == pygame.JOYAXISMOTION:
                if(event.axis==0):
                    changeX = int(event.value*1.5)
                elif(event.axis==1):
                    changeY = int(event.value*1.5)
                elif(event.axis==2):
                    changeX = int(event.value*3)
                elif(event.axis==3):
                    changeY = int(event.value*3)
            if event.type == pygame.JOYBUTTONDOWN:

                if(event.button==12):
                    exit = True
                    break
                elif event.button == 6:
                    six = True
                elif event.button == 7:
                    seven = True
                elif event.button == 10:
                    mouse.press(Button.left)
                elif event.button == 11:
                    mouse.press(Button.right)
                else:
                    mouse.press(Button.left)
            if event.type == pygame.JOYBUTTONUP:
                if event.button == 6:
                    six = False
                elif event.button == 7:
                    seven = False
                elif event.button == 10:
                    mouse.release(Button.left)
                elif event.button == 11:
                    mouse.release(Button.right)
                else:
                    mouse.release(Button.left)
        if(exit):
            exit = False
            break
        mouse.scroll(side,updown)
        if(six and seven):
            end = True
            break
        mouse.move(changeX, changeY)
        if(mouse.position[0]<10):
            mouse.position=(2550,mouse.position[1])
        if(mouse.position[1]<10):
            mouse.position=(mouse.position[0],790)
        if(mouse.position[0]>2550):
            mouse.position=(10,mouse.position[1])
        if(mouse.position[1]>790):
            mouse.position=(mouse.position[0],10)
    if end:
        break
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 12:
                    exit = True
                    break
                if event.button == 6:
                    six = True
                if event.button == 7:
                    seven = True
            if event.type == pygame.JOYBUTTONUP:
                if event.button == 6:
                    six = False
                if event.button == 7:
                    seven = False
        if(exit):
            exit=False
            break
        if (six and seven):
            end = True
            break
    if end:
        break
