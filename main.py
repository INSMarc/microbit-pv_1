def on_button_pressed_a():
    global Contador_1, Contador_2, Contador_3
    Contador_1 += 1
    basic.show_string("1+")
    if Contador_1 == 5:
        Contador_2 += 1
        basic.show_string("2+")
    if Contador_2 == 5:
        Contador_3 += 1
        basic.show_string("3+")
input.on_button_pressed(Button.A, on_button_pressed_a)

Contador_2 = 0
Contador_1 = 0
Contador_1 = 0
Contador_2 = 0
Contador_3 = 0
basic.show_leds("""
    # . . . #
    # # . # #
    # . # . #
    # . . . #
    # . . . #
    """)
basic.show_string("Hola")
music.set_volume(120)
music.play(music.string_playable("C5 B A G F E D C ", 180),
    music.PlaybackMode.UNTIL_DONE)

def on_every_interval():
    basic.show_leds("""
        . # # # .
        # # # # #
        # . . . #
        . # . # .
        . . # . .
        """)
loops.every_interval(500, on_every_interval)

def on_forever():
    cuteBot.color_light(cuteBot.RGBLights.ALL, 0xffffff)
    if cuteBot.tracking(cuteBot.TrackingState.L_R_LINE):
        cuteBot.motors(30, 30)
    if cuteBot.tracking(cuteBot.TrackingState.L_UNLINE_R_LINE):
        cuteBot.motors(30, 15)
    if cuteBot.tracking(cuteBot.TrackingState.L_LINE_R_UNLINE):
        cuteBot.motors(15, 30)
    if cuteBot.tracking(cuteBot.TrackingState.L_R_UNLINE):
        cuteBot.motors(0, 0)
basic.forever(on_forever)

def on_forever2():
    if Contador_3 == 5:
        basic.show_string("Adeu")
basic.forever(on_forever2)

def on_forever3():
    basic.show_icon(IconNames.CHESSBOARD)
basic.forever(on_forever3)
