import cv2 as cv


def sketch(image):

    grey_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    grey_image_blur = cv.GaussianBlur(grey_image, (5, 5), 0)

    canny_edges = cv.Canny(grey_image_blur, 30, 70)

    ret, mask = cv.threshold(canny_edges, 120, 255, cv.THRESH_BINARY_INV)
    return mask


def live_Sketch():
    cap = cv.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv.imshow("Live Sketch", sketch(frame))
        if cv.waitKey(1) == 27:
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    live_Sketch()
