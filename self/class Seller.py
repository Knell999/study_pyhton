class Seller:
    def __init__(self, name, email, seller_number):
        self.name = name
        self.email = email
        self.seller_number = seller_number

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Seller Number: {self.seller_number}"
    
seller = Seller("Kim", "crazy@gmail.com", "123456")

print("이름", "\t", "이메일", "\t", "판매자 번호")
print(seller.name, "\t", seller.email, "\t", seller.seller_number)