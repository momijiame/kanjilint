# kanjilint

## これは何ですか？

文章の中から平仮名に開いた方が読みやすくなる漢字を見つけ出すツールです。

## インストール

Python のパッケージマネージャ PIP を使ってインストールします。
```
$ pip install https://github.com/momijiame/kanjilint.git
```

## 使い方

インストールされると kanjilint コマンドが使えるようになります。

開いたほうが読みやすくなる漢字を文章から見つけるには detect サブコマンドを使います。
```
$ kanjilint detect <directory or file>
```

見つけると同時にインプレースで置換するには replace サブコマンドを使います。
```
$ kanjilint replace <directory or file>
```

## 参考

https://twitter.com/tarareba722/status/604512061003960320
