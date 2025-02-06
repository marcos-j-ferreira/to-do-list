import os

to_do:list = [
    "Atividade 1",
    "Atividade 2",
    "Atividade 3"
]

def clear_terminal():
    os.system('cls')

def add_task(to_do:list, task:str) -> bool:
    try:
        to_do = to_do + [task]
    except e as e:
        return False
    else:
        return True

def delete_task(to_do:list, number:int) -> bool:
    try:
        del to_do[number - 1]
    except e as e:
        return False
    else:
        return True
    
def print_task(to_do) -> None:

    c = 0

    print("N   Atividade  \n ")
    for i in to_do:
        c += 1
        print(f"{c} | {i} \n")

def main():

    ope = "\n--- To Do List --- \n "

    c = 0

    while c < 1:

        print("Escolha uma opção:\n1 - Add\n2 - Deletar\n3 - See\n4 - sair\n Enter:")
        o = int(input()) 

        if o == 1:
            task = str(input("Escreva a task:\n"))
            add_task(to_do, task)
            print_task(to_do)
            clear_terminal()
        elif o == 2:
            n = int(input("Digi o número da atividade"))
            print_task(to_do)
            delete_task(to_do, n)
            clear_terminal()

        elif o == 3:
            clear_terminal()
            print_task(to_do)

        else:
            break

main()