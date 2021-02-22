import cv2
from Classes.WindowCapture import WindowCapture
import time
import argparse
import win32gui
from osrsbox import items_api

def environment():
    window_rect = win32gui.GetWindowRect(win32gui.FindWindow(None, 'Old School RuneScape'))
    w = window_rect[2] - window_rect[0]
    h = window_rect[3] - window_rect[1]

    # account for the window border and titlebar and cut them off
    border_pixels = 8
    titlebar_pixels = 30

    w = w - (border_pixels * 2)
    h = h - titlebar_pixels - border_pixels
    cropped_x = border_pixels
    cropped_y = titlebar_pixels

    # set the cropped coordinates offset so we can translate screenshot
    # images into actual screen positions
    offset_x = window_rect[0] + cropped_x
    offset_y = window_rect[1] + cropped_y
    print(offset_x, offset_y, w, h)

def main():
    # items = items_api.load()
    # for i in items:
    #     print(i.icon)

    # get the window size

    cap = WindowCapture('Old School RuneScape')

    while True:
        last_time = time.time()
        img = cap.get_screenshot()
        cv2.imshow("Image", img)
        print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    main()
