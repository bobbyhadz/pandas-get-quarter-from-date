# How to get a Quarter from a Date in Pandas

import pandas as pd

df = pd.DataFrame({
    'Name': [
        'Alice',
        'Bobby',
        'Carl'
    ],
    'Date': [
        '2023-01-12',
        '2023-05-23',
        '2023-09-21'
    ]
})

df['quarter'] = pd.PeriodIndex(df['Date'], freq='Q')

#     Name        Date quarter
# 0  Alice  2023-01-12  2023Q1
# 1  Bobby  2023-05-23  2023Q2
# 2   Carl  2023-09-21  2023Q3
print(df)