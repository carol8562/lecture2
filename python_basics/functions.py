def cube(x):
    return x*x*x;

def square(x):
    return x*x;

def main():
    print("Squares of the first 17 natural numbers")
    for i in range(17):
        print(f"{i+1} squared is {square(i+1)}")
    print("Cubes of the first 10 natural numbers")
    for i in range(10):
        print(f"{i+1} cubed is {cube(i+1)}")

if __name__ == "__main__":
    main()
