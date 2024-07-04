import numpy as np
import cv2 as cv
import os

width = 120 # 120 Default # 150 Optimal
height = 32 # 32 Default # 40 Optimal
cap = cv.VideoCapture("C:\\Path\\To\\Video\\Goes\\Here")
gradient = '- : _ , ^ = ; > < + ! r c * / z ? s L T v ) J 7 ( | F i f I 3 1 t l u [ n e o Z 5 Y x j y a ] 2 E S w q k P 6 h 9 d 4 V p O G b U A K X H m 8 R D # $ B g 0 M N W Q % & @'.split(' ')
cmd = (f'mode {width},{height}')
os.system(cmd)


def rescale(frame, height, width):
    return(cv.resize(frame, (height, width)))

def determineSymbol(x):
    value = round(x/3)
    if value < len(gradient):
        return gradient[value]
    else:
        return '@'

def processVideo():
    symbols = []
    pixels = []
    while True:
        ret, frame = cap.read()
        if not ret:
            print('Animation Finished. Quitting...')
            break
        else:
            screen = ([[' ' for x in range(width)] for x in range(height)])
            frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            frame = rescale(frame, width, height)
            for x in range(len(frame)):
                for y in range(len(frame[x])):
                    if frame[x][y] > 5:
                        pixels.append([x,y])
                        symbols.append(determineSymbol(frame[x][y]))

            for x in range(len(pixels)):
                screen[pixels[x][0]][pixels[x][1]] = symbols[x]
            for x in screen:
                print(''.join(x))
            pixels.clear()
            symbols.clear()
            if cv.waitKey(1) == ord('q'):
                break
    cap.release()
    cv.destroyAllWindows()

processVideo()

# py E:\Dev\VideoToASCII\main.py
