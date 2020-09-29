import pyautogui as pag
import mss, cv2
import numpy as np

left_icon_pos = {
    'left': 83,
    'top': 485,
    'width': 70,
    'height': 60
}

right_icon_pos = {
    'left': 212,
    'top': 484,
    'width': 70,
    'height': 60
}

left_button = [70, 680]
right_button = [355, 680]




while True:
#      x, y = pag.position()
#      position_str = 'X: ' + str(x) + ' Y: ' + str(y)
#      print(position_str)
    with mss.mss() as sct:
        left_img = np.array(sct.grab(left_icon_pos))[:, :, :3]
        right_img = np.array(sct.grab(right_icon_pos))[:, :, :3]
        helper.macro(left_img, right_img, left_button, right_button)

        cv2.imshow('left_img', left_img)
        cv2.imshow('right_img', right_img)
        cv2.waitKey(0)