# Task 3
# Author : Yunqiu Xu

import matplotlib.pyplot as plt
import cv2
import numpy as np
from PIL import Image, ImageEnhance

def cut(img, lines, int_upper, int_lower, int_left, int_right):
    height, width = img.shape[:2]
    left_vertical, right_vertical, upper_horizontal, lower_horizontal = 0, width - 1, 0, height - 1
    
    for rho,theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = int(a * rho)
        y0 = int(b * rho)
        
        if a > b : # Vertical
            if x0 < width / 2: # left_vertical
                left_vertical = max(x0, left_vertical)
            else: # right_vertical
                right_vertical = min(x0, right_vertical)
        else: # Horizontal
            if y0 < height / 2:
                upper_horizontal = max(y0, upper_horizontal)
            else:
                lower_horizontal = min(y0, lower_horizontal)
                
    return img[(upper_horizontal+int_upper):(lower_horizontal-int_lower), (left_vertical+int_left):(right_vertical-int_right), :]


# Remove border
def remove_border(img, kernel_size = 5, canny_min = 50, canny_max = 100, int_upper = 5, int_lower = 5, int_left = 5, int_right = 5):
    # Canny edge detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)
    edged_img = cv2.Canny(gray, canny_min, canny_max)
    # Hough transformation
    lines = cv2.HoughLines(edged_img,1,np.pi/180,200)
    # Cut the image
    cutted_img = cut(img, lines, int_upper, int_lower, int_left, int_right)
    return cutted_img


# Show histogram
def get_histogram(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray],[0],None,[256], [0.0,255.0])
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)    
    histImg = np.zeros([256,256,3], np.uint8)    
    hpt = int(0.9 * 256)
    for h in range(256):    
        intensity = int(hist[h]*hpt/maxVal)    
        cv2.line(histImg,(h,256), (h,256-intensity), [255,255,255],1)
    return histImg


# Histogram Equalization
def histEq(img):
    b,g,r = cv2.split(img)
    b_eq = cv2.equalizeHist(b)
    g_eq = cv2.equalizeHist(g)
    r_eq = cv2.equalizeHist(r)
    img_output = cv2.merge([b_eq, g_eq, r_eq])
    return img_output


# White balance
def white_balance_gray_world(img):
    img = img * 1.
    b,g,r = cv2.split(img)
    avgR, avgG, avgB = np.mean(r), np.mean(g), np.mean(b)
    avgGray = (avgR + avgG + avgB) / 3. ;  
    outR = (avgGray / avgR) * r
    outG = (avgGray / avgG) * g  
    outB = (avgGray / avgB) * b
    img_output = cv2.merge([outB, outG, outR]) 
    img_output = np.array(img_output, dtype = np.uint8)
    return img_output


def brightness(img, factor):
    img_pil = Image.fromarray(img)
    img_enhanced = ImageEnhance.Brightness(img_pil).enhance(factor)
    img_cv = np.array(img_enhanced, dtype = np.uint8)
    return img_cv


def contrast(img, factor):
    img_pil = Image.fromarray(img)
    img_enhanced = ImageEnhance.Contrast(img_pil).enhance(factor)
    img_cv = np.array(img_enhanced, dtype = np.uint8)
    return img_cv


def color(img, factor):
    img_pil = Image.fromarray(img)
    img_enhanced = ImageEnhance.Color(img_pil).enhance(factor)
    img_cv = np.array(img_enhanced, dtype = np.uint8)
    return img_cv

