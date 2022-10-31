import cv2 as cv
import numpy as np

def detectCorners(contour):
    peri = cv.arcLength(contour, True)
    corners = cv.approxPolyDP(contour, 0.04 * peri, True)
    return corners

def getSlope(contours,frame):
    if(len(contours)!=1):
        # raise Exception("The number of contours is not equal to 1")
        pass
    else:
        contour=contours[0]
        cprop=cv.boundingRect(contour) #x, y, w, h
        corners=detectCorners(contour)
        # corners[0][0] sağ üst
        # corners[1][0] sol üst
        # corners[2][0] sol alt
        # corners[3][0] sağ alt
        realCorners=matchCorners(list(cprop),corners)
        cv.circle(frame, realCorners["ul"],5 , (0, 255, 0), thickness=-1)
        cv.circle(frame, realCorners["ur"],5 , (0, 255, 0), thickness=-1)
        cv.circle(frame, realCorners["dr"],5 , (0, 255, 0), thickness=-1)
        cv.circle(frame, realCorners["dl"],5 , (0, 255, 0), thickness=-1)

        m = (realCorners["ul"][0] - realCorners["dl"][0]) / (realCorners["ul"][1] - realCorners["dl"][1])

        # k=100
        # b=((k**2/(m**2+1))**(1/2))
        print(f"eğim => {m}")
        # cv.line(frame, realCorners["ul"], np.array((realCorners["ul"][0]+b*m, realCorners["ul"][1]+b)).astype(int), (0, 255, 0), thickness=3)

        return m

def matchCorners(cprop,corner):
    rectCorners={"ul":[cprop[0],cprop[1]],
                "ur": [cprop[0]+cprop[2], cprop[1]],
                "dr": [cprop[0] + cprop[2], cprop[1]+cprop[3]],
                "dl": [cprop[0] , cprop[1] +cprop[3]]}

    realCorners={"ul":proximityMatching(rectCorners["ul"],corner),
                "ur": proximityMatching(rectCorners["ur"],corner),
                "dr": proximityMatching(rectCorners["dr"],corner),
                "dl": proximityMatching(rectCorners["dl"],corner)}

    return realCorners


def proximityMatching(arr1,arr2):
    q=[]
    counter=0
    for i in arr2:
        q.append(((arr1[0]-i[0][0])**2+(arr1[1]-i[0][1])**2)**(1/2))
        counter+=1
    mq=min(q)
    for i in range(len(q)):
        if q[i]==mq:
            return arr2[i][0]


def findCenterOfGravity(contours,frame):
    if (len(contours) != 1):
        # raise Exception("The number of contours is not equal to 1")
        pass
    else:
        contour=contours[0]
        cprop = cv.boundingRect(contour)  # x, y, w, h
        corners = detectCorners(contour)
        realCorners = matchCorners(list(cprop), corners)
        top=[0,0]
        for i in realCorners:
            top+=realCorners[i]
        cog=top//4
        cv.circle(frame, cog, 5, (0, 255, 0), thickness=-1)
        return cog
