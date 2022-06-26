class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def action(self, in_put):
        if in_put == "take":
            self.take()

        elif in_put == "buy":
            command = input(
                "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n> "
            )

            if command.isdigit():
                self.buy(int(command))
            else:
                print()

        elif in_put == "fill":
            self.fill()

        elif in_put == "remaining":
            self.remaining()

    def take(self):
        print("I gave you $", self.money, "\n", sep="")
        self.money = 0

    def buy(self, command):

        flag = True
        missing = []
        a = self.consumption(command)
        x = [self.water, self.milk, self.beans, self.cups, self.money]
        y = ["water", "milk", "beans", "cups", "money"]

        for i in range(5):
            x[i] -= a[i]
            if x[i] < 0:
                missing.append(y[i])
                flag = False

        if flag:
            self.water, self.milk, self.beans, self.cups, self.money = x
            print("I have enough resources, making you a coffee!\n")
        else:
            print("Sorry, not enough ", ", ".join(missing), "!\n", sep="")

    def consumption(self, command):
        return {
            1: [250, 0, 16, 1, -4],
            2: [350, 75, 20, 1, -7],
            3: [200, 100, 12, 1, -6],
        }[command]

    def fill(self):

        self.water += int(input("Write how many ml of water you want to add:\n> "))
        self.milk += int(input("Write how many ml of milk you want to add:\n> "))
        self.beans += int(
            input("Write how many grams of coffee beans you want to add:\n> ")
        )
        self.cups += int(input("Write how many disposable cups you want to add:\n> "))
        print()

    def remaining(self):
        print(
            f"""The coffee machine has:
{self.water} ml of water
{self.milk} ml of milk
{self.beans} g of coffee beans
{self.cups} disposable cups
{self.money}$ of money\n"""
        )


my_machine = CoffeeMachine()

s = input("Write action (buy, fill, take, remaining, exit):\n> ")


while s != "exit":
    print()
    my_machine.action(s)
    s = input("Write action (buy, fill, take, remaining, exit):\n> ")