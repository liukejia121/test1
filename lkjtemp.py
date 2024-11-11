import pandas as pd

# 读取CSV文件
dirf_csv = r"D:/0_ds/SkyScript_cls/img_txt_pairs_val_all.csv"
df = pd.read_csv(dirf_csv)

# 只取前10行
df_top10 = df.head(128)

# 将结果另存为新的CSV文件
dirf_csv2 = r"D:/0_ds/SkyScript_cls/img_txt_pairs_val.csv"

df_top10.to_csv(dirf_csv2, index=False)

def test_print():
    print('--lkjtemp.py/test_print() is called.')



"""
# 基本用法是使用一个for循环迭代一个列表或生成式来更新进度条的状态
import time
from tqdm import tqdm

lst = ['item1', 'item2', 'item3']

for i in tqdm(lst):
    time.sleep(1)
    print(i)

# 在诸如模型训练这样的大型计算任务中的嵌套循环使用
import time
from tqdm import tqdm

for epoch in range(4):
    pbar = tqdm(total=200)
    for i in range(100):
        # do something
        time.sleep(0.0001)
        pbar.update(1)
    pbar.close()
    
# 此外,tqdm支持设置描述、后缀等来个性化进度条。比如:

for i in tqdm(range(100), desc="Training", postfix={'batches': 5}):
   # training code here

"""
