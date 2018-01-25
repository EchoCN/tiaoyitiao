import os
import PIL,numpy
import matplotlib.pyplot as plt
import matplotlib.animation
import matplotlib.animation


def get_screen_image():
    os.system('adb shell screencap -p /sdcard/screen.png')
    os.system('adb pull /sdcard/screen.png')
    return numpy.array(PIL.Image.open('screen.png'))

def jump_to_next(point1,point2):
    x1,y1 = point1;x2,y2 = point2
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    os.system('adb shell input swipe 320 410 320 410 {}'.format(int(distance*1.35)))

def on_click(event,coor=[]):
    coor.append((event.xdata,event.ydata))
    if len(coor) == 2:
        jump_to_next(coor.pop(),coor.pop())



figure = plt.figure()
axes_image = plt.imshow(get_screen_image(),animated=True)
figure.canvas.mpl_connect('button_press_event', on_click)
plt.show()