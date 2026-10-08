def calcul_rendement(montant, taux, duree):
    interet = montant * (taux / 100) * duree
    total = montant + interet
    return {
        'montant_initial': montant,
        'interet': round(interet, 2),
        'total': round(total, 2)
    }
