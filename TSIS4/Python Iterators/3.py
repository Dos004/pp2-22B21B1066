class MyNumbers():
    def __iter__(self): # создает переиенную(инициализирует) и дает значение 1
        self.a = 1
        return self
    
    def __next__(self):  # работает как цикл 
        x = self.a  # х = 1 , х = 2
        self.a += 1 # а = 1 + 1, а = 2 + 1
        return x    # х = 1 , х = 2
    
myclass = MyNumbers()
my_iter = iter(myclass)


for i in range(int(input())):
    print(next(my_iter),sep=' ',end=' ')
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))