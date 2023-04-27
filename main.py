def on_gesture_logo_up():
    music.set_volume(255)
    music.start_melody(music.built_in_melody(Melodies.JUMP_DOWN),
        MelodyOptions.ONCE)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_logo_down():
    music.set_volume(255)
    music.start_melody(music.built_in_melody(Melodies.JUMP_UP), MelodyOptions.ONCE)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_forever():
    if input.pin_is_pressed(TouchPin.P0):
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.set_volume(255)
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        . # # # .
                        # . . . #
        """)
    if input.pin_is_pressed(TouchPin.P1):
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.set_volume(255)
        basic.show_icon(IconNames.HAPPY)
    if input.pin_is_pressed(TouchPin.P2):
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.set_volume(255)
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        . # # # .
                        # . . . #
        """)
basic.forever(on_forever)
