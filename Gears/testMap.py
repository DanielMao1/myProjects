#using disparity get one point coordinates
import numpy as np
import cv2
import camera_configs

cv2.namedWindow("left")
cv2.namedWindow("right")
cv2.namedWindow("depth")
cv2.moveWindow("left", 0, 0)
cv2.moveWindow("right", 600, 0)
cv2.createTrackbar("num", "depth", 0, 10, lambda x: None)
cv2.createTrackbar("blockSize", "depth", 5, 255, lambda x: None)

# Add a click event to print the distance to the current point
def callbackFunc(e, x, y, f, p):
    if e == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        print(threeD[y][x])


cv2.setMouseCallback("depth", callbackFunc, None)

while True:
    # ret1, frame1 = camera1.read()
    # ret2, frame2 = camera2.read()
    # if not ret1 or not ret2:
    #     break

    frame1 = cv2.imread("./img/01.bmp")
    frame2 = cv2.imread("./img/02.bmp")

    # Reconstruct the image according to the correct map
    img1_rectified = cv2.remap(frame1, camera_configs.left_map1, camera_configs.left_map2, cv2.INTER_LINEAR)
    img2_rectified = cv2.remap(frame2, camera_configs.right_map1, camera_configs.right_map2, cv2.INTER_LINEAR)

    # The image is set as grayscale for StereoBM
    imgL = cv2.cvtColor(img1_rectified, cv2.COLOR_BGR2GRAY)
    imgR = cv2.cvtColor(img2_rectified, cv2.COLOR_BGR2GRAY)
    # Two trackbars are used to adjust different parameters to see the effect
    num = cv2.getTrackbarPos("num", "depth")
    blockSize = cv2.getTrackbarPos("blockSize", "depth")
    if blockSize % 2 == 0:
        blockSize += 1
    if blockSize < 5:
        blockSize = 5

    # Generate the difference graph according to the Block Maching method
    stereo = cv2.StereoBM_create(numDisparities=16 * num, blockSize=blockSize)
    # stereo = cv2.StereoSGBM_create(numDisparities=16 * num, blockSize=blockSize)
    disparity = stereo.compute(imgL, imgR)

    disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    #the threeD is the coordinates space of the whole image, you can click the image to get every points image
    threeD = cv2.reprojectImageTo3D(disparity.astype(np.float32) / 16., camera_configs.Q)
    cv2.imshow("depth", disp)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("s"):
        cv2.imwrite("./snapshot/BM_left.jpg", imgL)
        cv2.imwrite("./snapshot/BM_right.jpg", imgR)
        cv2.imwrite("./snapshot/BM_depth.jpg", disp)

cv2.destroyAllWindows()
