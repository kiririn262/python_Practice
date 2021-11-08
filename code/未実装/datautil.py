from dateutil.relativedelta import relativedelta
today = datetime.date.today()
print(today)
print(today + relativedelta(months=+3))