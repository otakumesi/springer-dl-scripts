# DL FROM SPRINGER

 SPRINGERが公開してくれてるPDFをダウンロードするスクリプト。  
 サーバーに迷惑かけないようにダウンロード1回につき2秒くらいsleepを置いてます。
 
### HOT TO USE
https://www.springernature.com/jp/campaign/library_textbook  
まず、上記からタイトルリストのexcelファイルをダウンロードして、srcディレクトリに置きます。

そして、以下のコマンドを実行してきます。

```
poetry install
poetry run python dl_from_springer.py
```
