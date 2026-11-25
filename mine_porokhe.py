class Splitwise_Alternative:
    def __init__(self,makan,nam1,nam1p,nam2,nam2p,nam3,nam3p):
        self.teem =nam1,nam2,nam3
        self.makan =makan
        self.nam1p =nam1p
        self.nam3p =nam3p
        self.nam2p =nam2p
        self.nam1 =nam1
        self.nam3 =nam3
        self.nam2 =nam2
    if self.makan =="hotel":
        dastor =input("dastor:")
        if dastor =="neshandadanghasm ha":
            print("ghza",self.nam1)
            print("hml",self.nam2)
            print("otagh",self.nam3)
        elif dastor =="taghsem":
            self.nam1p -=1200000
            self.nam2p -=3000000
            self.nam3p -=10000000
    elif self.makan =="kamp":
        dastor =input("dastor:")
        if dastor =="neshandadanghasm ha":
            print("ghza",self.nam1)
            print("hml",self.nam2)
            print("otagh",self.nam3)
        elif dastor =="taghsem":
            self.nam1p -=12000
            self.nam2p -=30000
            self.nam3p -=100000
        