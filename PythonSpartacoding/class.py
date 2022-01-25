class Monster():
    hp = 100
    alive = True

    def damage(self, attack):
        self.hp = self.hp - attack
        if self.hp < 0:
            self.alive = False

    def status_check(self):
        if self.alive:
            print('살아있다')
        else:
            print('죽었다')

m = Monster()
m.damage(120)

m2 = Monster()
m2.damage(90)

m.status_check()
m2.status_check()