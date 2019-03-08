import cv2 as cv
from PIL import Image
import os
import numpy as np

def make_error_map(path, img_a, img_b):
    # エラーマップ作製
    error_map = cv.absdiff(img_a, img_b, dst=None)

    # 画像の表示
    cv.imshow('error_map', error_map)

    # 画像の保存
    cv.imwrite(path + 'error_map_diff.png', error_map)

    # キー入力待ち 入力すると開いているウインドウをすべて閉じる
    cv.waitKey(0)
    cv.destroyAllWindows()

    return error_map

def merge_img(path, img_a, img_b):
    # マージ画像の作製
    merge = cv.add(img_a, img_b)

    # 画像の表示
    cv.imshow('merge', merge)

    # 画像の保存
    cv.imwrite(path + '/merge.png', merge)

    cv.waitKey(0)
    cv.destroyAllWindows()

    return merge_img

def calculation_ROI(path, w, h, merge_img, error_map):

    # ROIリストの入れ物を作成
    rlist = []
    glist = []
    blist = []

    # rgbリストの入れ物を作成
    redlist = []
    greenlist = []
    bluelist = []

    # 各ピクセルのRGBをリスト化する
    for i in range(w):
        for j in range(h):
            r, g, b = merge_img.getpixel((i, j))
            red, green, blue = error_map.getpixel((i, j))
            if r > 50:
                rlist.append(r)
                redlist.append(red)
            else:
                rlist.append(0)
                redlist.append(0)
            if g > 120:
                glist.append(g)
                greenlist.append(green)
            else:
                glist.append(0)
                greenlist.append(0)
            if b > 100:
                blist.append(b)
                bluelist.append(blue)
            else:
                blist.append(0)
                bluelist.append(0)

    """# リストをエクセルで出力
    f = open(path + 'output.csv', 'w')
    f.write("r,g,b\n")
    n = len(rlist)
    for i in range(0, n - 1):
        f.write(str(rlist[i]) + "," + str(glist[i]) + "," + str(blist[i]) + "\n")

    f.close()"""

    # 画像の面積(pixel)
    # area = pixelSizeTuple[0] * pixelSizeTuple[1]
    area = w * h
    # 各リストの0をカウントし、全ピクセル数から引く
    Red_ROI = int(area) - int(rlist.count(0))
    Blue_ROI = int(area) - int(blist.count(0))
    Green_ROI = int(area) - int(glist.count(0))
    ROI_list = [Red_ROI, Green_ROI, Blue_ROI]

    r = sum(redlist)
    g = sum(greenlist)
    b = sum(bluelist)
    print('R, G, B')
    rgblist = [r, g, b]
    print(rgblist)

    # ROIの出力
    if not int(Red_ROI) == 0:
        print('赤の関心領域')
        print(Red_ROI, "pixels")
    if not int(Green_ROI) == 0:
        print('緑の関心領域')
        print(Green_ROI, "pixels")
    if not int(Blue_ROI) == 0:
        print('青の関心領域')
        print(Blue_ROI, "pixels")

    return ROI_list, rgblist

def RGB_error(w, h, error_img):

    # リストの入れ物を作成
    redlist = []
    greenlist = []
    bluelist = []

    # 各ピクセルのRGBをリスト化する
    for i in range(w):
        for j in range(h):
            r, g, b = error_img.getpixel((i, j))
            redlist.append(r)
            greenlist.append(g)
            bluelist.append(b)

    r = sum(redlist)
    g = sum(greenlist)
    b = sum(bluelist)
    print('R, G, B')
    rgblist = [r, g, b]
    print(rgblist)

    return rgblist
