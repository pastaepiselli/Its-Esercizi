def car_specifics(manifacturer: str, modelname: str, **optional):
    mycar: dict = {"Manifacturer": manifacturer, modelname: modelname, **optional}
    return mycar
