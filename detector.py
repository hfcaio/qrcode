import cv2
import numpy as np

def center_point(points):
    x = (points[0][0][0] + points[0][1][0])/2
    y = (points[0][0][1] + points[0][1][1])/2
    return (x, y)

def detect_qrcode(img):
    qcd = cv2.QRCodeDetector()
    retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(img)
    return retval, decoded_info, points


camera = cv2.VideoCapture(0)
validate, frame = camera.read()

print("start :)")
while validate:
    validate, frame = camera.read()
    found, info, points = detect_qrcode(frame)
    if found:
        print(f"decoded info: {info}")
        print (f"center {center_point(points)}")
        frame = cv2.polylines(frame, points.astype(int), True, (0, 255, 0), 3)
    cv2.imshow("show", frame)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()