import json

if __name__ == "__main__":
    numbers = set()
    numbers.add("+33353490088")
    numbers.add("+33353490082")
    numbers.add("+33353490081")

    """
    file = open("merged.txt", "r")
    lines = file.readlines()
    numbers = set()

    for line in lines:
        numbers.add(line.replace("\n", ""))


    with open(f"merged.json", "w") as outfile:
        json.dump(list(numbers), outfile)

    """
    new_file = open("merged.txt")
    newl = new_file.readlines()

    old_file = open("old.json")
    oldl = json.load(old_file)

    print(len(newl))
    print(len(oldl))

    count_same = 0

    for new in newl:
        numbers.add(new.replace("\n", ""))

    for old in oldl:
        numbers.add(old.replace("\n", ""))

    with open(f"merged.json", "w") as outfile:
        json.dump(list(numbers), outfile)
