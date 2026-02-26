# FastAPI Logging Sample

## 概要
FastAPI ロギングサンプル

- JSON ログ出力
- Request-ID を発行し出力
- アクセスログ、エラーログを出力
- エラーログにはスタックトレースを含む
- ログ取得 API（期間指定）
- テスト付き（pytest）

## Demo
Cloud Run サーバーレス構成サンプル<br>
https://fastapilogging-347911280466.asia-northeast1.run.app/docs

## 起動方法

pythonコマンドは環境によって「python3」だったり、「python」、「py」だったりするようです。<br>
お使いの環境に合わせてコマンドを変更してください。

```bash
python3 -m venv venv
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# Windows (cmd.exe)
venv\Scripts\activate.bat
pip install -r requirements.txt
uvicorn app.main:app --reload --no-access-log
```

## 起動後
- Swagger UI: http://127.0.0.1:8000/docs
- Redoc:        http://127.0.0.1:8000/redoc

## テスト

```bash
python -m pytest
```

# Note
 
現状試作品です。<br>
今後改良していく予定。<br>
Uvicorn のデフォルトアクセスログは無効にしてます。
 
# Author
 
* 作成者 阿座上 英治
* 所属 　株式会社Ｌ．Ｓ．Ｅ
 
## 📝 License

MIT License  
Copyright (c) 2026 L.S.E Eiji.Azakami

This project is licensed under the MIT License.  
See the [LICENSE](https://en.wikipedia.org/wiki/MIT_License) file for details.
