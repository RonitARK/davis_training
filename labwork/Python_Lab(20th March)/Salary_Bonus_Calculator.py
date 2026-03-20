# Input: salary and years of experience
def calculate_bonus(salary, years):
    # Use if-elif-else
    if years >= 10:
        return salary * 0.20 # 10 years -> 20% bonus
    elif years >= 5:
        return salary * 0.10 # 5-10 years -> 10%
    elif years >= 0:
        return salary * 0.05 # <5 -> 5%
    else:
        return 0

def run_bonus_system():
    # Loop for multiple employees
    while True:
        salary_input = input("Enter employee salary (or 'quit' to exit): ")
        if salary_input.lower() == 'quit':
            break
                
        salary = float(salary_input)
        years = float(input("Enter years of experience: "))
            
        bonus = calculate_bonus(salary, years)
        print(f"Bonus calculated: ${bonus:.2f}\n")

run_bonus_system()