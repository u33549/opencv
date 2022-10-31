import cv2
import numpy as np

videoPath="..\\..\\Resources\\Videos"
capture=cv2.VideoCapture(videoPath+"\\drone1.mp4")



while True:
    isTrue, frame=capture.read()
    print(isTrue)
    if isTrue:

        rgb_planes = cv2.split(frame)
        result_planes = []
        result_norm_planes = []
        for plane in rgb_planes:
            dilated_img = cv2.dilate(plane, np.ones((7, 7), np.uint8))
            bg_img = cv2.medianBlur(dilated_img, 21)
            diff_img = 255 - cv2.absdiff(plane, bg_img)
            norm_img = cv2.normalize(diff_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
            result_planes.append(diff_img)
            result_norm_planes.append(norm_img)

        result = cv2.merge(result_planes)
        result_norm = cv2.merge(result_norm_planes)

        cv2.imshow('shadows_out.png', result)
        cv2.imshow('shadows_out_norm.png', result_norm)

        if cv2.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()








