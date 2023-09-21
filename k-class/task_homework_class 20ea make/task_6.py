class Bookstore:
    # 책이름, 책 가격, 책 재고

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, customer):
        discount_price = self.price - (self.price * customer.discount * 0.01)
        customer.money = int(discount_price)
        self.stock -= 1




class Customer:
        # 고객명, 회원 타입, 할인율(10%)
    def __init__(self, name, customer_type, discount, money):
        self.name = name
        self.customer_type = customer_type
        self.discount = discount
        self.money = money
        # if customer_type == "정회원" :

customer = Customer('주현진', "정회원", 10, 50000)
bookstore = Bookstore("노인과 바다", 15000, 15)

bookstore.sell(customer)
print(customer.money)

# 왜 1500원이 빠진 다음 출력이 되었는가?? => 15000원에서 10% 할인이 된 가격 인듯?
