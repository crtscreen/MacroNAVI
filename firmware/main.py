"""MacroNAVI: Seeed XIAO RP2040, three direct keys, 128x32 SSD1306 OLED"""
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

# set as False to test the keys before intalling the display libraries
ENABLE_OLED = True

keyboard = KMKKeyboard()
keyboard.matrix = KeysScanner(
    pins=(board.D0, board.D1, board.D2),
    value_when_pressed=False,
    pull=True,
    interval=0.001,
    debounce_threshold=5,
)
keyboard.coord_mapping = (0, 1, 2)

# SW1, SW2, SW3: left to right
keyboard.keymap = [[KC.F13, KC.F14, KC.F15]]

if ENABLE_OLED:
    import busio

    from kmk.extensions.display import Display, TextEntry
    from kmk.extensions.display.ssd1306 import SSD1306

    i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
    oled = Display(
        display=SSD1306(i2c=i2c, device_address=0x3C),
        width=128,
        height=32,
        brightness=0.8,
        entries=[
            TextEntry(text="COPLAND OS", x=0, y=0, y_anchor="T"),
            TextEntry(text="F13  F14  F15", x=0, y=16, y_anchor="T"),
        ],
    )
    keyboard.extensions.append(oled)

if __name__ == "__main__":
    keyboard.go()