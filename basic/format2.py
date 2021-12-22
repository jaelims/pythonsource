# format() 함수 - {} 사용
print("{} and {}".format('You', "Me"))
print("{0} and {1}".format('You', "Me"))
print("{0} and {1} and {0}".format('You', "Me"))
print("{var1} and {var2}".format(var1='You', var2="Me"))
print("I ate {0} apples. so I was sick for {day} days".format(20, day=3))
print()
print("Test1 : {0: 5d}, Price : {1: 4.2f}".format(776, 6534.123))
print("Test1 : {a: 5d}, Price : {b: 4.2f}".format(a=776, b=6534.123))

