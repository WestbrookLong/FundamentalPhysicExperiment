import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from scipy.stats import norm
import numpy as np

# 您的数据
data = [

]

# 将数据转换为 Pandas DataFrame
df = pd.DataFrame(data, columns=['Value'])

# 计算统计量
count = df['Value'].count()
mean = round(df['Value'].mean(), 2)
std = round(df['Value'].std(), 2)
max_value = round(df['Value'].max(), 2)
min_value = round(df['Value'].min(), 2)
median = round(df['Value'].median(), 2)
range_value = round(df['Value'].max() - df['Value'].min(), 2)

# 输出统计量
print(f"数据个数: {count}")
print(f"平均值: {mean}")
print(f"标准差: {std}")
print(f"最大值: {max_value}")
print(f"最小值: {min_value}")
print(f"中间值（中位数）: {median}")
print(f"范围: {range_value}")

# 设置字体属性
font = FontProperties(fname='C:/Windows/Fonts/simhei.ttf')  # Windows 系统使用

# 绘制频率分布直方图
plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(df['Value'], bins=15, color='skyblue', edgecolor='black', density=True, alpha=0.6)

# 标注每个频率
for patch, frequency in zip(patches, n):
    if frequency > 0:
        plt.text(patch.get_x() + patch.get_width() / 2., patch.get_height(),
                 f'{frequency:.2f}', ha='center', va='bottom', fontproperties=font)

# 计算正态分布曲线
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std)
plt.plot(x, p, 'k', linewidth=2, label=r'Fit: $\mu$={:.2f}, $\sigma$={:.2f}'.format(mean, std))

# 计算区间中值并代入正态分布函数
bin_centers = 0.5 * (bins[:-1] + bins[1:])  # 区间中值
bin_centers_pdf = norm.pdf(bin_centers, mean, std)  # 区间中值对应的正态分布概率密度值

# 在图中绘制这些点
plt.scatter(bin_centers, bin_centers_pdf, color='red', zorder=5, label='Bin Centers')

plt.xlabel('时间/s', fontproperties=font)
plt.ylabel('Frequency', fontproperties=font)
plt.title('Frequency Distribution Histogram with Normal Fit', fontproperties=font)
plt.legend()
plt.grid(True)
plt.show()
