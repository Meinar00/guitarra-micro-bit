input.onGesture(Gesture.LogoUp, function () {
    music.setVolume(255)
    music.startMelody(music.builtInMelody(Melodies.JumpDown), MelodyOptions.Once)
})
input.onGesture(Gesture.LogoDown, function () {
    music.setVolume(255)
    music.startMelody(music.builtInMelody(Melodies.JumpUp), MelodyOptions.Once)
})
basic.forever(function () {
    if (input.pinIsPressed(TouchPin.P0)) {
        music.playTone(262, music.beat(BeatFraction.Whole))
        music.setVolume(255)
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            `)
    }
    if (input.pinIsPressed(TouchPin.P1)) {
        music.playTone(262, music.beat(BeatFraction.Whole))
        music.setVolume(255)
        basic.showIcon(IconNames.Happy)
    }
    if (input.pinIsPressed(TouchPin.P2)) {
        music.playTone(262, music.beat(BeatFraction.Whole))
        music.setVolume(255)
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            `)
    }
})
