## check for prime Number or not.
"""
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
        
    return True
number = int(input("Enter Number : "))

if is_prime(number):
    print(f"{number} ===> PRIME")
else: 
    print(f"{number} ===> NOT  PRIME") 
"""
"""
string = "aaalljdieureuieiuallaasne"
dic = {}
def counting_occurences(str):
    for alp in str:
        if alp in dic:
            dic[alp] = dic[alp] + 1
        else:
            dic[alp] = 1
    return dic

print(counting_occurences(string))
"""
"""
a = 269
b = 305
while b  != 0:
    temp = a & b
    a = a ^ b
    b = temp << 1
print(a)
"""
"""
li = [-10, 12, 31, 1, -7, 6, -15, -17]

def sort_and_square(lst):
    lst = [ele**2 for ele in lst]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                
    return lst
print(sort_and_square(li))
"""
"""
import json

data = {
  "name": "Jane Doe",
  "age": 25,
  "skills": ["programming", "writing", "design"],
  "contact" : "+91 1020304050",
  "city" : "Pune Maharashtra"
}

with open("data.json", "w") as f:
  json.dump(data, f)
"""
"""
dic ={"name": "Jane Doe",
       "age": 25,
       "skills": ["programming", "writing", "design"],
       "contact": "+91 1020304050",
       "city": "Pune Maharashtra"
    }

print(dic.get("contact")[4:])
"""
"""
li = [10, 20, 30, 40, [50, 60, 70, 80,[90], 100], 1000]
sum = 0
def nested_list_sum(lst):
    for ele in lst:
        if isinstance(ele, list):
            nested_list_sum(ele)
        else:
            global sum 
            sum += ele
    return sum

print(nested_list_sum(li))
"""
"""
li = [100, 300, [250, 1000, [2000, 3000, [4000], [1000]], [900], [800]], [1200]]
sum = 0
def summing_nested_list(lst):
    
    for ele in lst:
        if isinstance(ele, list):
            summing_nested_list(ele)
            
        else:
            global sum
            sum += ele
    return sum
print(summing_nested_list(li))
"""
"""
li = ["abhay", "krishna", ["poonam", "kavya", [], ], ["ashvini", "saumya", "kartik", [], [[], "amit"]]]
la = []
def removing_empty_list_and_adding_all_elements_in_one_list(lst):
    for ele in lst:
        if isinstance(ele, list) and len(ele) == 0:
            lst.pop(ele)
            removing_empty_list_and_adding_all_elements_in_one_list(ele)
            
        else:
            removing_empty_list_and_adding_all_elements_in_one_list(lst[ele])
    return lst
print(removing_empty_list_and_adding_all_elements_in_one_list(li))   
"""
"""
def remove_empty_lists(lst):
    if not isinstance(lst, list):
        return lst
    
    # Remove empty lists using list comprehension
    cleaned_list = [remove_empty_lists(item) for item in lst if item != []]
    
    return cleaned_list

li = ["abhay", "krishna", ["poonam", "kavya", [], ], ["ashvini", "saumya", "kartik", [], [[], "amit"]]]

cleaned_li = remove_empty_lists(li)
print(cleaned_li)
"""
"""
def remove_null_list(lst):
    if not isinstance(lst, list):
        return lst
    
    lst = [remove_null_list(ele) for ele in lst if ele != []]
    
    return lst
print(remove_null_list(["abhay", "krishna", ["poonam", "kavya", [], ], ["ashvini", "saumya", "kartik", [], [[], "amit"]]]))
"""

# string = "qpowertyuiolaksjhdfgzbvx"
# # print(string[::-1])
# print(string[-2:1:-2])
"""
def string_reverse(str):
    li = []
    for i in range(len(str)-1, -1, -1):
        print(str[i])
        li.append(str[i])
    return "".join(li)
print(string_reverse("Ramesh"))
"""
"""
name = "RAHUL"
def string_reverse(str):
    li = []
    for i in range(len(str)-1, -1, -1):
        li.append(str[i])
    return "".join(li)
print(string_reverse(name))
"""
"""
sentence = "I am very Happy that I got this oppurtunity to work on this project"

def reverse_word_inSentence(str):
    return " ".join((str.split(" "))[::-1])
print(reverse_word_inSentence(sentence))
"""
"""
def find_pair_indexs(lst, target):
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] + lst[j] == target:
                return (i, j)
    return "Pair does not Exist."

li = [100, 200, 1000, 1200, 500, 200]
print(find_pair_indexs(li, 1400))
"""
"""
my_string = "Hello World"
vowels = "aeiouAEIOU"
vowel_list = []

for char in my_string:
    if char in vowels:
        vowel_list.append(char)
        
print(vowel_list)
"""
"""
my_list = [1, 2, 3, 4, 5]
index1 = 1
index2 = 3

my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

print(my_list)

"""
"""
num = int(input('no='))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + (digit**3)
    temp = temp // 10

if num == sum:
    print('yes')

else:
    print('no')
"""
#check for amstrong Number.

"""
num = int(input("No : "))   
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum = sum + (digit **3)
    temp = temp // 10
    
if num == sum:
    print("yes")

else:
    print("NO")
        
"""
