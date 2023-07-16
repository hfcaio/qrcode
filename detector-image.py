import cv2

qcd = cv2.QRCodeDetector()

img = cv2.imread("qrcode-example.JPG", -1)

retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(img)
if retval:
    print(decoded_info)
    print(points)

img = cv2.polylines(img, points.astype(int), True, (0, 255, 0), 8)


for s, p in zip(decoded_info, points):
    img = cv2.putText(img, s, p[0].astype(int),
                      cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)


img2 = cv2.resize(img, (800, 900))
cv2.imshow("test", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()