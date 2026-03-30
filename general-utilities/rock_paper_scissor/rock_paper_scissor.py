import random

def check_rerun():
    while True:
        exit_or_rerun = input("\n If you want to exit this program type 'exit' or rerun type 'rerun' [default = rerun]: ").lower().strip()
        if exit_or_rerun == "exit":
            print("\n Exiting this program..........")
            print("\n Thankyou  for running my program \n ")
            return False
        elif exit_or_rerun == "rerun":
            return True
        else:
            print("Invalid input. Please type 'exit' or 'rerun' ")

def user_greeting():
    print("\n Hey 👋 , Let's play Rock - Paper - Scissor ;  Defeat me if you can 👻")

def main():
    a = ["rock" , "paper" , "scissor"]
    user_greeting()
    while True:
        i_choose = random.choice(a)
        try:
            user_choose = input("\n Choose among [rock , paper , scissor] , I will choose too : ").lower().strip()
            print(f"\n \t you choose  : {user_choose} ")
            print(f"\n \t I choose  : {i_choose} ")
        except Exception:
            if user_choose not in a:
                print("🥲 \n Please choose among rock , paper , scissor")
                continue

        if i_choose == "rock" and user_choose == "scissor":
            print("\n My rock 🪨 will destroy your scissor ✂️ ")
            print("\n Hurray , 😁 I win this game .......")

        elif i_choose == "paper" and user_choose == "rock":
            print("\n My paper 📜 will cover up your rock 🪨")
            print("\n Hurray , 😁 I win this game .......")

        elif i_choose == "scissor" and user_choose == "paper":
            print("\n My scissor ✂️ will cut your paper 📜")
            print("\n Hurray , 😁 I win this game .......")

        elif user_choose == "rock" and i_choose == "scissor":
            print("\n Your rock 🪨 will destroy my scissor ✂️ ")
            print("\n Hmm my bad , 🥲 I lose this game .......")

        elif user_choose == "paper" and i_choose == "rock":
            print("\n Your paper 📜 will cover up my rock 🪨")
            print("\n Hmm my bad , 🥲 I lose this game .......")

        elif user_choose == "scissor" and i_choose == "paper":
            print("\n Your scissor ✂️ will cut my paper 📜")
            print("\n Hmm my bad , 🥲 I lose this game .......")

        elif user_choose == "rock" and i_choose == "rock":
            print("\n Well , Match is Draw 🟰 try to rerun this program")

        elif user_choose == "paper" and i_choose == "paper":
            print("\n Well , Match is Draw 🟰 try to rerun this program")

        elif user_choose == "scissor" and i_choose == "scissor":
            print("\n Well , Match is Draw 🟰 try to rerun this program")
    
        if not check_rerun():
            break

if __name__ == "__main__":
    main()
            
