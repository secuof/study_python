class honghouse:
    lastname = "홍"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s여행을 가다." % (self.fullname, where))
    def love(self, other):
        print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))
    def fight(self, other):
        print("%s, %s 싸우네" % (self.fullname, other.fullname))
    def __add__(self, other):
        print("%s, %s 결혼했네" % (self.fullname, other.fullname))
    def __sub__(self, other):
        print("%s, %s 이혼했네" % (self.fullname, other.fullname))


class kimhouse(honghouse):
    lastname = "김"
    def travel(self, where, day):
        print("%s, %s 여행 %d일 가네." % (self.fullname, where, day))

me = honghouse("로미오")
wife = kimhouse("줄리엣")
me.travel("부산")
wife.travel("부산", 3)
me.love(wife)
me.fight(wife)
me + wife
me - wife