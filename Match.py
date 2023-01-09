

def http_error(status):
    match status:
        case 400:
            return "Solicitud no encontrada"
        case 404:
            return "No encontrado"
        case 418:
            return "Soy una tetera"
        case _:
            return "Se cayo internet"


print(http_error)
