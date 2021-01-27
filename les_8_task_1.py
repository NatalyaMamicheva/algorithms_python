import hashlib

str_ = input("Введите строку: ")
print(f"Количество символов в строке {len(str_)}")
set_ = set()

for i in range(len(str_)):
    for j in range(len(str_), i, -1):
        hash_str = hashlib.sha1(str_[i:j].encode("utf-8")).hexdigest()
        set_.add(hash_str)

print(f"{len(set_) - 1} подстрок в строке")