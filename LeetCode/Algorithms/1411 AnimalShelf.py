# 【简单】1411. 面试题 03.06. 动物收容所
# 动物收容所。有家动物收容所只收容狗与猫，且严格遵守“先进先出”的原则。
# 在收养该收容所的动物时，收养人只能收养所有动物中“最老”（由其进入收容所的时间长短而定）的动物，或者可以挑选猫或狗（同时必须收养此类动物中“最老”的）。
# 换言之，收养人不能自由挑选想收养的对象。请创建适用于这个系统的数据结构，实现各种操作方法，比如enqueue、dequeueAny、dequeueDog和dequeueCat。
# 允许使用Java内置的LinkedList数据结构。
# enqueue方法有一个animal参数，animal[0]代表动物编号，animal[1]代表动物种类，其中 0 代表猫，1 代表狗。
# dequeue*方法返回一个列表[动物编号, 动物种类]，若没有可以收养的动物，则返回[-1,-1]。


class AnimalShelf:

    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal) -> None:
        if animal[1] == 0: self.cats.append(animal)
        else: self.dogs.append(animal)

    def dequeueAny(self):
        if len(self.cats) > 0 and len(self.dogs) > 0:
            if self.cats[0][0] < self.dogs[0][0]: return self.cats.pop(0)
            else: return self.dogs.pop(0)
        elif len(self.cats) > 0: return self.cats.pop(0)
        elif len(self.dogs) > 0: return self.dogs.pop(0)
        else: return [-1, -1]

    def dequeueDog(self):
        return self.dogs.pop(0) if len(self.dogs) > 0 else [-1, -1]
        
    def dequeueCat(self):
        return self.cats.pop(0) if len(self.cats) > 0 else [-1, -1]
        



# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()