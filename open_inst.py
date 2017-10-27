import pickle as pk
def save(ob, p):
    with open(p, 'wb') as f:
        pk.dump(ob, f)
def opop(p):
    x = 0
    with open(p, 'rb') as f:
        x = pk.load(f)
    return x