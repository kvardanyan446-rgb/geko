class BankAccount:
   
    def __init__(self, owner: str):
        self.owner = owner
        self.balance = 0.0

   
    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"{amount}֏ հաջողությամբ մուտքագրվեց {self.owner}-ի հաշվին։")
        else:
            print("Սխալ․ Գումարը պետք է մեծ լինի 0-ից։")

  
    def withdraw(self, amount: float):
        if amount > self.balance:
            print(f"Սխալ․ {self.owner}-ի հաշվին բավարար գումար չկա (Մնացորդ՝ {self.balance}֏)։")
        elif amount <= 0:
            print("Սխալ․ Գումարը պետք է մեծ լինի 0-ից։")
        else:
            self.balance -= amount
            print(f"{amount}֏ հաջողությամբ հանվեց {self.owner}-ի հաշվից։")
            # 4. Փոխանցել գումար մեկ այլ հաշվի
    def transfer(self, target_account, amount: float):
        if amount <= 0:
            print("Սխալ․ Փոխանցվող գումարը պետք է մեծ լինի 0-ից։")
        elif amount > self.balance:
            print(f"Սխալ․ Փոխանցումը ձախողվեց։ {self.owner}-ի հաշվին բավարար գումար չկա։")
        else:
            self.balance -= amount         
            target_account.balance += amount 
            print(f"Հաջողությամբ {amount}֏ փոխանցվեց {self.owner}-ի հաշվից {target_account.owner}-ի հաշվին։")
            # 5. Ցույց տալ հաշվի տվյալները
    def show_info(self):
        print(f"Հաճախորդ՝ {self.owner} | Մնացորդ՝ {self.balance}֏")
      

anna = BankAccount(owner="Anna")
karen = BankAccount(owner="Karen")


anna.deposit(10000)


anna.transfer(karen, 4000)


anna.show_info()
karen.show_info()