# -*- coding: utf-8 -*-
'''
Created on 2015/01/18

@author: fumio
'''

import scipy as sp
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# トラフィック量データの読み込み
data = sp.genfromtxt("data/web_traffic.tsv")

# TSVファイルの夜も混んだリストをxとyに代入する
x = data[:,0]
y = data[:,1]

# 日本語フォントの指定
fp = FontProperties(fname="/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf")

# 散布図作成
plt.scatter(x, y)

# 散布図のタイトルやxy軸ラベルをセットする
plt.title(u"先月のトラフィック量",  fontdict={'fontproperties':fp})
plt.xlabel(u"時間",  fontdict={'fontproperties':fp})
plt.ylabel(u"１時間毎のアクセス数",  fontdict={'fontproperties':fp})

# 10日分のx軸のメモリ区切りを1週毎に設定し、メモリに単位表示する
plt.xticks([w*7*24 for w in range(10)], ['week %i'%w for w in range(10)])

# データのある上限リミットいっぱいでグラフ表示するようにする
plt.autoscale(tight=True)

# xの値の最後までを1000分割してf1(x)へのxの引数とするために設定する
#fx = sp.linspace(0, x[-1], 1000)
fx = sp.linspace(0, 6*7*24, 1000)

# 1次関数として近似関数のモデルを得る
# fp1にモデル係数が格納される f(x) = ax + bのa, bに当たる部分が格納される。
# full=Trueに指定した場合residuals以降の詳細なデータを返してくれる。デフォルトはFalse
fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)

# モデルパラメータfp1からモデル関数f1(x)を作成する
f1 = sp.poly1d(fp1)
plt.plot(fx, f1(fx), linewidth=4)

# 2次関数として近似関数のモデルを得る
# fp2にモデル係数が格納される f(x) = ax^2 + bx + cのa, b, cに当たる部分が格納される。
fp2 = sp.polyfit(x, y, 2)

f2 = sp.poly1d(fp2)
plt.plot(fx, f2(fx), linewidth=4)

fp3 = sp.polyfit(x, y, 3)

f3 = sp.poly1d(fp3)
plt.plot(fx, f3(fx), linewidth=4)

fp10 = sp.polyfit(x, y, 10)

f10 = sp.poly1d(fp10)
plt.plot(fx, f10(fx), linewidth=4)

fp50 = sp.polyfit(x, y, 50)

f50 = sp.poly1d(fp50)
plt.plot(fx, f50(fx), linewidth=4)

plt.ylim(0,10000)
# 左上に凡例を表示する
plt.legend(["d=%i" % f1.order, "d=%i" % f2.order, "d=%i" % f3.order, "d=%i" % f10.order, "d=%i" % f50.order], loc="upper left")

# 目盛線を表示する
plt.grid()

# 散布図を表示する
plt.show()
