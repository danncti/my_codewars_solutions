class User:
    rank = -8
    progress = 0

    def inc_progress(self, act):

        print(act - (act > 0) - self.rank + (self.rank > 0))
        if not (-8 <= act <= 8 and act != 0): raise ValueError('Error')

        i = (act - self.rank)
        if act > 0 and self.rank < 0: i -= 1
        elif self.rank > 0 and act < 0: act +=1
        p = 0
        if act == self.rank: p = 3
        elif act + 1 == self.rank: p = 1
        elif act > self.rank: p = (10 * i * i)
        self.set_rank(p)

    def set_rank(self, p = 0):
        self.progress += p

        if self.rank == 8:
            self.progress = 0
        elif self.progress >= 100:
            if self.rank < 8: self.rank += 1
            if self.rank == 0: self.rank = 1
            self.progress -=100
            self.set_rank()
        return




user = User()
# user.inc_progress(0)
user.inc_progress(-4)
# user.inc_progress(-6)
# user.inc_progress(-5)
# user.inc_progress(-4)