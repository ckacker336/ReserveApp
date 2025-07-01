"# ReserveApp"

## 病院の診察予約自動化アプリの作成

---

## ■ 概要  
病院における診察予約の自動化を目的としたPythonアプリケーションの作成を行った。  
予約のスケジューリング機能やブラウザ操作による自動処理を学習・実装対象とし、PythonおよびVSCode環境での開発を進めた。

---
## ■ 作業内容  

- Python開発環境の構築（VSCode、仮想環境含む）  
- GitHubアカウントとの連携およびSSH通信設定  
- スケジューラによる予約機能の実装（参考コードベースにカスタマイズ）  
- Pythonを用いたEdgeブラウザの自動操作の理解と検証  

---

## ■ 作業時間  
2日間

---

## ■ 動作確認  
設定した日時にブラウザの立ち上げ・指定の操作を行うことを確認した。  
実際のURLを入れて動かすと、自動的に予約を行うことができた。  
手動操作を行うときよりも処理速度が挙がったことで、1番の予約番号を取得できることを確認した。

---

## ■ 所感  
VSCodeは以前のプロジェクトで使用経験があり、スムーズにPythonの環境構築を行うことができた。  
Python自体は初めて学習したが、シンプルで読みやすい構文であり、比較的理解しやすかった。  
ただし、まだ学習が浅く、構文やコード規則などの全体的な理解には至っていないため、今後も継続して学んでいきたいと考えている。

---

## ■ 参考資料  

- Pythonのインストール・VSCodeでの環境構築  
  - https://qiita.com/mmake/items/5197afbe5c055f82265e  
  - https://qiita.com/mmake/items/55401c6a9e2f3f0f3475  

- Pythonのディレクトリ構成について  
  - https://qiita.com/flcn-x/items/c866eec8824a3cd70fa8  

- Pythonの仮想環境構築  
  - https://qiita.com/shun_sakamoto/items/7944d0ac4d30edf91fde  
  - https://packaging.python.org/ja/latest/guides/installing-using-pip-and-virtual-environments/  

- Pythonインストール時のエラー対応  
  - https://www.out48.com/archives/5720/#google_vignette  
  - （補足）Windows内蔵の`python.exe`との競合が原因と推測され、適切なバージョンのインストールで解決  

- GitHubのSSH通信設定  
  - https://zenn.dev/nikaera/articles/ssh-config-github  

- Pythonの予約システム参考コード  
  - https://ogatago.com/python-hospital-web-booking/  

