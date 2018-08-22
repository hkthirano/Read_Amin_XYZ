# Read_xyzクラス

PDBファイルから、アミノ酸の座標を取り出すクラスである。

# デモ

実行するファイルと同じディレクトリに*Read_XYZ*のディレクトリがあることを想定します。

以下のコードは`demo.py`と同じです。
使用するサンプルPDBファイルとして、タンパク質番号`1A6N`と`1APS`を用意しています。

まずは、ライブラリを読み込みます。
```
from Read_XYZ.main import Read_xyz as r_xyz
```

次に、必要となる変数を定義します。

+ 第１変数 : Chain Id
Chainタイプ (ex. A, B, 1)

+ 第2,3変数 : flagment start, flagment end
取り出すアミノ酸番号の範囲。
指定しない場合は'NA'にする。

```
# config = [Chain Id, flagment start, flagment end]
config = ['A', 'NA', 'NA']
# config = ['A', '10', '100']
```

次に、インスタンスを生成します。
引数には、先ほどの*config*とPDBファイル(ex. './Data/1APS.pdb')のパスを指定します。
```
demo = r_xyz("./Data/1APS.pdb", config)
```

次に、以下の条件に**全て**マッチする行をPDBファイルから取り出します。
## 条件
+ ATOM(原子)を含む
+ CA(α炭素)を含む
+ Chain Id にマッチする
+ 取り出すアミノ酸の範囲にマッチする

```
demo.matching_lines()
```

次に、上で取り出した行を保存します。
引数には、保存先(ex. './demo_line.txt')を指定します。
```
demo.save_matching_lines('./demo_line.txt')
```

次に、先ほど取り出した行からXYZ座標の値を取り出します。
```
demo.extract_xyz()
```

最後に、上で取り出したXYZ座標の値を保存します。
引数には、保存先(ex. './demo_xyz.txt')を指定します。
```
demo.save_extract_xyz('./demo_xyz.txt')
```

demo_xyz.txtの中身は、左から順に、X座標、Y座標、Z座標になっています。

１つのPDBファイルに複数のモデルが存在している場合は、初めの１つ目のモデルについてのみ参照しています。
(ex. 1APS)