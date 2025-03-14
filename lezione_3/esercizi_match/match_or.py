http_status = 200
match http_status:
    case 200|201: # | si riferisce ad or 
        print("Success")
    case 404:
        print("Not found")
    case 500|501:
        print("Server Error")
    # caso default
    case _:
        print("Pier damien")