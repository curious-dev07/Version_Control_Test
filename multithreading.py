# import multithreading
"""
import threading
import time

# Indicates some task being done.


def func(seconds):
    print(f"Sleeping for {seconds} seconds.")
    
    time.sleep(seconds)
    
func(4)
func(2)
func(1)

# hum bana chahate hai ye sab simultaneously run ho.

t1 = threading.Thread(target=func, args = [4])
"""
"""
total = 0
def sum_list(lst):
    for ele in lst:
        if isinstance(ele, list):
            sum_list(ele)
        else:
            global total
            total += ele
    return total

li = [10, 20, [30, 40], 50,[60, 70, 80, 90, [100, 110, 120, 130, 140], 150], 160]
print(sum_list(li))
"""
"""
def remove_empty_list(lst):
    if not isinstance(lst, list):
        return lst
        
    lst = [remove_empty_list(ele) for ele in lst if ele != [] ]
    
    return lst

li = [100, 'ajay', [], ['amit', [], [], 'athrva'], [[], 'omkar', 123, 11], [44, 'sakeeb'], []]
print(remove_empty_list(li))
"""
"""
total = 0
def sum_all(lst):
    for ele in lst:
        if isinstance(ele, list):
            sum_all(ele)
            
        else:
            global total
            total += ele
    return total

print(sum_all([10, 20, [30, 40], 50,[60, 70, 80, 90, [100, 110, 120, 130, 140], 150], 160]))
"""
"""
str = "G  Gle"

def replace_space(str):
    new_str = ""
    for char in str:
        if char == " ":
            new_str = new_str + "o"
            
        else:
            new_str = new_str + char
            
    return new_str.upper()

print(replace_space(str))
"""
"""
str = "Sugar is bad for health"

def reverse_sentence(str):
    str = str.upper()
    return " ".join(str.split(" ")[::-1])

print(reverse_sentence(str))
"""