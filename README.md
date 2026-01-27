# FastAPI Logging Sample

## 概要
FastAPI ログ設計サンプル。

- JSON ログ出力
- Request-ID を発行し出力
- アクセスログ、エラーログを出力
- エラーログにはスタックトレースを含む
- ログ取得 API（期間指定）
- テスト付き（pytest）

## 起動方法

```bash
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```
http://127.0.0.1:8000/docs

## テスト

```bash
python -m pytest
```

# Note
 
現状試作品です。
今後改良していく予定。
 
# Author
 
* 作成者 阿座上 英治
* 所属 　株式会社Ｌ．Ｓ．Ｅ
 
## 📝 License

MIT License  
Copyright (c) 2026 L.S.E Eiji.Azakami

This project is licensed under the MIT License.  
See the [LICENSE](https://en.wikipedia.org/wiki/MIT_License) file for details.
