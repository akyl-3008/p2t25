word = input("Введите прделожение: ")
word_ = word.split()
test = word_[0]
for i in word_[1:]:
    if len(i) > len(test):
        test = i
print(test)