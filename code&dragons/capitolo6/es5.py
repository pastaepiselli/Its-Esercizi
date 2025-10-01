def min_coins(amount, coins):
    # Inizializza un array dp con un valore grande (1_000_000_000) per indicare impossibile
    dp = [1_000_000_000] * (amount + 1)
    dp[0] = 0  # Importo 0 richiede 0 monete
    
    # Per ogni importo da 1 ad amount
    for i in range(1, amount + 1):
        # Prova ogni moneta
        for coin in coins:
            if coin <= i:
                # Usa il minimo tra il valore corrente e il numero di monete per (i - coin) + 1
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] 