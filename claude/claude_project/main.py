import utils

def main():
    data = [1,2,3,4]
    # Intentional inefficiency
    result = []
    for x in data:
        result.append(utils.square_number(x))
    print("Squares:", result)

if __name__ == "__main__":
    main()
