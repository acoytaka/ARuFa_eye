# 某ブロガーみたいな目線を入れるプログラム

こんにちは、さんずです。

突然ですが皆さん、目線をつけたブロガーになりたいなぁと思ったとこはありませんか？
僕はあります。

と、いうことで某ブロガーになるべく、目線を自動でつけるプログラムを作ってみました！

<img src="https://user-images.githubusercontent.com/46366459/181903931-4582a22a-5027-431f-a423-62625d79d065.gif" width="40%">

**⚠️ 即席で作ったのでよく目線が外れます**

**⚠️ 正面じゃないと認識しないです。横顔も顔を傾けてもだめです。まっすぐ姿勢を正してください**

OpenCV + Pythonで動きます。

## ダウンロード

まずはダウンロードしてください

```shell
git clone https://github.com/acoytaka/ARuFa_eye.git
```

動かすのにxmlファイルが必要なので <https://github.com/opencv/opencv/tree/master/data/haarcascades> から

* haarcascade_frontalface_default.xml
* haarcascade_eye.xml

をダウンロードして先程のARuFa_eyeディレクトリの中にdataディレクトリを作って入れてください

## 使い方

MacでOpenCVをインストールしていない場合

```shell
brew install OpenCV
```

動かすとき

```shell
python3 arufa_eye.py
```

動かなかったら頑張って検索して動かせるようにしてください
