'''
El juego del cronometro en Python 3.3.2 consta de 3 botones, start que sirve para iniciar la cuenta del
cronometro, stop para detener el cronometro y reset para reiniciar el juego.
El objetivo es detener el cronometro con la ayuda del boton stop justamente cuando el primer
digito de la derecha en color blanco este en cero, cuando esto suceda abremos acertado y el
contador incrementara el cual es el marcador de color verde.

Stopwatch: The Game
Created by: Jassael Ruiz
Version: 1.0
'''

import sys
sys.path.append("..")
import simplegui as sg

# define global variables
A = 0
B = 0
C = 0
tenths_seconds = 0
total_stops = 0
successful_stops = 0
score = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.tenths_seconds
def format(t):
    global A, B, C
    tenths_seconds = 0
    tenths_seconds = t % 10
    C = t // 10
    if(C >= 60):
        A = C // 60
        C = C % 60
    if(C < 10):
        return str(A)+":"+str(B)+str(C)+"."+str(tenths_seconds)
    else:
        return str(A)+":"+str(C)+"."+str(tenths_seconds)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global score
    timer.start()
    score = True

def stop_handler():
    global total_stops, score, tenths_seconds, successful_stops
    timer.stop()
    if(score):
        total_stops += 1
        seconds = tenths_seconds % 10
        if(seconds == 0):
            successful_stops += 1
    score = False

def reset_handler():
    global tenths_seconds, A, B, C, total_stops, successful_stops
    A = 0
    B = 0
    C = 0
    tenths_seconds = 0
    total_stops = 0
    successful_stops = 0
    label.set_text("tenths_seconds:\n"+str(tenths_seconds))
    timer.stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global tenths_seconds
    tenths_seconds += 1
    label.set_text("tenths_seconds:\n"+str(tenths_seconds))

# define draw handler
def draw(canvas):
    canvas.draw_text(format(tenths_seconds), [100, 170], 40, "white")
    canvas.draw_text(str(successful_stops)+"/"+str(total_stops), [230, 40], 20,"green")

def input_handler(t):
    global tenths_seconds
    tenths_seconds = int(t)
    label.set_text("tenths_seconds:\n"+str(tenths_seconds))
    
# create frame
frame = sg.create_frame("StopWatch!", 300, 300)

# register event handlers
frame.set_draw_handler(draw)
timer = sg.create_timer(100, timer_handler)
start_button = frame.add_button("Start", start_handler, 50)
stop_button = frame.add_button("Stop", stop_handler, 50)
reset_button = frame.add_button("Reset", reset_handler, 50)
frame.add_input("tenths", input_handler, 50)
label = frame.add_label("tenths_seconds:\n"+str(tenths_seconds))
# start frame
frame.start()
