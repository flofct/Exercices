def convertir(nombre):
    if (nombre < 4):
        return 'I'*nombre

    if (nombre == 4):
        return 'IV'

    if (nombre <= 8):
        return 'V' + 'I'*(nombre - 5)

    if (nombre == 9):
        return 'IX'

    if (nombre <= 10):
        return 'X' + 'I' * (nombre-10)


    raise Exception('Nombre non supporté')


