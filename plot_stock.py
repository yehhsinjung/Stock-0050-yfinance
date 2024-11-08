import matplotlib.pyplot as plt

def stock_trend (historical_data, stock_code):
    
    plt.figure(figsize=(10, 6))
    plt.title(f"{stock_code} Bollinger band")
    plt.xlabel('Date')
    plt.ylabel('Price')
  
    plt.grid(True)#設定網格

    #畫出收盤價、上軌、下軌
    plt.plot(historical_data['Date'], historical_data['Close'], label='Close', color='blue')
    plt.plot(historical_data['Date'], historical_data['Upper Band'], label='Upper Band', color='red')
    plt.plot(historical_data['Date'], historical_data['Lower Band'], label='Lower Band', color='green')
    # 填充布林通道內上下軌間區域，凸顯股價變化
    plt.fill_between(historical_data['Date'], historical_data['Upper Band'], historical_data['Lower Band'],
                     color='lightgray', alpha=0.4)
  
    #將 x 軸上的所有標籤旋轉 45 度，避免重疊
    plt.xticks(rotation=45, ha='right')

    #自動調整圖表元素以免重疊
    plt.tight_layout()
    plt.show()
