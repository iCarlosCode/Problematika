from tkinter.constants import S


def obterVetorDePontos(dotA = (0, 0, 0), dotB = (0, 0, 0)):
    return (dotB[0] - dotA[0], dotB[1] - dotA[1], dotB[2] - dotA[2])

def calcularProdutoEscalar(v = (0, 0, 0), u = (0, 0, 0)):
    return ((v[0]*u[0]) + (v[1]*u[1]) + (v[2]*u[2]))

def calcularProdutoVetorial(v = (0, 0, 0), u = (0, 0, 0)):
    return (((v[1] * u[2]) - (v[2] * u[1])), ((v[2] * u[0]) - (v[0] * u[2])), ((v[0] * u[1]) - (v[1] * u[0])))
def calcularProdutoMisto(v = (0, 0, 0), u = (0, 0, 0), w = (0, 0, 0)):
    return calcularProdutoEscalar(w, calcularProdutoVetorial(v, u))
def calcularSoma(v = (0, 0, 0), u = (0, 0, 0)):
    return (v[0] + u[0], v[1] + u[1], v[2] + u[2])
def calcularSubtração(v = (0, 0, 0), u = (0, 0, 0)):
    return (v[0] - u[0], v[1] - u[1], v[2] - u[2])
def checarParalelismo(v = (0, 0, 0), u = (0, 0, 0)):
    return (calcularProdutoVetorial(v, u) == (0, 0, 0))
def checarPerpedincularismo(v = (0, 0, 0), u = (0, 0, 0)):
    return (calcularProdutoEscalar(v, u) == 0)
def calcularMultEscalar(e = 1, v = (0, 0, 0)):
    return ((v[0]*e), (v[1]*e), (v[2]*e))

def teste_do_ponto(pR = (0, 0, 0), pS = (0, 0, 0), uS = (0, 0, 0)):
    return (((pR[0] - pS[0]) * (uS[0])) == ((pR[1] - pS[1]) * (uS[1])) == ((pR[2] - pS[2]) * (uS[2])))


def calcularPosRelativaDuasRetas(pR = (0, 0, 0), vR = (0, 0, 0), pS = (0, 0, 0), uS = (0, 0, 0)):
    paralela = checarParalelismo(vR, uS)

    if paralela:
        return 'coincidentes' if teste_do_ponto(pR, pS, uS) else 'paralelas'
    else:
        wRS = obterVetorDePontos(pR, pS)
        return 'concorrentes' if calcularProdutoMisto(wRS, vR, uS) == 0 else 'reversas'

def calcular(coordenadas, resultado_lbl, coordenada4e, modo, modos):
    coordenada1 = (coordenadas[0]['x']['coordenada'].get(), coordenadas[0]['y']['coordenada'].get(), coordenadas[0]['z']['coordenada'].get())
    coordenada2 = (coordenadas[1]['x']['coordenada'].get(), coordenadas[1]['y']['coordenada'].get(), coordenadas[1]['z']['coordenada'].get())
    coordenada3 = (coordenadas[2]['x']['coordenada'].get(), coordenadas[2]['y']['coordenada'].get(), coordenadas[2]['z']['coordenada'].get())
    coordenada4 = (coordenadas[3]['x']['coordenada'].get(), coordenadas[3]['y']['coordenada'].get(), coordenadas[3]['z']['coordenada'].get())
    c_para_calc = list()
    for c in coordenadas:
        c_para_calc.append((c['x']['coordenada'].get(), c['y']['coordenada'].get(), c['z']['coordenada'].get()))

    if(modo.get() == modos[0]):
        resultado_lbl.configure(text= f'O resultado é: {obterVetorDePontos(c_para_calc[0], c_para_calc[1])}.')
    elif(modo.get() == modos[1]):
        resultado_lbl.configure(text= f'O resultado é: {calcularProdutoEscalar(c_para_calc[0], c_para_calc[1])}.')
    elif(modo.get() == modos[2]):
        resultado_lbl.configure(text= f'O resultado é: {calcularProdutoVetorial(c_para_calc[0], c_para_calc[1])}.')
    elif(modo.get() == modos[3]):
        resultado_lbl.configure(text= f'O resultado é: {calcularProdutoMisto(c_para_calc[0], c_para_calc[1], c_para_calc[3])}.')
    elif(modo.get() == modos[4]):
        resultado_lbl.configure(text= f'O resultado é: {calcularSoma(c_para_calc[0], c_para_calc[1])}.')
    elif(modo.get() == modos[5]):
        resultado_lbl.configure(text= f'O resultado é: {calcularSubtração(c_para_calc[0], c_para_calc[1])}.')
    elif(modo.get() == modos[6]):
        resultado_lbl.configure(text= '{}, pois v x u = {}.'.format('São paralelos' if checarParalelismo(c_para_calc[0], c_para_calc[1]) else 'Não são paralelos', calcularProdutoVetorial(c_para_calc[0], c_para_calc[1])))
    elif(modo.get() == modos[7]):
        resultado_lbl.configure(text= '{}, pois v • u = {}.'.format('São Perpendiculares' if checarPerpedincularismo(c_para_calc[0], c_para_calc[1]) else 'Não são perpendiculares', calcularProdutoEscalar(c_para_calc[0], c_para_calc[1])))
    elif(modo.get() == modos[8]):
        resultado_lbl.configure(text= f'O resultado é: {calcularMultEscalar(coordenada4e.get(), c_para_calc[3])}') 
    else:
        resultado_lbl.configure(text= 'Escolha um modo! :P')