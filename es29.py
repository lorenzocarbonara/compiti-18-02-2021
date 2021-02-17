reddito = float(input("Inserire il reddito."))
limite = [15000,28000,55000,75000,1000000000]
aliquota = [23,27,38,41,43]

if reddito <= 1000000000 and reddito > 75000:

    imposta = 15000*23/100 + 13000*27/100 + 27000*38/100 + 20000*41/100 + (reddito - 75000)*43/100
    reddito_tassato = reddito - imposta
    print("Il reddito tassato è ",reddito_tassato," euro.")
elif reddito <= 75000 and reddito > 55000:
    imposta = 15000*23/100 + 13000*27/100 + 27000*38/100 + (reddito - 55000)*41/100
    reddito_tassato = reddito - imposta
    print("Il reddito tassato è ",reddito_tassato," euro.")
elif reddito <= 55000 and reddito > 28000:
    imposta =  15000*23/100 + 13000*27/100 + (reddito - 28000)*38/100
    reddito_tassato = reddito - imposta
    print("Il reddito tassato è ",reddito_tassato," euro.")    
elif reddito <= 28000 and reddito > 15000:
    imposta = 15000*23/100 + (reddito - 15000)*27/100
    reddito_tassato = reddito - imposta
    print("Il reddito tassato è ",reddito_tassato," euro.")    
elif reddito <= 15000:
    imposta = reddito*23/100
    reddito_tassato = reddito - imposta
    print("Il reddito tassato è ",reddito_tassato," euro.")
else:
    print("Hai scritto male il reddito.")