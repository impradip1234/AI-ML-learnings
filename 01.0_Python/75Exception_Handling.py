# exception handling 
# try, except, else, finally
try:
    x=int(input("Enter the value of x: "))
    ans=10/x
except ZeroDivisionError:
    print("Division by zero is not possible")

except ValueError:
    print("invalid input.")

else:
    print(f"ans={ans}")
finally:
    print("End of the program")
