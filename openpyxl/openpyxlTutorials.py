import datetime
import calendar

nowdate = datetime.datetime.now() + datetime.timedelta(12)

def add_month(indate: datetime, add: int) -> int:
  """
  :param indate: Data początkowa. Ten argument jest potrzebny ze wzgledu na potrzebe znajomości kolejnych miesięcy
  :param add: Ile miesięcy należy dodać do daty początkowej
  :return: Obliczona ilość dni zawartych w kolejnych miesiącach, które będą dodane
  """
  count_day: int = 0  # Ile dni trzeba dodać
  month: int = indate.month
  year: int = indate.year

  for ilicz in range(1, add + 1):
    # print("{}".format(calendar.monthrange(year, month)[1]))
    new_month = month + ilicz

    if new_month > 12:
      month = new_month - 12
      count = calendar.monthrange(year, month)[1]
      count_day += count
      print("!! new_month: {}, count: {}".format(month, count))
    else:
      count = calendar.monthrange(year, new_month)[1]
      count_day += count
      print("new_month: {}, count: {}".format(new_month, count))

  return count_day

c_day = add_month(nowdate, 12)

new_date = nowdate + datetime.timedelta(c_day)
print("count_day: {}, nowdate: {} - new_date: {}".format(c_day, nowdate, new_date))
