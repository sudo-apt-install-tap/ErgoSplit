import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.row_pins = (board.D4, board.D5, board.D6, board.D7, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

split = Split(
    split_type=SplitType.BLE,
    is_left=False,
)
keyboard.modules.append(split)

if __name__ == '__main__':
    keyboard.go()