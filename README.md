# ArtificialBeeColony
## CODE EXAMPLE:
```python
def test(X,D):
    x1 = X[0]
    x2 = X[1]
    return x1**2 - x1*x2 + x2**2 + 2*x1 + 4*x2 + 3

def RastriginFunc(X, D):
    funsum = 0
    for i in range(D):
        x = X[i]
        funsum += x**2-10*np.cos(2*np.pi*x)
    funsum += 10*D
    return funsum

def StyblinskiTangFunc(X, D):
    funsum = 0
    for i in range(D):
        x = X[i]
        funsum += (x**4) - 16*(x**2) + 5*x
    funsum *= 0.5
    return funsum

# ArtificialBeeColony(D, Lb, Ub, n, generation, ans[min=0/max=1], func)
abc = ArtificialBeeColony(2, -5, 5, 5, 100, 0, test)
abc.doRun()
```
