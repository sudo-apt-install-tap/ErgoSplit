import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.split import Split, SplitType

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.row_pins = (board.D4, board.D5, board.D6, board.D7, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

split = Split(
    split_type=SplitType.BLE,
    use_weighted=False,
    is_left=True,
)
keyboard.modules.append(split)

keyboard.keymap = [
    [
        KC.ESC,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,
        KC.TAB,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,
        KC.LCTL, KC.LALT, KC.SPC,  KC.ENT,  KC.BSPC, KC.DEL,  KC.RSFT, KC.RCTL,
        KC.NO,   KC.NO,   KC.SPC,  KC.ENT,  KC.NO,   KC.NO,   KC.NO,   KC.NO,
    ]
]

if __name__ == '__main__':
    keyboard.go()