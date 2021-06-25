def AckermanFunction(Number1, Number2):
    if Number1 == 0:
        return Number2 + 1
    else:
        if Number2 == 0:
            return (AckermanFunction(Number1 - 1, 1))
        return (AckermanFunction(Number1 - 1, AckermanFunction(Number1, Number2 - 1)))

print(AckermanFunction(2,3))