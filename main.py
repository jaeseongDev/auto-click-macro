import pyautogui as pag
import mss, cv2
import numpy as np
import keyboard

pag.PAUSE = 0.03

left_icon_pos = {
    'left': 83,
    'top': 485,
    'width': 60,
    'height': 60
}

right_icon_pos = {
    'left': 212,
    'top': 484,
    'width': 60,
    'height': 60
}

left_button = [61, 600]
right_button = [305, 613]

def compute_icon_type(img):
    result = None
    mean = np.mean(img, axis=(0, 1))
    
    if (
        mean[0] > 200 and mean[0] < 255 and 
        mean[1] > 70 and mean[1] < 100 and 
        mean[2] > 200 and mean[2] < 255
    ):
        result = 'SWORD'
    elif (
        mean[0] > 30 and mean[0] < 55 and
        mean[1] > 30 and mean[1] < 55 and
        mean[2] > 30 and mean[2] < 55
    ):
        result = 'BOMB'
    elif (
        mean[0] > 90 and mean[0] < 120 and
        mean[1] > 150 and mean[1] < 173 and
        mean[2] > 70 and mean[2] < 100
    ):
        result = 'POSION'
    elif (
        mean[0] > 190 and mean[0] < 210 and
        mean[1] > 190 and mean[1] < 210 and
        mean[2] > 100 and mean[2] < 130
    ):
        result = 'JEWEL'
    else:
        result = '????'
        print('mean : ', mean)

    print('result : ', result)
    return result;

def click(coords):
    print('coords : ', coords)
    pag.moveTo(x=coords[0], y=coords[1], duration=0.0)
    pag.mouseDown()
    pag.mouseUp()

while True:
    with mss.mss() as sct:
        left_img = np.array(sct.grab(left_icon_pos))[:, :, :3]
        right_img = np.array(sct.grab(right_icon_pos))[:, :, :3]

        # cv2.imshow('left_img', left_img)
        # cv2.imshow('right_img', right_img)
        # cv2.waitKey(0)

        left_icon = compute_icon_type(left_img)
        right_icon = compute_icon_type(right_img)

        if left_icon == 'SWORD':
            print('TAP LEFT!')
            click(left_button)
        elif right_icon == 'SWORD':
            print('TAP RIGHT!')
            click(right_button)
        elif left_icon == 'JEWEL' or right_icon == 'JEWEL':
            print('TAP LEFT AND RIGHT!')
            click(left_button)
            click(right_button)

while True:
	x, y = pag.position()
	print('X : ' + str(x) + ' Y : ' + str(y))