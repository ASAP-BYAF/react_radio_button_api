# 目次

- [使用技術](#technology-used)
- [環境構築](#build-environment)
- [実行方法](#how-to-run)

<h2 id="technology-used">使用技術</h2>

<!-- 言語、フレームワーク、ミドルウェア、インフラの一覧とバージョンを記載 -->

| 言語・フレームワーク | バージョン |
| -------------------- | ---------- |
| Python               | 3.11.4     |

<!-- シールド一覧 -->
<p style="display: inline">
  <!-- バックエンドのフレームワーク一覧 -->
  <!-- バックエンドの言語一覧 -->
  <img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge">
  <!-- ミドルウェア一覧 -->
  <!-- インフラ一覧 -->
</p>

<h2 id="build-environment">環境構築</h2>

```
pip3 install -r requirements.txt
```

<h2 id="how-to-run">実行方法</h2>

#### run local server

```
uvicorn api.main:app --reload

```
