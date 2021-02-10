def list_comprehension_exercise_1():
    list_comprehension = [i for i in range(11)]
    return list_comprehension
   

def list_comprehension_exercise_2():
    list_comprehension = [i for i in range(22) if i % 2 == 0 or i % 3 == 0]
    return list_comprehension
    
def list_comprehension_exercise_3():
    list_comprehension = [i for i in range(-5, 32) if i % 5 != 0 and i % 2 != 0]
    return list_comprehension

def list_comprehension_exercise_4():

    list_comprehension = [i*i for i in range(0, 11)]
    return list_comprehension
