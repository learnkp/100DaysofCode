import pyautogui
from PIL import ImageGrab
import time


def hit(key):
    """function to automate your key, which you want to press in keyboard"""
    pyautogui.keyDown(key)


# We are creating a function, Which will draw a rectangle within the range of cactus as well as bird.
# if the respective rectangle clash with bird, the dino will headed down.
# if the respective rectangle clash with cactus, the dino will jump.
def is_collide(data):
    # collide with bird
    for i in range(180, 210):
        for j in range(300, 410):
            if data[i, j] < 100:
                hit("down")
                return True

    # collide with cactus
    for i in range(211, 270):
        for j in range(411, 480):
            if data[i, j] < 110:
                hit("up")
                return True
    return False


if __name__ == "__main__":
    time.sleep(3)
    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        is_collide(data)


        # collide with cactus
        # for i in range(211, 240):
        #     for j in range(411, 500):
        #         data[i, j] = 0
        #
        # # collide with bird
        # for i in range(180, 210):
        #     for j in range(300, 410):
        #         data[i, j] = 171
        # # if is_collide(data):
        # #     hit('up')
        #
        # image.show()
        # break
