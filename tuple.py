fee=(10,20,30)
print(fee)
fee=list(fee)
print(type(fee))

fee[1]=25

fee=tuple(fee)
print(type(fee))
print(fee)