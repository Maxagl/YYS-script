from __future__ import print_function
import cv2 as cv
import numpy as np
import action

def surf(img1, img2,ratio_thresh):
    if img1 is None or img2 is None:
        print('Could not open or find the images!')
        exit(0)
    #-- Step 1: Detect the keypoints using SURF Detector, compute the descriptors

    minHessian = 400
    detector = cv.SIFT_create() #(hessianThreshold=minHessian)
    keypoints1, descriptors1 = detector.detectAndCompute(img1, None)
    keypoints2, descriptors2 = detector.detectAndCompute(img2, None)
    #-- Step 2: Matching descriptor vectors with a FLANN based matcher
    # Since SURF is a floating-point descriptor NORM_L2 is used
    matcher = cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)
    knn_matches = matcher.knnMatch(descriptors1, descriptors2, 2)
    #-- Filter matches using the Lowe's ratio test
    # ratio_thresh = 0.65
    good_matches = []
    distance = []
    for m,n in knn_matches:
        if m.distance < ratio_thresh * n.distance:
            distance.append(m.distance)
            good_matches.append(m)

    #-- Draw matches
    if distance:
        best_distance = min(distance)
        for i in good_matches:
            if (i.distance == best_distance ):
                best_match = i


        img_matches = np.empty((max(img1.shape[0], img2.shape[0]), img1.shape[1]+img2.shape[1], 3), dtype=np.uint8)
        cv.drawMatches(img1, keypoints1, img2, keypoints2, good_matches, img_matches, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

        img1_idx = best_match.queryIdx
        img2_idx = best_match.trainIdx
        a = keypoints1[img1_idx].pt
        b = keypoints2[img2_idx].pt
        return b
    else:
        return []
