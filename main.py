from calculator import add, subtract, multiply, divide
import utils


def main():
    print("Calculator Test")
    print(f"{add(5, 3)=}")
    print(f"{subtract(10, 4)=}")
    print(f"{multiply(5, 3)=}")
    print(f"{divide(8, 4)=}")
    print(f"{utils.is_even(7)=}")
    print(f"{utils.factorial(5)=}")


if __name__ == "__main__":
    main()
