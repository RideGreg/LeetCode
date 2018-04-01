class MyCalendar(object):

    def __init__(self):
        self.booked = []


    def book(self, start, end):
        valid = 1
        for b in self.booked:
            s, e = b[0], b[1]
            if not ((start < s and end-1 < s) or (start > e and end-1 > e)):
                valid = 0
                break
        if valid:
            self.booked.append([start, end-1])
            return True
        else:
            return False

obj = MyCalendar(
)
print obj.book(10,20)
print obj.book(15,25)
print obj.book(20,30)


