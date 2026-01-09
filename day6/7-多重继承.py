
class A:
    def test(self):
        print('A test')

    def demo(self):
        print('A demo')

class B:
    def test(self):
        print('B test')

    def demo(self):
        print('B demo')

class C(A,B):
    def test(self):
        print('C test')

if __name__ == '__main__':
    c = C()
    c.test()
    print(C.__mro__)