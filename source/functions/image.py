import cv2
import numpy as np

def pad_image(image):
    resy, resx = image.shape[:2]
    bigger_res = resx if resx > resy else resy


    dw = int((resy - resx) / 2)
    if dw < 0:
        dh = -dw
        dw = 0
    else:
        dh = 0


    black_im = np.zeros((bigger_res, bigger_res, 3))
    print(f'{dh}:{bigger_res}-{dh}, {dw}:{bigger_res}-{dw}')
    black_im[dh:bigger_res-dh, dw:bigger_res-dw] = im
    im = black_im

    
    return image, (dw, dh)

def draw_bounding_box(image, bounding_box_normalized):
    
    ymin, xmin, ymax, xmax = bounding_box_normalized * bigger_res

    res_x, res_y = image.shape[:2]
    
    cv2.rectangle(image,(xmin,ymin),(xmax,ymax),(0,255,0),2)
    cv2.circle(image,(px, py), 5,(50,50,255),2)