#把1.csv中“email”列的邮箱地址与2.csv中的“邮箱地址”列进行匹配，并将匹配的2.处所中的对应行写入与2.csv表头相同的3.csv中。

import pandas as pd

# 1. 检查列名（新增调试步骤）
df2 = pd.read_csv('2.csv')
print("2.csv的列名列表:", df2.columns.tolist())  # 关键调试语句[1](@ref)

# 2. 修正列名（根据实际列名调整）
correct_col_name = '邮件地址'  # 示例可能存在的真实列名，需根据实际打印结果修改

# 3. 读取数据时统一处理列名
df1 = pd.read_csv('1.csv', usecols=['email'])
df2 = pd.read_csv('2.csv').rename(columns={correct_col_name: '邮箱地址'})  # 列名标准化[1,17](@ref)

# 4. 添加列名存在性验证
if '邮箱地址' not in df2.columns:
    raise ValueError("2.csv缺少邮箱地址列，检测到现有列名为：" + str(df2.columns))

# 后续代码保持不变...
email_set = set(df1['email'].dropna().unique())
matched_df = df2[df2['邮箱地址'].isin(email_set)]
matched_df.to_csv('3.csv', index=False, encoding='utf-8-sig')
