monthly_income = eval(input("enter your monthly income"))
monthly_exp = eval(input("Enter your monthly expenses"))
monthly_saving =monthly_income - monthly_exp

project_saving = monthly_saving *12 + (monthly_saving * 12 * 0.05)


print(monthly_saving)
print(project_saving)