# 使用前に「#」を付加し、使用後に「#」を削除する
print(a)

from PIL import Image, ImageOps
import os
import glob
import re

# path = "./元の画像が入っているフォルダ名" とする
path = "./FL"


""" files_fileに画像名の一覧をリストとして保持させる """
files = os.listdir(path)
files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]


""" files_fileのリストをテキストに書き込む """
# with open("テキスト名", "w", encoding = "utf-8") as f: とする
with open("FL.txt", "w", encoding = "utf-8") as f:
    f.writelines(files_file)


""" 画像を開いてそのまま保存 """
for f in files_file:
    # img = Image.open("使用する細胞が入っているフォルダ名/" + f) とする
    img = Image.open("FL/" + f)
    img.save("FL 0/" + f, quality = 95)

# files = glob.glob("./引数に画像を保存したフォルダ名/*") とする
files = glob.glob("./FL 0/*")


""" 生成した画像名の後ろに_00を付ける """
for i,f in enumerate(files):
    ftitle, fext = os.path.splitext(f)
    os.rename(f, ftitle + "_" + "00".format(i) + fext)


""" 上下反転させた画像を生成 """
for f in files_file:
    # img = Image.open("使用する細胞が入っているフォルダ名/" + f) とする
    img = Image.open("FL/" + f)
    img_flip = ImageOps.flip(img)
    
    # img_flip.save("画像を保存するフォルダ名/" + f, quality = 95) とする
    img_flip.save("FL 1/" + f, quality = 95)

# files = glob.glob("./引数に画像を保存したフォルダ名/*") とする
files = glob.glob("./FL 1/*")


""" 生成した画像名の後ろに_01を付ける """
for i,f in enumerate(files):
    ftitle, fext = os.path.splitext(f)
    os.rename(f, ftitle + "_" + "01".format(i) + fext)


""" 左右反転させた画像を生成 """
for f in files_file:
    # img = Image.open("使用する細胞が入っているフォルダ名/" + f) とする
    img = Image.open("FL/" + f)
    img_mirror = ImageOps.mirror(img)
    
    # img_flip.save("画像を保存するフォルダ名/" + f, quality = 95) とする
    img_mirror.save("FL 2/" + f, quality = 95)

# files = glob.glob("./引数に画像を保存したフォルダ名/*") とする
files = glob.glob("./FL 2/*")


""" 生成した画像に対して_02を付ける """
for i,f in enumerate(files):
    ftitle, fext = os.path.splitext(f)
    os.rename(f, ftitle + "_" + "02".format(i) + fext)


""" 上下左右反転させた画像を生成 """
for f in files_file:
    # img = Image.open("使用する細胞が入っているフォルダ名/" + f) とする
    img = Image.open("FL/" + f)
    img_flip_mirror = img.rotate(180)

    # img_flip.save("画像を保存するフォルダ名/" + f, quality = 95) とする
    img_flip_mirror.save("FL 3/" + f, quality = 95)

# files = glob.glob("./引数に画像を保存したフォルダ名/*") とする
files = glob.glob("./FL 3/*")


""" 生成した画像に対して_03を付ける """
for i,f in enumerate(files):
    ftitle, fext = os.path.splitext(f)
    os.rename(f, ftitle + "_" + "03".format(i) + fext)
