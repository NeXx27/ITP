
# with out using min() function
def min_form_list(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min
    


    
# now max without useing max() function

def max_form_list(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max


list1 = [1, 2, 3, 4, 5]

