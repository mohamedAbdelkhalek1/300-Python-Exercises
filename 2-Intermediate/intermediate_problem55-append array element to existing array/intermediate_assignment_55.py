"""
intermediate_assignment_55:

Write a Python Program to Generate a random month between start and end date.

"""
import random
from datetime import datetime

def generate_random_month(start_date, end_date):
    start_month = start_date.month
    start_year = start_date.year
    end_month = end_date.month
    end_year = end_date.year

    if start_year == end_year:
        random_month = random.randint(start_month, end_month)
    else:
        random_year = random.randint(start_year, end_year)
        
        if random_year == start_year:
            random_month = random.randint(start_month, 12)
        elif random_year == end_year:
            random_month = random.randint(1, end_month)
        else:
            random_month = random.randint(1, 12)
    
    return datetime(random_year, random_month, 1)

# Example usage
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

random_month = generate_random_month(start_date, end_date)
print(random_month.strftime("%B %Y"))