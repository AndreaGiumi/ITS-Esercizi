voto: int = int(input("Inserisci voto di laurea: "))

match voto:
    # case 1
    case 106|107|108|109|110:
        print("GPA 4.0")
    # case 2
    case 101|102|103|104|105:
        print("GPA 3.7")
    # case 3
    case 96|97|98|99|100:
        print("GPA 3.3")
    # case 3
    case 91|92|93|94|95:
        print("GPA 3.0")
    # case 4
    case 86|87|88|89|90:
        print("GPA 2.7")
    # case 5
    case 81|82|83|84|85:
        print("GPA 3.0")
    # case 6
    case 91|92|93|94|95:
        print("GPA 3.0")
        