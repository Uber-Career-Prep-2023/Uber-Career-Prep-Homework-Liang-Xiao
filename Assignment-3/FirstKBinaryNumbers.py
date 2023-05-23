# Given a number, k, return an array of the first k binary numbers, represented as strings.
# time complexity O(k * log k), k refer to input number
# space complexity O(k), k refer to input number
# time spent on the question: about 10 min
def FirstKBinaryNumbers(k):
    list_bin = []
    for num in range(k):
        list_bin.append(bin(num)[2:])
    return list_bin


if __name__ == "__main__":
    print(FirstKBinaryNumbers(5))
    print(FirstKBinaryNumbers(10))
