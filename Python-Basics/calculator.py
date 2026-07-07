def main():
    x = float(input("Whats x? "))
    y = float(input("Whats y? "))
    q = (input("Multiplication, Subtraction, Division, or Addition Today? ")).title().strip()
    print("your answer is ", answer(q, x, y))

def answer(q, x, y):
    if q == "Multiply" or q == "Multiplication":
        return x * y
    elif q == "Subtract" or q == "Subtraction":
        return x - y 
    elif q == "Division" or q == "Divide":
        return x / y
    elif q == "Addition" or q == "Add":
        return x + y 
    else:
        print("Did not enter valid mathematical equations please try again")

main()