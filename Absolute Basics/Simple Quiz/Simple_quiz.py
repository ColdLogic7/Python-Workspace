
questions = [
    {"question": "What is 2+2?", "options": ["2","3","4","5"], "answer": "4"},
    {"question": "Capital of France?", "options": ["Berlin","Paris","Rome","Madrid"], "answer": "Paris"},
    {"question": "Which is the longest river in the world?", "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"], "answer": "Nile River"},
    {"question": "What is the largest ocean on Earth?", "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"], "answer": "Pacific Ocean"},
    {"question": "Which planet in our solar system is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "Which country gifted the Statue of Liberty to the United States?", "options": ["United Kingdom", "France", "Canada", "Spain"], "answer": "France"},
    {"question": "What is the hardest natural substance on Earth?", "options": ["Gold", "Iron", "Quartz", "Diamond"], "answer": "Diamond"},
    {"question": "Which is the largest planet in our solar system?", "options": ["Earth" ,"Mars","Jupiter" ,"Saturn"], "answer": "Jupiter"},
    {"question": "What is the name of the galaxy that contains our Solar System?", "options": ["Andromeda", "Milky Way", "Sombrero", "Whirlpool"], "answer": "Milky Way"},
    {"question": "Which metal is a liquid at room temperature?", "options": ["Gold", "Iron", "Silver","Mercury"], "answer": "Mercury"},
    {"question": "What is the chemical symbol for water?", "options": ["O2", "H2O", "CO2", "NaCl"], "answer": "H2O"},
    {"question": "Who was the founder of the Maurya Empire in India?", "options": ["Bindusara", "Ashoka", "Chandragupta Maurya", "Samudragupta"], "answer": "Chandragupta Maurya"},
    {"question": "Which monument was built by the Mughal Emperor Akbar to celebrate his victory in Gujarat?", "options": ["Red Fort", "Humayun's Tomb", "Buland Darwaza", "Qutub Minar"], "answer": "Buland Darwaza"},
    {"question": "Which fruit is known as the 'king of fruits'?", "options": ["Apple", "Mango", "Banana", "Orange"], "answer": "Mango"},
    {"question": "How many bones are in the adult human body?", "options": ["200", "206", "212", "218"], "answer": "206"}
]


import random

def printing_random_questions(questions_list):
    random_index = random.randrange(len(questions_list))
    select_question = questions_list[random_index]['question']
    return random_index, select_question

# About the flow:
def display_option(questions_list,index):
    options = questions_list[index]['options']
    print("\n ⚡ Options:")
    for i, option in enumerate(options,1):
        print(f"{i}. {option}")

def check_answer(q_index, question_pool,answer_index):
    answer = question_pool[q_index]['answer']
    user_answer = question_pool[q_index]['options'][answer_index]
    if user_answer == answer:
        return True, answer
    else:
        return False, answer
    
def taking_user_input(question_pool,q_index):
    while True:
        try:
            options_len = len(question_pool[q_index]['options'])
            answer_index = int(input("\n 🎯 Enter Your Answer No. Here [1,2,3,4]: ").strip())
            if 1<= answer_index <= options_len:
                return answer_index - 1
            else: 
                print("\n ❌ Please Choose Number Below 5 and Greater 1")
        except ValueError:
            print("\n ❌ Please Enter Option Number Here, Nothing Else! ")
    
def main():
    print("\n-------- 🧠 Welcome To Simple Quiz Game ---------")
    asked_q_index = []
    attempt = 5
    while True:
        print(f"[ 💖 Attempt Left: {attempt} ]")
        
        while True:
            q_index, question = printing_random_questions(questions)

            if q_index not in asked_q_index:
                break

        asked_q_index.append(q_index)
        print(f"\n � Question: {question}")
        display_option(questions,q_index)
        user_answer_index = taking_user_input(questions,q_index)
        answer_check, answer = check_answer(q_index,questions,user_answer_index)

        if answer_check:
            print("\n ✨ Correct Answer ")
        else:
            print(f"\n ⚠️ Wrong Answer, Correct Answer is '{answer}' ")
        attempt -= 1
        
        if attempt == 0:
            print("\n 💔 No Attempts Left!, 👍 Well Played")
            break

        print("\n----------------------------------------\n ")


if __name__ == '__main__':
    try:
        while True:
            main()
            play_again = input("\n 🤔 Do You Want to Play Again [y/n]: ").strip().lower()
            if play_again != 'y':
                print("\n 👋 Goodbye!")
    except KeyboardInterrupt:
        print("\n 👋 Goodbye!")

