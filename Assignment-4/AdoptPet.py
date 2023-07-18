"""
You are given a list of pets in the shelter with their names, species, and time in the shelter
 at the start of a week.
 You receive a sequence of incoming people (to adopt pets) and animals (new additions to the shelter) one at a time.
 Print the names and species of the pets as they are adopted out.


we use two deque to indicate the list of cats and dogs
time complexity O(m * logm + n), m refer to size of the pets and n refer to size of arr
space complexity O(m + n), extra array of size m + n is needed
time spent on the question: about 30 min
"""

from collections import deque


def adoptPet(pets, arr):
    def keyFun(alist):
        return alist[-1]

    cat = []
    dog = []
    for name, species, time in pets:
        if species == 'cat':
            cat.append((name, time))
        else:
            dog.append((name, time))
    cat.sort(key=keyFun, reverse=True)
    dog.sort(key=keyFun, reverse=True)
    cat = deque(cat)
    dog = deque(dog)
    res = []
    for i in range(len(arr)):
        if len(arr[i]) == 3:  # a person to adopt a pet
            species = arr[i][-1]
            if species == 'cat' and len(cat) > 0 or (species == 'dog' and len(dog) == 0):
                pet = cat.popleft()
                res.append([pet[0], 'cat'])
            else:
                pet = dog.popleft()
                res.append([pet[0], 'dog'])
        else:  # a pet coming in the shelter
            name, species = arr[i]
            if species == 'cat':
                cat.append((name, 0))
            else:
                dog.append((name, 0))
    return res


if __name__ == "__main__":
    pets_arr = [['Sadie', 'dog', 4],
                ['Woof', 'cat', 7],
                ['Chirpy', 'dog', 2],
                ['Lola', 'dog', 1]]
    coming = [['Bob', 'person', 'dog'],
              ['Floofy', 'cat'],
              ['Ji', 'person', 'cat'],
              ['Sally', 'person', 'cat'],
              ['Ali', 'person', 'cat']]
    print(adoptPet(pets_arr, coming))
