class goda():
    def __init__(self, year):
        
        self.year = year

    def raschet(self):
        if self.year%4==0 and self.year%100!=0 or self.year%400==0:
            print("Високосный год!")
        else:
            print("Этот год не високосный!")
        
gf = goda(2016)
ga = goda(2015)
gf.raschet()
ga.raschet()