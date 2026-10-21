
import yfinance as yf
import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo

# Danh sách mã cổ phiếu Mỹ
symbols = ["AAPL", "TSLA", "NVDA", "MSFT"]

rows = []

for symbol in symbols:
    try:
        df = yf.Ticker(symbol).history(period="5d", interval="1d")

        if df.empty:
            print(f"Khong co du lieu: {symbol}")
            continue

        latest = df.iloc[-1]

        rows.append({
            "symbol": symbol,
            "date": str(df.index[-1].date()),
            "close": round(float(latest["Close"]), 2),
            "volume": int(latest["Volume"]),
            "updated_at": datetime.now(
                ZoneInfo("Asia/Ho_Chi_Minh")
            ).strftime("%Y-%m-%d %H:%M:%S")
        })

    except Exception as e:
        print(f"Loi {symbol}: {e}")

if rows:
    pd.DataFrame(rows).to_csv(
        "stocks.csv", index=False, encoding="utf-8-sig"
    )
    print("Da cap nhat stocks.csv")
else:
    raise RuntimeError("Khong lay duoc du lieu co phieu")
