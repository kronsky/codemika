from datetime import datetime


def input_date():
    return datetime.timestamp(datetime(int(input('Год: ')), int(input('Месяц: ')), int(input('Число: ')),
                                       int(input('Час: ')), int(input('Минута: ')), int(input('Секунда: '))))


class Timerange(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.duration = end - start

    def get_duration(self):
        print(self.duration)

    def edit_start(self):
        print('Введите начало диапазона')
        start = input_date()
        if start < self.end:
            self.duration = self.end - start
        else:
            print('Начало диапазона времени не может наступить позднее окончания')

    def edit_end(self):
        print('Введите конец диапазона')
        end = input_date()
        if self.start < end:
            self.duration = end - self.start
        else:
            print('Окончание диапазона времени не может наступить раньше начала')


print('Введите начало диапазона')
tstart = input_date()
print('Введите конец диапазона')
tend = input_date()

timerange = Timerange(tstart, tend)

# смотрим длительность
timerange.get_duration()
# меняем начало диапазона
timerange.edit_start()
# смотрим длительность
timerange.get_duration()
#  меняем конец диапазона
timerange.edit_end()
# смотрим длительность
timerange.get_duration()
