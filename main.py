import os
import datetime as dt


class Client:
    def __init__(self, name):
        self.name = name

    def initials(self):
        if not os.path.exists("data/clients.txt"):
            os.mkdir("data")
            file = open("data/clients.txt", "w")
            file.close()
        with open("data/clients.txt") as file:
            contents = file.readlines()
            if f"{self.name}\n" not in contents:
                with open("data/clients.txt", "a") as file:
                    file.write(f"{self.name}\n")
            else:
                print("Welcome back existing user!")

    def log(self):
        inp = int(input("Enter 1 for logging food, 2 for exercise: "))
        if inp == 1:
            food = input("Enter the food: ")
            if not os.path.exists(f"data/{self.name}_food.txt"):
                file = open(f"data/{self.name}_food.txt", "w")
                file.close()
            with open(f"data/{self.name}_food.txt", "a") as file:
                current_time = dt.datetime.now()
                modify_time = current_time.strftime("%d %b %Y %H:%M:%S")
                file.write(f"{modify_time} - {food}\n")
        elif inp == 2:
            exercise = input("Enter the exercise: ")
            if not os.path.exists(f"data/{self.name}_exercise.txt"):
                file = open(f"data/{self.name}_exercise.txt", "w")
                file.close()
            with open(f"data/{self.name}_exercise.txt", "a") as file:
                current_time = dt.datetime.now()
                modify_time = current_time.strftime("%d %b %Y %H:%M:%S")
                file.write(f"{modify_time} - {exercise}\n")
        else:
            raise ValueError("You did something inappropriate.")


newClient = Client(input("Enter your name: "))

if __name__ == "__main__":
    newClient.initials()
    newClient.log()
