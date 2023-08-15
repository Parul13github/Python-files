word=input("Enter the word:")

def find_lenth(word):
    count=0
    for i in word:
        count+=1
    return count
print(find_lenth(word))
