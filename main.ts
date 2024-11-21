input.onButtonPressed(Button.A, function () {
    Contador_1 += 1
    basic.showString("1+")
    if (Contador_1 == 5) {
        Contador_2 += 1
        basic.showString("2+")
    }
    if (Contador_2 == 5) {
        Contador_3 += 1
        basic.showString("3+")
    }
})
let Contador_2 = 0
let Contador_1 = 0
Contador_1 = 0
Contador_2 = 0
let Contador_3 = 0
basic.showLeds(`
    # . . . #
    # # . # #
    # . # . #
    # . . . #
    # . . . #
    `)
basic.showString("Hola")
music.setVolume(120)
music.play(music.stringPlayable("C5 A B G A F G E ", 180), music.PlaybackMode.UntilDone)
loops.everyInterval(500, function () {
    basic.showLeds(`
        . # # # .
        # # # # #
        # . . . #
        . # . # .
        . . # . .
        `)
})
basic.forever(function () {
    cuteBot.colorLight(cuteBot.RGBLights.ALL, 0xffffff)
    if (cuteBot.tracking(cuteBot.TrackingState.L_R_line)) {
        cuteBot.motors(30, 30)
    }
    if (cuteBot.tracking(cuteBot.TrackingState.L_unline_R_line)) {
        cuteBot.motors(30, 15)
    }
    if (cuteBot.tracking(cuteBot.TrackingState.L_line_R_unline)) {
        cuteBot.motors(15, 30)
    }
    if (cuteBot.tracking(cuteBot.TrackingState.L_R_unline)) {
        cuteBot.motors(0, 0)
    }
})
basic.forever(function () {
    if (Contador_3 == 5) {
        basic.showString("Adeu")
    }
})
basic.forever(function () {
    basic.showIcon(IconNames.Chessboard)
})
