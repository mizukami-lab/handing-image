from PIL import Image, ImageOps
import os
import glob
import re
from distutils import dir_util
import shutil

# path = "./元の画像が入っているフォルダ名" とする
path = "./image"

# files_fileに画像名の一覧をリストとして保持させる
files = os.listdir(path)
files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]

# files_fileのリストをテキストに書き込む
# with open("テキスト名", "w", encoding = "utf-8") as f: とする
with open("FL.txt", "w", encoding="utf-8") as f:
    f.writelines(files_file)

# 画像を開いてそのまま保存
for f in files_file:
    # img = Image.open("使用する細胞が入っているフォルダ名/" + f) とする
    img = Image.open(path + "/" + f)
    # 保存するフォルダを作成する
    if not os.path.exists(path + "_m"):
        os.mkdir(path + "_m")
    img.save(path + "_m/" + f, quality=95)
# files = glob.glob("./引数に画像を保存したフォルダ名/*") とする
files = glob.glob(path + "_m/*")
# 生成した画像名の後ろに_00を付ける
for i, f in enumerate(files):
    ftitle, fext = os.path.splitext(f)
    os.rename(f, ftitle + "_" + "00".format(i) + fext)

# 上下反転させた画像を生成
for f in files_file:
    # img = Image.open("使用する細胞が入っているフォルダ名/" + f) とする
    img = Image.open(path + "/" + f)
    img_flip = ImageOps.flip(img)
    # 保存するフォルダを作成する
    if not os.path.exists(path + "1"):
        os.mkdir(path + "1")
    # img_flip.save("画像を保存するフォルダ名/" + f, quality = 95) とする
    img_flip.save(path + "1/" + f, quality=95)
# files = glob.glob("./引数に画像を保存したフォルダ名/*") とする
files = glob.glob(path + "1/*")
# 生成した画像名の後ろに_01を付ける
for i, f in enumerate(files):
    ftitle, fext = os.path.splitext(f)
    os.rename(f, ftitle + "_" + "01".format(i) + fext)

# 画像をimage_mフォルダに移動
dir_util.copy_tree(path + "1", path + "_m")
shutil.rmtree(path + "1")

# 左右反転させた画像を生成
for f in files_file:
    # img = Image.open("使用する細胞が入っているフォルダ名/" + f) とする
    img = Image.open(path + "/" + f)
    img_mirror = ImageOps.mirror(img)
    # 保存するフォルダを作成する
    if not os.path.exists(path + "2"):
        os.mkdir(path + "2")
    # img_flip.save("画像を保存するフォルダ名/" + f, quality = 95) とする
    img_mirror.save(path + "2/" + f, quality=95)
# files = glob.glob("./引数に画像を保存したフォルダ名/*") とする
files = glob.glob(path + "2/*")
# 生成した画像に対して_02を付ける
for i, f in enumerate(files):
    ftitle, fext = os.path.splitext(f)
    os.rename(f, ftitle + "_" + "02".format(i) + fext)

# 画像をimage_mフォルダに移動
dir_util.copy_tree(path + "2", path + "_m")
shutil.rmtree(path + "2")

# 上下左右反転させた画像を生成
for f in files_file:
    # img = Image.open("使用する細胞が入っているフォルダ名/" + f) とする
    img = Image.open(path + "/" + f)
    img_flip_mirror = img.rotate(180)
    # 保存するフォルダを作成する
    if not os.path.exists(path + "3"):
        os.mkdir(path + "3")
    # img_flip.save("画像を保存するフォルダ名/" + f, quality = 95) とする
    img_flip_mirror.save(path + "3/" + f, quality=95)
# files = glob.glob("./引数に画像を保存したフォルダ名/*") とする
files = glob.glob(path + "3/*")
# 生成した画像に対して_03を付ける
for i, f in enumerate(files):
    ftitle, fext = os.path.splitext(f)
    os.rename(f, ftitle + "_" + "03".format(i) + fext)

# 画像をimage_mフォルダに移動
dir_util.copy_tree(path + "3", path + "_m")
shutil.rmtree(path + "3")
