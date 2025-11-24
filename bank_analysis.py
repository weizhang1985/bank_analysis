import math

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc("font", family='Microsoft Yahei')
import yfinance as yf


# 601398.SS 工商银行
# 601939.SS 建设银行
# 601288.SS 农业银行
# 601988.SS 中国银行
# 601658.SS 储蓄银行

# 601998.SS 中信银行
# 600036.SS 招商银行
# 601166.SS 兴业银行
# 000001.SZ 平安银行
# 600000.SZ 浦发银行
# 600015.SS 华夏银行
# 601916.SS 浙商银行
# 601818.SS 光大银行
# 600016.SS 民生银行


# 601628.SS 中国人寿
# 601988.SS 中国平安

idx_list = ['601398.SS', '601939.SS', '601288.SS', '601988.SS', '601658.SS',
            '601998.SS', '600036.SS', '601166.SS', '000001.SS', '600000.SS',
            '600015.SS', '601916.SS', '601818.SS', '600016.SS']

stock_list = ['工商银行收益', '建设银行收益', '农业银行收益', '中国银行收益', '储蓄银行收益',
              '中信银行收益', '招商银行收益', '兴业银行收益', '平安银行收益', '浦发银行收益',
              '华夏银行收益', '浙商银行收益', '光大银行收益', '民生银行收益']

kk = 0
print(stock_list[0])

for idx_name in idx_list:
    # k = k + 1
    # print(stock_list[kk-1])
    name = idx_name

    ticker = yf.Ticker(name)  # Apple Inc.

    # Step 2: Get historical data (last 1 month in this case)

    start_date = "1985-10-01"
    end_date = "2025-10-1"

    # Step 3: Get historical data for that range
    data = ticker.history(start=start_date, end=end_date)

    # Step 3: Reset the index so 'Date' becomes a column (not the index)
    data = data.reset_index()

    # Step 4: Select only the 'Date' and 'Close' columns

    data['Date'] = data['Date']
    date_df = data['Date']
    date_yy = date_df.dt.strftime("%Y")  # 4位年份
    date_mm = date_df.dt.strftime("%m")
    date_dd = date_df.dt.strftime("%d")
    data['Year'] = date_yy
    data['Month'] = date_mm
    data['Day'] = date_dd
    data['Date'] = data['Date'].dt.strftime("%Y%m%d")
    data_to_export = data[['Date', 'Year', 'Month', 'Day', 'Close']]

    # data_to_export_2015 = data_2015[['Date', 'Close']]

    # Step 5: Export to CSV
    export_file_name = name + '.csv'
    data_to_export.to_csv(export_file_name, index=False)

for idx_name in idx_list:

    name = idx_name + ".csv"
    print(name)
    print(stock_list[kk])
    df = pd.read_csv(name)
    date_df = pd.to_datetime(df['Date'])
    date_yy = date_df.dt.strftime("%Y") #4位年份
    date_mm = date_df.dt.strftime("%m")
    date_dd = date_df.dt.strftime("%d")

    print(date_yy, date_mm, date_dd)

    idx_value = df['Close'].to_numpy()
    idx_yy = df['Year'].to_numpy()
    idx_mm = df['Month'].to_numpy()
    idx_dd = df['Day'].to_numpy()

    temp_price = np.array([])
    temp_yy = np.array([])
    temp_mm = np.array([])
    temp_dd = np.array([])

    n_len = len(idx_value)  # add data to the system
    k = 0
    for i in range(n_len-1):
        _month_begin = idx_mm[i]
        _month_end = idx_mm[i]
        _year_begin = idx_yy[i]
        _year_end = idx_yy[i + 1]
        _day_begin = idx_dd[i]
        _day_end = idx_dd[i+1]

        if idx_dd[i + 1] - idx_dd[i] > 1:
            for j in range(idx_dd[i + 1] - idx_dd[i]):
                temp_price = np.append(temp_price, idx_value[i])
                temp_yy = np.append(temp_yy, _year_begin)
                temp_mm = np.append(temp_mm, _month_begin)
                temp_dd = np.append(temp_dd, _day_begin + j)
        elif idx_dd[i + 1] - idx_dd[i] < 0:
            if _year_begin == _year_end:
                if _month_begin == 1 or _month_begin == 3 or _month_begin == 5 or _month_begin == 7 or _month_begin == 8 \
                        or _month_begin == 10 or _month_begin == 12:
                    for j in range(idx_dd[i + 1] + 31 - idx_dd[i]):
                        if 31 - idx_dd[i] - j >= 0:
                            temp_price = np.append(temp_price, idx_value[i])
                            temp_yy = np.append(temp_yy, _year_begin)
                            temp_mm = np.append(temp_mm, _month_begin)
                            temp_dd = np.append(temp_dd, _day_begin + j)
                        else:
                            temp_price = np.append(temp_price, idx_value[i])
                            temp_yy = np.append(temp_yy, _year_begin)
                            temp_mm = np.append(temp_mm, _month_end)
                            temp_dd = np.append(temp_dd, _day_begin + j - 31)

                elif _month_begin == 2:
                    for j in range(idx_dd[i + 1] + 28 - idx_dd[i]):
                        if 28 - idx_dd[i] - j >= 0:
                            temp_price = np.append(temp_price, idx_value[i])
                            temp_yy = np.append(temp_yy, _year_begin)
                            temp_mm = np.append(temp_mm, _month_begin)
                            temp_dd = np.append(temp_dd, _day_begin + j)
                        else:
                            temp_price = np.append(temp_price, idx_value[i])
                            temp_yy = np.append(temp_yy, _year_begin)
                            temp_mm = np.append(temp_mm, _month_end)
                            temp_dd = np.append(temp_dd, _day_begin + j - 28)
                else:
                    for j in range(idx_dd[i + 1] + 30 - idx_dd[i]):
                        if 30 - idx_dd[i] - j >= 0:
                            temp_price = np.append(temp_price, idx_value[i])
                            temp_yy = np.append(temp_yy, _year_begin)
                            temp_mm = np.append(temp_mm, _month_begin)
                            temp_dd = np.append(temp_dd, _day_begin + j)
                        else:
                            temp_price = np.append(temp_price, idx_value[i])
                            temp_yy = np.append(temp_yy, _year_begin)
                            temp_mm = np.append(temp_mm, _month_end)
                            temp_dd = np.append(temp_dd, _day_begin + j - 30)
            else:
                for j in range(idx_dd[i + 1] + 31 - idx_dd[i]):
                    if 31 - idx_dd[i] -j >= 0:
                        temp_price = np.append(temp_price, idx_value[i])
                        temp_yy = np.append(temp_yy, _year_begin)
                        temp_mm = np.append(temp_mm, _month_begin)
                        temp_dd = np.append(temp_dd, _day_begin + j)
                    else:
                        temp_price = np.append(temp_price, idx_value[i])
                        temp_yy = np.append(temp_yy, _year_end)
                        temp_mm = np.append(temp_mm, _month_end)
                        temp_dd = np.append(temp_dd, _day_begin + j - 31)
        else:
            temp_price = np.append(temp_price, idx_value[i])
            temp_yy = np.append(temp_yy, _year_end)
            temp_mm = np.append(temp_mm, _month_end)
            temp_dd = np.append(temp_dd, _day_begin)

    df = pd.DataFrame(columns=['Date', 'Year', 'Month', 'Day', 'Price'])

    df['Year'] = temp_yy
    df['Month'] = temp_mm
    df['Day'] = temp_dd
    df['Price'] = temp_price
    df['Date'] = temp_yy*10000 + temp_mm*100 + temp_dd

    idx_value = df['Price'].to_numpy()
    idx_yy = df['Year'].to_numpy()
    idx_mm = df['Month'].to_numpy()
    idx_dd = df['Day'].to_numpy()
    idx_date = df['Date'].to_numpy()

    temp_price = np.array([])
    temp_yy = np.array([])
    temp_mm = np.array([])
    temp_dd = np.array([])

    n_len = len(idx_value)  # add data to the system
    ##
    cap_day = 1
    cap_week = 7
    sum_day = np.zeros((n_len, 1))
    sum_week = np.zeros((round(n_len/5), 1))

    for i in range(n_len-1):
        print(df['Date'][i], sum_day[i, 0], idx_value[i+1])
        if i == 0:
            sum_day[1] = cap_day
            idx_old = idx_value[i+1]
        else:
            idx_new = idx_value[i+1]
            sum_day[i+1] = sum_day[i] * idx_new / idx_old + cap_day
            idx_old = idx_new

    # Calculate return

    df['Return'] = sum_day[:, 0]
    max_return = max(sum_day[:, 0])
    apr = 2/100/365
    print(n_len)
    end_return = sum_day[n_len-1, 0]
    for i in range(10000):
        temp = (1 - math.pow(1+apr, n_len-1))/(- apr)
        if abs((end_return - temp)) / end_return * 100 < 0.1:
            break
        else:
            apr = apr + 1/365/10000
    df['Apr'] = apr * 365 * 100
    name_return = "Return_" + name
    df.to_csv(name_return)

    # x = [-100, n_len+1000, n_len+1000, 0]
    # y = [-100, -100, max_return*1.1, max_return*1.1]
    # plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10.5, 6))
    plt.title(stock_list[kk], font={'family': 'Microsoft Yahei', 'size': 18})
    kk = kk + 1
    plt.ylabel('总投资收益', font={'family': 'Microsoft Yahei', 'size': 16})
    plt.xlabel('投资天数', font={'family': 'Microsoft Yahei', 'size': 16})
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True, color='brown', linewidth=0.5, linestyle='--')
    plt.text(n_len-1+200, end_return-2000, (n_len-1, round(end_return)), fontweight='bold', fontsize=18, color='red', ha='center')

    plt.plot(sum_day[:, 0], color='black', linewidth=3)
    save_name = name + '.png'
    plt.savefig(save_name)

    # fig, ax = plt.subplots()
    # fig.set_facecolor('lightblue')
    # ax.plot(sum_day[:, 0])
   # plt.fill(x, y, color='blue')
    # plt.figure(facecolor='lightgray')
    # plt.show()

4

# Access specific columns

