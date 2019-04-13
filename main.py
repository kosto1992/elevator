from elevators.elevators import elevator

if __name__ == "__main__":
    left = int(input("Write position of left."))
    right = int(input("Write position of right."))
    call = int(input("Write call."))
    print(elevator(left, right, call))
