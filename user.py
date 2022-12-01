class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Is Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        return self

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        self.gold_card_points -= amount
        return self

user_1 = User("Kevin", "Moore", "kevinmoore444@gmail.com", 36)
user_2 = User("John", "Doe", "johndoe123@gmail.com", 40)

user_1.enroll().display_info()
user_2.enroll().spend_points(100).display_info()
