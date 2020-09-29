# QApython Vitalii Feshchenko
# Homework #4 Task 1

def la_la_la(string=3, n=3, end=0):
    """ 1-е число – сколько строк будет в песне. По умолчанию 3
        2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
        3-е число – если 0, то в конце песни (в конце последней строчки) стоит точка, если 1, то в конце
        стоит «!». По умолчанию 0 """


    song = 'la' * n

    # adding appropriate number of strings including all returns(enter) except last
    song = (song + '\n')*(string-1) + song

    if not end:
        song += '.'
    elif end == 1:
        song += '!'

    return song



print(la_la_la(end=1))

