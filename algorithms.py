amount = int(input("Enter amount: "))
changes = {'1000': 0, '100': 0, '50': 0, '5': 0, '1': 0}

while amount > 0:
    if (amount >= 1000):
        changes['1000'] = amount // 1000
        amount %= 1000
    elif amount >= 100:
        changes['100'] = amount // 100
        amount %= 100
    elif amount >= 50:
        changes['50'] = amount // 50
        amount %= 50
    elif amount >= 5:
        changes['5'] = amount // 5
        amount %= 5
    else:
        changes['1'] =  amount
print(changes)