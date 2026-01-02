# test_array = [0, 0, 0]
#
# users = {
#     1: "slavi",
#     2: "nasko",
#     3: "stoqn"
# }
#
# user_hashes = []
#
# for user in users.values():
#     user_hash = str(hash(user))
#
#     print(f"Hash for {user} is {user_hash}")
#     user_hashes.append(user_hash)
#
# print("user_hashes", user_hashes)


# import hashlib
#
# class BloomFilter:
#     def __init__(self, size=1000, hash_count=3):
#         self.size = size
#         self.hash_count = hash_count
#         self.bit_array = [0] * size
#
#     def _hashes(self, item):
#         digest = hashlib.md5(item.encode()).hexdigest()
#
#         for i in range(self.hash_count):
#             chunk = digest[i*8:(i+1)*8]
#             yield int(chunk, 16) % self.size
#
#     def add(self, item):
#         for index in self._hashes(item):
#             self.bit_array[index] = 1
#
#     def contains(self, item):
#         for index in self._hashes(item):
#             if self.bit_array[index] == 0:
#                 return False
#         return True
#
# users = ["slavi", "nasko", "stoqn"]
#
# bf = BloomFilter(size=100, hash_count=3)
#
# for user in users:
#     bf.add(user)
#
# print("bf", bf)
#
# print(bf.contains("slavi"))   # True
# print(bf.contains("nasko"))   # True
# print(bf.contains("pesho"))   # False (or sometimes True → false positive)

# The Simplest Membership Filter
# X - slow, memory-heavy
class WordSet:
    def __init__(self):
        self.words = []

    def add(self, word):
        self.words.append(word)

    def contains(self, word):
        return word in self.words


class MarkerArray:
    def __init__(self, size):
        self.size = size
        self.slots = [0] * size # Represented like [0, 0, 0, 0, 0, 0]


class MultiHasher:
    def __init__(self, size, count):
        self.size = size
        self.count = count

    def hashes(self, word):
        for i in range(self.count):
            total = 0
            for char in word:
                total += ord(char) * (i + 1)
            yield total % self.size


class BloomFilter:
    def __init__(self, size=20, hash_count=3):
        self.array = MarkerArray(size)
        self.hasher = MultiHasher(size, hash_count)

    def add(self, word):
        for index in self.hasher.hashes(word):
            self.array.slots[index] = 1

    def contains(self, word):
        for index in self.hasher.hashes(word):
            if self.array.slots[index] == 0:
                return False
        return True


bf = BloomFilter(10)

bf.add("cat")
bf.add("dog")

print(bf.contains("cat"))   # True
print(bf.contains("dog"))   # True
print(bf.contains("god"))   # ❗ Maybe True

# TODO: Truly understand what is going on and exercise bit operations
