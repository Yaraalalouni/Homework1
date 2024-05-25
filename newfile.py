#first question
#part A
L1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
L2 = [80, 443, 21, 53]
d = {key: value for key, value in zip(L1, L2)}
print(d)
#part B
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
number = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {number} is {factorial(number)}")
#part C
L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']
for item in L:
    if item.startswith('B'):
        print(item)
#part D
d = {i: i + 1 for i in range(11)}
print(d)


#second question
import json
import csv

def read_questions_from_text(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    questions = []
    for i in range(0, len(lines), 2):
        question = lines[i].strip()
        answer = lines[i + 1].strip()
        questions.append((question, answer))
    return questions

def read_questions_from_json(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
    return [(q['question'], q['answer']) for q in questions]

def read_questions_from_csv(file_path):
    questions = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            questions.append((row[0], row[1]))
    return questions

def ask_questions(questions):
    score = 0
    for question, correct_answer in questions:
        print(question)
        user_answer = input("Your answer: ").strip()
        if user_answer.lower() == correct_answer.lower():
            score += 1
    return score

def save_result_to_csv(user_name, score, file_path):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_name, score])

def save_result_to_json(user_name, score, file_path):
    result = {'user_name': user_name, 'score': score}
    try:
        with open(file_path, 'r') as file:
            results = json.load(file)
    except FileNotFoundError:
        results = []
    results.append(result)
    with open(file_path, 'w') as file:
        json.dump(results, file, indent=4)

def main():
    input_file = input("Enter the questions file path (text/json/csv): ").strip()
    if input_file.endswith('.txt'):
        questions = read_questions_from_text(input_file)
    elif input_file.endswith('.json'):
        questions = read_questions_from_json(input_file)
    elif input_file.endswith('.csv'):
        questions = read_questions_from_csv(input_file)
    else:
        print("Error: Unsupported file format.")
        return
    
    user_name = input("Enter your name: ").strip()
    score = ask_questions(questions)
    
    print(f"Your score: {score}/{len(questions)}")
    
    output_file = input("Enter the results file path (csv/json): ").strip()
    if output_file.endswith('.csv'):
        save_result_to_csv(user_name, score, output_file)
    elif output_file.endswith('.json'):
        save_result_to_json(user_name, score, output_file)
    else:
        print("Error: Unsupported file format.")

if __name__ == "__main__":
    main()
    
 #third question
 class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"BankAccount(account_number={self.account_number}, account_holder={self.account_holder}, balance=${self.balance:.2f})"

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest of ${interest:.2f}. New balance is ${self.balance:.2f}.")

    def __str__(self):
        return f"SavingsAccount(account_number={self.account_number}, account_holder={self.account_holder}, balance=${self.balance:.2f}, interest_rate={self.interest_rate:.2%})"

# Creating an instance of BankAccount
account = BankAccount("123456789", "John Doe")
print(account)
account.deposit(1000)
print(account)
account.withdraw(500)
print(account)

# Creating an instance of SavingsAccount
savings_account = SavingsAccount("987654321", "Jane Doe", 0.05)
print(savings_account)
savings_account.deposit(2000)
savings_account.apply_interest()
print(savings_account)

#4th question

def is_valid_binary(binary_str):
    """Check if the input string is a valid binary number."""
    for char in binary_str:
        if char not in '01':
            return False
    return True

def binary_to_decimal(binary_str):
    """Convert a binary string to its decimal equivalent."""
    decimal_number = 0
    power = 0
    for digit in reversed(binary_str):
        decimal_number += int(digit) * (2 ** power)
        power += 1
    return decimal_number

def main():
    """Main function to handle input and output."""
    binary_str = input("Enter a binary number: ")
    
    # Validate the input
    if not is_valid_binary(binary_str):
        print("Error: Invalid binary number. Please enter a number containing only 0s and 1s.")
        return
    
    # Convert to decimal and display the result
    decimal_number = binary_to_decimal(binary_str)
    print(f"The decimal equivalent of binary {binary_str} is {decimal_number}.")

# Run the main function
if __name__ == "__main__":
    main()def is_valid_binary(binary_str):
    """Check if the input string is a valid binary number."""
    for char in binary_str:
        if char not in '01':
            return False
    return True

def binary_to_decimal(binary_str):
    """Convert a binary string to its decimal equivalent."""
    decimal_number = 0
    power = 0
    for digit in reversed(binary_str):
        decimal_number += int(digit) * (2 ** power)
        power += 1
    return decimal_number

def main():
    """Main function to handle input and output."""
    binary_str = input("Enter a binary number: ")
    
    # Validate the input
    if not is_valid_binary(binary_str):
        print("Error: Invalid binary number. Please enter a number containing only 0s and 1s.")
        return
    
    # Convert to decimal and display the result
    decimal_number = binary_to_decimal(binary_str)
    print(f"The decimal equivalent of binary {binary_str} is {decimal_number}.")

# Run the main function
if __name__ == "__main__":
    main()