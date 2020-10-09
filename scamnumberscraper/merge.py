import json

if __name__ == "__main__":
    file = open("merged.txt", "r")
    lines = file.readlines()
    numbers = set()

    for line in lines:
        numbers.add(line.replace("\n", ""))

    with open(f"merged.json", "w") as outfile:
        json.dump(list(numbers), outfile)
