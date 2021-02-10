import time


def time_exchange(time_s):
    time_s = int(time_s)
    s_second = "%02d" % (time_s % 60)
    time_s = time_s // 60
    s_minutes = "%02d" % (time_s % 60)
    time_s = time_s // 60
    s_hour = str(time_s)
    return s_hour + ":" + s_minutes + ":" + s_second


def get_time():
    now_time_tmp = time.time()
    return now_time_tmp


class ProcessBar:
    def __init__(self, process_tip='Processing', process_char='#', n=0):
        self.now_time = time.time()
        self.start_time = self.now_time
        self.last_k = 0
        self.speed = 0
        self.process_char = process_char
        self.process_tip = process_tip
        self.k = 0
        self.n = n

    def speed_cal(self, k):
        now_time_tmp = time.time()
        dalta_time = now_time_tmp - self.now_time
        if dalta_time <= 0:
            return 0
        dalta_k = k - self.last_k
        if dalta_time > 0.3:
            self.now_time = now_time_tmp
            self.last_k = k
        return dalta_k / dalta_time

    def cal_need_time(self, k, n):
        self.speed = self.speed_cal(k)
        if self.speed <= 0:
            return "0:00:00"
        need_time_s = int((n - k) / self.speed + 0.5)
        return time_exchange(need_time_s)

    def process_bar(self, k, n):
        bar_len = 30
        already_process = int((k / n) * bar_len)
        s_bar = "[" + str(self.process_char) * already_process + "-" * (bar_len - already_process) + "]"
        return self.process_tip + s_bar

    def bar_print(self, k, n):
        if k == n:
            print("\r" + "Done." + "\t" + time_exchange(self.now_time - self.start_time), end="\n", flush=True)
            return 0
        pre_s = str(k) + "/" + str(n)
        present = str(int((k / n) * 10000) / 100) + "%"
        s_need_time = self.cal_need_time(k, n)
        s_speed = " " + ("%.2f" % self.speed) + "/s"
        s_bar = self.process_bar(k, n)
        s_process = s_bar + "\t" + pre_s + "\t" + present + "\t" + s_need_time + "\t" + s_speed
        print('\r' + s_process, end='', flush=True)
        return 0

    def next(self):
        self.bar_print(self.k + 1, self.n)
        self.k += 1
