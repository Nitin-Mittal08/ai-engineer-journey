#Exercise 1 - Ask username and print it

def printName():
    print("What's your name?");
    name=input();
    
    print(f'Hello {name}!');


printName();


#Exercise 2 - Ask age and print it

def printAge():
    age = input("What's your age?");
    print(f"You are {age} years old");


printAge();


#Exercise 3 - Ask 2 numbers and do algebra

def twoNumbers():
    num1 = input("Please enter 1st number:");
    num2 = input("Please enter 2nd number:");

    sum = int(num1) + int(num2);
    difference = int(num1)-int(num2);
    multiplication = int(num1)*int(num2);
    division = int(num1)/int(num2);

    print(f"Sum of the two numbers is {sum}");
    print(f"Difference of the two numbers is {difference}");
    print(f"Multiplication of the two numbers is {multiplication}");
    print(f"Division of the two numbers is {division}")


twoNumbers();


#Exercise 4 - Ask fav movie

def askFavMovie():
    favMovie = input("What's your fav movie?");
    print(f"{favMovie} is a great choice!");

askFavMovie();


#Exercise 5 - Ask YOB and tell age
from datetime import date
current_date = date.today();
current_year = current_date.year;
def tellAge():
    yearOfBirth = input("What year were you born?");
    age = current_year - int(yearOfBirth);
    print(f"You are {age} years old");


tellAge();
    







