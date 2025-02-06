to_do:list = [
    "Atividade 1",
    "Atividade 2",
    "Atividade 3"
]


def add_task(to_do:list, task:str) -> bool:

    try:
        to_do = to_do + [task]
    except e as e:
        return False
    else:
        print(to_do)
        return True

def delete_task(to_do:list, number:int) -> bool:

    try:

        del to_do[number - 1]
    except e as e:
        return False
    else:
        return True
    
