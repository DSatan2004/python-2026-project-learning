
class Gun:
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count = count

    def shoot(self):
        # 判断是否还有子弹
        if self.bullet_count <= 0:
            print("没有子弹了...")
            return

        self.bullet_count-=1
        print("%s 发射子弹[%d]..." % (self.model, self.bullet_count))

class Soldier:
    def __init__(self,name):
        self.name = name
        self.gun = None

    def fire(self):
        # 1。判断士兵是否有枪
        if self.gun is None:
            print("[%s] 还没有枪"%self.name)
            return

        # 2.高喊口号
        print("冲啊...[%s]" % self.name)

        # 3.让枪装填子弹
        self.gun.add_bullet(50)

        # 4.让枪发射子弹
        self.gun.shoot()

if __name__ == '__main__':
    # 1.创建枪对象
    ak47 = Gun("ak47")

    # 2.创建许三多
    xusanduo = Soldier("许三多")
    xusanduo.fire()
    xusanduo.gun = ak47
    xusanduo.fire()