class MyCalendar(object):

    def __init__(self):
        self.booked = []
        self.dup = []


    def book(self, start, end):
        valid = 1
        for d in self.dup:
            if not ((start < d[0] and end-1 < d[0]) or (start > d[1] and end-1 > d[1])):
                valid = 0
                break

        if valid:
            for b in self.booked:
                s, e = b[0], b[1]
                o_s, o_e = max(s, start), min(e, end - 1)
                if o_s > o_e:
                    continue
                self.dup.append([o_s, o_e])

            self.booked.append([start, end-1])
            return True
        else:
            return False


Code


class MyCalendarTwo_friday21:
    def __init__(self):
        self.booked_time = {}
        self.double_booked = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if end <= start:
            return False
        for key2, value2 in self.double_booked:
            if value2 <= start or key2 >= end:
                continue
            if start >= key2 and start < value2:
                return False
            if end - 1 >= key2 and end - 1 < value2:
                return False
            if key2 >= start and value2 <= end:
                return False

        for key, value in self.booked_time.items():
            if isinstance(key, str):
                key = int(key)

            if value <= start or key >= end:
                continue
            if start >= key and start < value:
                self.double_booked.append((start, min(value, end)))
            elif end - 1 >= key and end - 1 < value:
                self.double_booked.append((max(start, key), end))
            elif key >= start and value <= end:
                self.double_booked.append((key, value))

        if start in self.booked_time:
            start = str(start)
        self.booked_time[start] = end
        return True

obj = MyCalendar(
)
for i, d in enumerate([[47,50],[1,10],[27,36],[40,47],[20,27],[15,23],[10,18],[27,36], \
          [17,25],[8,17],[24,33],[23,28],[21,27],[47,50],[14,21],[26,32], \
          [16,21],[2,7],[24,33],[6,13],[44,50],[33,39],[30,36],[6,15],\
          [21,27],[49,50],[38,45],[4,12],[46,50],[13,21]], 1):
#for i, d in enumerate([[20,27], [15,23],[17,25]]):
    print obj.book(d[0],d[1])
    if i%5==0:
        print "\n"

'''
print obj.book(50,60)
print obj.book(10,40)
print obj.book(5,15)
print obj.book(5,10)
print obj.book(25,55)

'''
