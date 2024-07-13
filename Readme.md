# 訂單處理API

## 程式碼架構

```plaintext
.
├── app/
│   ├── __init__.py              # 初始化程式
│   ├── config.py                # config 設定
│   ├── main.py                  # FastAPI 主程式
│   ├── schemas.py               # Pydantic 模型定義
│   ├── services/                # 服務模組
│   │   ├── __init__.py          # 初始化程式
│   │   ├── currency_service.py  # 貨幣轉換服務
│   │   └── order_service.py     # 訂單處理服務
│   ├── transformers/            # 轉換模組
│   │   ├── __init__.py          # 初始化程式
│   │   └── order_transformer.py # 訂單轉換
│   └── validators/              # 驗證模組
│       ├── __init__.py          # 初始化程式
│       └── order_validator.py   # 訂單驗證
├── tests/
│   ├── __init__.py              # 初始化程式
│   └── test_main.py             # API 測試
├── Dockerfile                   # Docker 設定檔
├── README.md                    # 專案說明文件
└── requirements.txt             # 依賴包列表



## 主要功能

1. 新增訂單: POST /api/orders
2. 自動驗證訂單資料
3. 自動將美金轉換為台幣


## 使用的 SOLID 原則

這個專案運用了以下 SOLID 原則:

1. Single-responsibility principle:
   - 每個類別只負責一件事。例如 `OrderValidator` 只負責驗證訂單資料。

2. Open–closed principle:
   - 使用依賴注入,讓我們可以輕鬆擴展功能而不用改動現有程式碼。

3. Liskov substitution principle:
   - 但我們的設計允許使用子類別替換父類別。

4. Interface segregation principle:
   - 每個介面都很精簡。像是 `OrderValidator` 只有一個 `validate` 方法。

5. Dependency inversion principle:
   - 高層模組不直接依賴低層模組,而是依賴抽象。例如 `create_order` 依賴於 `OrderValidator` 和 `OrderTransformer` 的抽象。

## 使用的設計模式

這個專案也用了一些設計模式:

1. Strategy Pattern:
   - `OrderValidator` 和 `OrderTransformer` 可以視為不同的策略,允許在執行期間切換不同的驗證或轉換策略。

2. Factory Pattern:
   - FastAPI的 `Depends` 扮演了工廠的角色,幫我們建立需要的物件。

3. Singleton Pattern:
   - `get_settings` 方法使用了 `lru_cache` decorator,確保只建立一個 `Settings` 實例。


## 如何使用

### 從GitHub下載並執行

1. 先把專案clone下來:
git clone https://github.com/TseAnLin/AsiaYo_API_Test.git
cd AsiaYo_API_Test

2. 建立Docker image:
docker build -t fastapi-app .

3. 執行Docker Container:
docker run -d -p 8000:8000 fastapi-app

3. 打開瀏覽器並輸入 `http://localhost:8000/docs` 就可以使用API了


### 測試

1. 進入容器內部
docker exec -it fastapi-container /bin/sh

2. 進行測試
pytest tests/
