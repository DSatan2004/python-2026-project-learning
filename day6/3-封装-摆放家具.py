
class HouseItem:
    def __init__(self,name,area,):
        """
        初始化方法
        :param name: 家具名字
        :param area: 占地面积
        """
        self.name = name
        self.area = area

    def __str__(self):
        return f"[{self.name}]占地{self.area}平方米"

class House:
    def __init__(self,house_type,area):
        """
        初始化方法,房子类
        :param house_type:
        :param area:
        """
        self.house_type = house_type
        self.area = area
        self.free_area = area # 空余面积
        self.items_list = [] # 家具列表

    def __str__(self):
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.items_list))

    def add_item(self, item:HouseItem):# 通过冒号加对象类型，加注解
        if item.area > self.free_area:
            print('房子没空间了，放家具失败')
            return
        self.free_area -= item.area
        self.items_list.append(item.name)


if __name__ == '__main__':
    bed = HouseItem("席梦思", 4)
    chest = HouseItem("衣柜", 2)
    table = HouseItem("餐桌", 1.5)

    print(bed)
    print(chest)
    print(table)

    house = House("两室一厅", 30)
    house.add_item(bed)
    house.add_item(chest)
    house.add_item(table)

    print(house)

