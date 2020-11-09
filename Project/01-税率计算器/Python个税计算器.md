##### Python个税计算器

----

扣税计算器

税率表格

| 级数 | 累计预扣预缴应纳税所得额 | 税率（%） | 速算扣除数 |
| :--: | :----------------------: | :-------: | :--------: |
|  1   |       不超过36000        |     3     |     0      |
|  2   | 超过36000至144000的部分  |    10     |    2520    |
|  3   | 超过144000至300000的部分 |    20     |   16920    |
|  4   | 超过300000至420000的部分 |    25     |   31920    |
|  5   | 超过420000至660000的部分 |    30     |   52920    |
|  6   | 超过660000至960000的部分 |    35     |   85920    |
|  7   |     超过960000的部分     |    45     |   181920   |

个税起征点为5000

```
一种简单的公式（不完整）
累计扣税额 = （累计工资-5000*月份）* 对应税率 - 速算扣除数
应缴扣税 = 累计扣税额 -  已缴税额
```

```python
# 计算税后工资
def tax_rate(salary):
    if salary <= 0:
        return 0
    elif salary <= 36000:
        return 0.03 * salary - 0
    elif salary <= 144000:
        return 0.1 * salary - 2520
    elif salary <= 300000:
        return 0.2 * salary - 16920
    elif salary <= 420000:
        return 0.25 * salary - 31920
    elif salary <= 660000:
        return 0.3 * salary - 52920
    elif salary <= 960000:
        return 0.35 * salary - 85920
    else:
        return 0.45 * salary - 181920

salary = int(input('请输入您的月薪：'))
qizhengdian = 5000      # 起征点
yijiao_tax = 0          # 存储应缴税额
for month in range(1,13):
    leiji_salary = salary*month         #累计工资=月工资*月份
    yingjiao_salary = leiji_salary-qizhengdian*month    # 应缴税工资=累计工资-起征点*月份
    yingjiao_tax = tax_rate(yingjiao_salary)-yijiao_tax # 应缴税 = 累计应缴税-已缴税
    yijiao_tax += yingjiao_tax      # 已缴税等于前几个月份的总缴税
    print('{}月您需要缴税{}元,税后收入{}元'.format(month,yingjiao_tax,salary-yingjiao_tax))
```





