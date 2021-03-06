# Read_Amin_XYZ

PDBファイルからアミノ酸主鎖の座標を取り出すライブラリ. 

オプションでアミノ酸に重みを付加.

**重み**
+ VDWr : ファンデルワールス半径 
+ IEP : 等電点
+ Kyte-Doolittle : 疎水性指標1
+ Hopp-Woods : 疎水性指標2
+ Engelman : 疎水性指標3
+ MW : 分子量

１つのPDBファイルに複数のモデルが存在している場合は, 初めの１つ目のモデルについてのみ参照.

(ex. 1APS)

# デモ

`python demo_1A6N.py`を実行すると３つのファイルができる.

1. 1A6N_line.txt : PDBファイルの（model1の）アミノ酸主鎖の行

```
# 例
ATOM      2  CA  VAL A   1      -3.461  15.612  15.004  0.70 28.70           C  
ATOM      9  CA  LEU A   2      -0.614  14.130  16.996  0.70 14.07           C  
ATOM     17  CA  SER A   3      -1.434  12.460  20.317  0.70 14.28           C  
```

2. 1A6N_xyz.txt : 1A6N_line.txtのXYZ座標

```
# 例 : x座標、y座標、z座標
-3.460999965667724609e+00 1.561200046539306641e+01 1.500399971008300781e+01
-6.140000224113464355e-01 1.413000011444091797e+01 1.699600028991699219e+01
-1.434000015258789062e+00 1.246000003814697266e+01 2.031699943542480469e+01
```

3. 1A6N_xyz_VDWr.txt : 1A6N_line.txtのXYZ座標 + 重み

```
# 例 : x座標、y座標、z座標、重み(ファンデルワールス半径)
-3.460999965667724609e+00 1.561200046539306641e+01 1.500399971008300781e+01 1.050000000000000000e+02
-6.140000224113464355e-01 1.413000011444091797e+01 1.699600028991699219e+01 1.240000000000000000e+02
-1.434000015258789062e+00 1.246000003814697266e+01 2.031699943542480469e+01 7.300000000000000000e+01
```

# 使い方

実行するファイルと同じディレクトリに`Read_XYZ`のディレクトリがあることを想定.

以下のコードは`demo_1A6N.py`と同じ. 

使用するサンプルPDBファイルとして,タンパク質番号`1A6N`と`1APS`を用意.

まずは, ライブラリを読み込む.

```
from Read_XYZ.main import Read_xyz as r_xyz
```

次に, 必要となる変数を定義.

+ 第１変数 : Chain Id
Chainタイプ (ex. A, B, 1)

+ 第2,3変数 : flagment start, flagment end

取り出すアミノ酸番号の範囲.

指定しない場合は'NA'にする.

```
# config = [Chain Id, flagment start, flagment end]
config = ['A', 'NA', 'NA']
# config = ['A', '10', '100']
```

次に, インスタンスを生成.

引数には先ほどの`config`とPDBファイル(ex. './Data/1APS.pdb')のパスを指定.

```
demo = r_xyz("./Data/1APS.pdb", config)
```

次に, 以下の条件に**全て**マッチする行をPDBファイルから取り出す.
+ ATOM(原子)を含む
+ CA(α炭素)を含む
+ Chain Id にマッチする
+ 取り出すアミノ酸の範囲にマッチする

```
demo.matching_lines()
```

次に, 上で取り出した行を保存.

引数には保存先(ex. './demo_line.txt')を指定.

```
demo.save_matching_lines('./1A6N_line.txt')
```

次に, 先ほど取り出した行からXYZ座標の値を取り出す.
```
demo.extract_xyz()
```

最後に, 上で取り出したXYZ座標の値を保存.

引数には保存先(ex. './demo_xyz.txt')を指定.

```
demo.save_extract_xyz('./1A6N_xyz.txt')
```

重みを付ける場合は, `demo.extract_xyz()`の代わりに

```
demo.extract_xyz_with_weight('VDWr')
```

を使用.

引数には重みのタイプを指定.

defaultでは、`VDWr`:Van der Waals radius と `IEP`:Isoelectric point
を用意.

保存は`demo.extract_xyz()`の時と同じ.

```
demo.save_extract_xyz('./1A6N_xyz_VDWr.txt')
```

