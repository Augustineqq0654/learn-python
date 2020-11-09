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


