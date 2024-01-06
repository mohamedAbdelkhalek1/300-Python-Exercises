"""
complex_assignment_15:

Write A Python Program To Find Keyword Density In A Article. And Display A Message If Density Increase Up To 3%

"""

para = input("Enter a paragraph...")
keywrod = input("Enter a word or keywrod to find density")

word_count = 1
for i in para:
    if i == " ":
        word_count += 1
        
print("Total Words = "+str(word_count))

keywrod_count = para.count(keywrod)
print("User Word occurences ="+str(keywrod))

keyword_density = (keywrod_count / word_count) * 100

print("Keyword Density = "+str(keyword_density)+"%")

if keyword_density > 3:
    print("the specific keyword Density Increase Up To 3\% and massegr : ")
    print(para)