import cv2

qcd = cv2.QRCodeDetector()

img = cv2.imread("4_qrcode.png", -1)

retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(img)
if retval:
    print(decoded_info)
    print(points)

img = cv2.polylines(img, points.astype(int), True, (0, 255, 0), 8)


for s, p in zip(decoded_info, points):
    img = cv2.putText(img, s, (p[0].astype(int)[0], p[0].astype(int)[1] - 10),
                      cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imwrite("multi_qrcode_detected.jpg", img)
cv2.imshow("test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
