def calcularProdutoVetorial(v = (0, 0, 0), u = (0, 0, 0)):
    return (((v[1] * u[2]) - (v[2] * u[1])), ((v[2] * u[0]) - (v[0] * u[2])), ((v[0] * u[1]) - (v[1] * u[0])))
    