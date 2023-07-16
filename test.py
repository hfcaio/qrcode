import cv2

qcd = cv2.QRCodeDetector()
img = cv2.imread("qrcode-example.JPG", -1)

cam = cv2.VideoCapture(-1)

while True:
    validate, img = cam.read()
    retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(img)
    img = cv2.polylines(img, points.astype(int), True, (0, 255, 0), 8)

    cv2.imshow("test", img)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()