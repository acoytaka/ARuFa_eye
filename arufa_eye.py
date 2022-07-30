import cv2
import sys

camera_id = 0   # カメラIDは環境によって変わります。大体は0か1で動くはず
delay = 1
window_name = 'frame'

# 各自でxmlファイルをダウンロードしてください。
# https://github.com/opencv/opencv/tree/master/data/haarcascades
# Macでbrew installなら入ってるらしい

face_cascade_path = 'data/haarcascade_frontalface_default.xml'
eye_cascade_path = 'data/haarcascade_eye.xml'

face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

cap = cv2.VideoCapture(camera_id)

if not cap.isOpened():
    sys.exit()

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, dsize=None, fx=0.5,
                       fy=0.5)   # 解像度が大きいと誤検出がめっさ増える

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray)  # 顔検出

    for x, y, w, h in faces:
        face = frame[y: y + round(h/2), x: x + w]   # 鼻の誤検出を防ぐ
        face_gray = gray[y: y + round(h/2), x: x + w]
        eyes = eye_cascade.detectMultiScale(face_gray)  # 目の検出

        # こういう書き方は良くない。目の位置と顔の大きさを把握していい感じに描画している。適当だから適宜調整してください。
        try:
            if eyes[0][0] < eyes[1][0]:
                addw = (w - eyes[1][0] - eyes[0][0])/3
                eyex0 = round(eyes[0][0] - addw)
                eyey0 = round(eyes[0][1])
                eyex1 = round(eyes[1][0] + eyes[1][2] + addw)
                eyey1 = round(eyes[1][1] + eyes[1][3])
            else:
                addw = (w - eyes[0][0] - eyes[1][0])/3
                eyex0 = round(eyes[0][0] + eyes[0][2] + addw)
                eyey0 = round(eyes[0][1] + eyes[0][3])
                eyex1 = round(eyes[1][0] - addw)
                eyey1 = round(eyes[1][1])
            cv2.rectangle(face, (eyex0, eyey0), (eyex1, eyey1),
                          (0, 0, 0), -1)
        except:
            pass

    cv2.imshow(window_name, frame)
    if cv2.waitKey(delay) & 0xFF == ord('q'):   # q押すと終了
        break

cv2.destroyWindow(window_name)
