import cv2 as cv
from PIL import Image
import numpy as np

from function import make_error_map
from function import merge_img
from function import RGB_error
from function import calculation_ROI

def main():
    # パスを指定
    path = "./from_hoshoi/"
    iter = 37700
    iter_padded = '{0:08d}'.format(iter)
    path_A = path + 'image_gt_' + iter_padded + '_0001.png'
    path_B = path + 'image_gen_' + iter_padded + '_0001.png'

    # 画像を開く
    img_a = cv.imread(path_A, 1)
    img_b = cv.imread(path_B, 1)

    # 画像サイズが異なるとエラーになるので確認すること
    h, w, c = img_a.shape
    # print(img_a.shape)

    print("分岐を選択")
    choice = input("1:画像全体で比較,2:ROIで比較>>>" + "\n")

    if int(choice) == 1:

        # 関数による処理
        make_error_map(path, img_a, img_b)
        error_map = Image.open(path + "error_map_diff.png")
        rgblist = RGB_error(w, h, error_map)

        # 画像全体のエラー率を算出する
        error = ((sum(rgblist) / (w * h)) / 256) * 100
        print('画像全体でピクセル当たりのエラー率(%)')
        print(error)

    else:
        # 関数による処理
        make_error_map(path, img_a, img_b)
        error_map = Image.open(path + "error_map_diff.png")
        merge_img(path, img_a, img_b)
        merge = Image.open(path + "./merge.png")
        ROI_list, rgblist = calculation_ROI(path, w, h, merge, error_map)

        # ROIのエラー率を算出する
        if not int(ROI_list[0]) == 0:
            Red_error_ROI = rgblist[0] / ROI_list[0] / 256 * 100
            print('RのROIエラー(%)')
            print(Red_error_ROI)
        if not int(ROI_list[1]) == 0:
            Green_error_ROI = rgblist[1] / ROI_list[1] / 256 * 100
            print('GのROIエラー(%)')
            print(Green_error_ROI)
        if not int(ROI_list[2]) == 0:
            Blue_error_ROI = rgblist[2] / ROI_list[2] / 256 * 100
            print('BのROIエラー(%)')
            print(Blue_error_ROI)

if __name__ == "__main__":
    main()
