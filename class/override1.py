# 오버로딩 : 한 클래스 내에서 동일한 이름으로 메소드, 생성자가 존재
#            ()안에 인자의 개수가 다르거나, 타입이 다르거나...
#            파이썬에서 오버로딩은 기본값을 이용한 형태로 구현

# 오버라이딩 : 상속에서 사용
#              부모 클래스와 동일한 메소드가 자식 클래스에 존재
#              부모가 넘겨주는 메소드를 재정의

# 오버라이딩
# class Parent:
#     def func1(self):
#         print("Parent의 func1() 실행")

#     def func2(self):
#         print("Parent의 func2() 실행")


# class Child(Parent):
#     def func1(self):
#         print("Child의 func1() 실행")

#     def func3(self):
#         print("Child의 func3() 실행")


# parent, child = Parent(), Child()
# parent.func1()
# child.func1() # Child의 func1() 실행
# child.func2()
# child.func3()


class Car:

    speed = 0

    def up_speed(self, value):
        self.speed += value

        print("현재 속도(슈퍼클래스) : %d" % self.speed)

    def down_speed(self, value):
        self.speed -= value


class Sedan(Car):

    seat_num = 0

    def up_speed(self, value):
        self.speed += value

        if self.speed > 150:
            self.speed = 150
            print("현재 속도(자식클래스) : %d" % self.speed)

    def getSeatNum(self):
        return self.seat_num


sedan = Sedan()

sedan.up_speed(100)
sedan.seat_num = 5
sedan.up_speed(300)
