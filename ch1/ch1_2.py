"""
An employee’s total weekly pay equals the hourly wage multiplied by the total
number of regular hours plus any overtime pay. Overtime pay equals the total
overtime hours multiplied by 1.5 times the hourly wage. Write a program that
takes as inputs the hourly wage, total regular hours, and total overtime hours and
displays an employee’s total weekly pay.
"""

def main():

    hourlyWage = float(input("Enter your hourly wage: "))
    regularHours = float(input("Enter the regular hours you worked: "))
    overtime = float(input("Enter the number of overtime hours you worked: "))

    weeklyPay = (hourlyWage * regularHours) + (overtime * 1.5 * hourlyWage)

    print("Weekly Pay:", weeklyPay)

if __name__ == "__main__":
    main() 