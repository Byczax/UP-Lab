import cv2 as cv
import datetime
import os
def resize_frame(image, scale, height, width):
    height, width, channels = image.shape

    centerX, centerY = int(height / 2), int(width / 2)

    radiusX, radiusY = int(scale * height), int(scale * width)

    minX, maxX = centerX - radiusX, centerX + radiusX
    minY, maxY = centerY - radiusY, centerY + radiusY

    cropped = image[minX:maxX, minY:maxY]
    resized_cropped = cv.resize(cropped, (width, height)) 
    return resized_cropped


def main():
    capture = cv.VideoCapture(0)  # get first visible video device

    if not capture.isOpened():  # check if founded camera
        raise IOError("Can't open camera (camera doesn't exist)")

    width, height = 1280, 720
    alpha, beta, zoom = 1.0, 0.0, 0.5

    capture.set(cv.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv.CAP_PROP_FRAME_HEIGHT, height)

    title = "Camera"
    cv.namedWindow(title)
    
    recording = False
    recorder = cv.VideoWriter("Film.avi", 0, 20, (width, height))
    
    detect = False
    prev_frame = None

    while capture.isOpened():

        _, frame = capture.read()  # get camera video

        frame = cv.resize(frame,
                          None,
                          fx=width / 1280,
                          fy=height / 720,
                          interpolation=cv.INTER_AREA)  # change resolution

        alpha = max(0, alpha)
        zoom = max(0.1, zoom)
        zoom = min(0.5, zoom)
        

        frame = cv.convertScaleAbs(frame, alpha=alpha, beta=beta)
        
        if recording:
            recorder.write(frame)

        cv.putText(
            frame,
            f"Alpha={format(alpha, '.1f')}, Beta={format(beta, '.1f')}, Zoom={format(zoom * 2, '.1f')}",
            (0, 24),
            cv.FONT_ITALIC,
            1,
            (255, 255, 255))

        frame = resize_frame(frame, zoom, height, width)

        if not detect:
            cv.imshow(title, frame)  # show video
        
        
        # motion detection
        if detect:
            if prev_frame is not None: # don't compare with empty frame
                
                # change to grayscale
                prev_frame = cv.cvtColor(prev_frame, cv.COLOR_BGR2GRAY)
                frame_copy = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

                # remove sharp edges
                prev_frame = cv.GaussianBlur(prev_frame, (21, 21), 0)
                frame_copy = cv.GaussianBlur(frame_copy, (21, 21), 0)

                # compare frames
                delta_frame = cv.absdiff(prev_frame, frame_copy)
                
                # mark different pixels
                thresh_frame = cv.threshold(delta_frame, 5, 255, cv.THRESH_BINARY)[1]
                cv.dilate(thresh_frame, None, iterations=2)

                contours, _ = cv.findContours(thresh_frame, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

                # create rectangles on captured motion
                rectangles = []
                for c in contours:
                    if cv.contourArea(c) < 1 / 750 * width * height:
                        continue
                    rectangles.append(cv.boundingRect(c))

                frame_copy = frame.copy()
                for rect in rectangles:
                    x = rect[0]
                    y = rect[1]
                    w = rect[2]
                    h = rect[3]
                    cv.rectangle(frame_copy, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv.imshow(title, frame_copy)
        
        prev_frame = frame

        key = cv.waitKey(1)
        if key == 27 or cv.getWindowProperty(title, cv.WND_PROP_VISIBLE) < 1:  # Esc
            break
        elif key == ord("a"):
            alpha += 0.1
        elif key == ord("A"):
            alpha -= 0.1
        elif key == ord("b"):
            beta += 0.1
        elif key == ord("B"):
            beta -= 0.1
        elif key == ord("Z"):
            zoom += 0.01
        elif key == ord("z"):
            zoom -= 0.01
        elif key == ord("s"):  
            os.makedirs("screens", exist_ok=True)              
            filename = datetime.datetime.isoformat(datetime.datetime.now()).replace(":","")
            if detect:
                save_frame = frame_copy
            else:
                save_frame = frame
            cv.imwrite(f"screens/{filename}.png", save_frame)
            print(f"Saved image to screens/{filename}.png")
        elif key == ord("r"):
            if not recording:
                recording = True
            else:
                recorder.release()
        elif key == ord("m"):
            detect = not detect
            
    capture.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
