def main():
    x = int(input("Enter a number: "))
    
    if x > 0:
        print("The number is positive.")
    elif x < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

if __name__ == "__main__":
    main()