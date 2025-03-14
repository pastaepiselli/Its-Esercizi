def sandwich_order(ingredienti: list[str]):
    print("Preparo subito un sandwich con ...")
    for item in ingredienti:
        print(f"--{item}")

joseph: list[str] = ["panino", 'salame', "tacchino"]

sandwich_order(joseph)