import cv2 as cv


def main():
    capture = cv.VideoCapture(0)  # get first visible video device

    if not capture.isOpened():  # check if founded camera
        raise IOError("Can't open camera (camera doesn't exist)")

    width, height = 1280, 720
    capture.set(cv.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv.CAP_PROP_FRAME_HEIGHT, height)

    title = "Camera"
    cv.namedWindow(title)

    while capture.isOpened():

        _, frame = capture.read()  # get camera video

        frame = cv.resize(frame, None, fx=width / 1280,
                          fy=height / 720, interpolation=cv.INTER_AREA)  # change resolution

        cv.imshow(title, frame)  # show video

        key = cv.waitKey(1)
        if key == 27 or cv.getWindowProperty(title, cv.WND_PROP_VISIBLE) < 1:  # Esc
            break
    capture.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
