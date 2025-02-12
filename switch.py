language=input("what is ur programing language")
match language:
    case "1":
        print("my program is java")
    case "2":
        print("my program is python")
    case "3":
        print("my program is c")
    case _: 
        print("no program")   
