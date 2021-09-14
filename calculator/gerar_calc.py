from calculator.operations import calcularProdutoEscalar, calcularProdutoVetorial, obterVetorDePontos, teste_do_ponto
from fractions import Fraction


c = "\[\sqrt{{{c}}}\]"
HTML_BASE = """<!DOCTYPE html>
<html lang="pt-BR">

<head>
  <meta charset="UTF">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <script type="text/x-mathjax-config">
    MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\\(','\\\)']]}});
  </script>
  <script type="text/javascript" async src="mathjax2/MathJax.js?config=TeX-AMS_CHTML" onerror=onError()></script>
  <script>
    function onError() {
      var script = document.createElement('script');
      script.src = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML";
      script.async = true;
      document.head.appendChild(script);
    }
  </script>
</head>

<body>"""


def gerar_calculo_soma(v=(0, 0, 0), u=(0, 0, 0)):
    text = (
        HTML_BASE
        + f"""Para subtrair dois vetores \(\\vec v=(a, b, c)\) e \(\\vec u=(d, e, f)\), podemos usar a fórmula: \(\\vec v + \\vec u = (a + d, b + e, c + f)\).
<br>Sendo \(\\vec v=({v[0]}, {v[1]}, {v[2]})\) e \(\\vec u=({u[0]}, {u[1]}, {u[2]})\).
Temos:
    \(\\vec v + \\vec u = ({v[0]} + {u[0]}, {v[1]} + {u[1]}, {v[2]} + {u[2]})\).<br>
    \(\\vec v + \\vec u = ({v[0]+u[0]}, {v[1]+u[1]}, {v[2]+u[2]})\).
</body>
</html>"""
    )

    with open("calculo1.html", "w") as file:
        file.write(text)


def gerar_calculo_subtração(v=(0, 0, 0), u=(0, 0, 0)):
    text = (
        HTML_BASE
        + f"""Para subtrair dois vetores \(\\vec v=(a, b, c)\) e \(\\vec u=(d, e, f)\), podemos usar a fórmula: \(\\vec v - \\vec u = (a - d, b - e, c - f)\).
<br>Sendo \(\\vec v=({v[0]}, {v[1]}, {v[2]})\) e \(\\vec u=({u[0]}, {u[1]}, {u[2]})\).
Temos:
    \(\\vec v - \\vec u = ({v[0]} - ({u[0]}), {v[1]} - ({u[1]}), {v[2]} - ({u[2]}))\).<br>
    \(\\vec v - \\vec u = ({v[0]-u[0]}, {v[1]-u[1]}, {v[2]-u[2]})\).
</body>
</html>"""
    )

    with open("calculo1.html", "w") as file:
        file.write(text)


def gerar_calculo_formar_vetores(v=(0, 0, 0), u=(0, 0, 0)):
    text = (
        HTML_BASE
        + f"""Para formar um vetor \(\\overrightarrow{{AB}}=(a, b, c)\) com os pontos \(\\color{{teal}}{{A(x_a, y_a, z_a)}}\) e \(\\color{{#A80}}{{B(x_b, y_b, z_b)}}\), podemos usar a fórmula: \[\\overrightarrow{{AB}}= “\\color{{#A80}}{{B}}-\\color{{teal}}{{A}}” \\\\ \\overrightarrow{{AB}}= \\color{{#A80}}{{(x_b, y_b, z_b)}} - \\color{{teal}}{{(x_a, y_a, z_a)}} \\\\ \\overrightarrow{{AB}}= (\\color{{#A80}}{{x_b}} - \\color{{teal}}{{x_a}}, \\color{{#A80}}{{y_b}} - \\color{{teal}}{{y_a}}, \\color{{#A80}}{{z_b}} - \\color{{teal}}{{z_a}})\].
<br>Sendo \(\\color{{teal}}{{A({v[0]}, {v[1]}, {v[2]})}}\) e \(\\color{{#A80}}{{B({u[0]}, {u[1]}, {u[2]})}}\).
Temos:
\(\\overrightarrow{{AB}}= “\\color{{#A80}}{{B}}-\\color{{teal}}{{A}}”\)
\(\\overrightarrow{{AB}}= \\color{{#A80}}{{B({u[0]}, {u[1]}, {u[2]})}}- \\color{{teal}}{{A({v[0]}, {v[1]}, {v[2]})}}\)
\(\\overrightarrow{{AB}}= (\\color{{#A80}}{{{u[0]}}} - \\color{{teal}}{{({v[0]})}}, \\color{{#A80}}{{{u[1]}}} - \\color{{teal}}{{({v[1]})}}, \\color{{#A80}}{{{u[2]}}} - \\color{{teal}}{{({v[2]})}})\)
\(\\overrightarrow{{AB}}= ({u[0] - v[0]}, {u[1] - v[1]}, {u[2] - v[2]})\)
</body>
</html>"""
    )

    with open("calculo1.html", "w") as file:
        file.write(text)


def gerar_calculo_perpendincularismo(v=(0, 0, 0), u=(0, 0, 0)):
    e =calcularProdutoEscalar(v, u)
    text = (
        HTML_BASE
        + f"""Quando dois vetores \(\\color{{teal}}{{\\vec v=(a, b, c)}}\) e \(\\color{{#A80}}{{\\vec u=(d, e, f)}}\) são perpendiculares, o seu produto escalar é \(0\), então \(\\color{{teal}}{{\\vec v}} \\cdot \\color{{#A80}}{{\\vec u}} = 0\).<br>

<br>Sendo \(\\color{{teal}}{{\\vec v=({v[0]}, {v[1]}, {v[2]})}}\) e \(\\color{{#A80}}{{\\vec u=({u[0]}, {u[1]}, {u[2]})}}\).
Temos:
\(\\color{{teal}}{{({v[0]}, {v[1]}, {v[2]})}} \\cdot \\color{{#A80}}{{({u[0]}, {u[1]}, {u[2]})}} = {e}\). Como \({e}\){'' if e == 0 else ' não'} é igual a \(0\), então os vetores \(\\color{{teal}}{{\\vec v=({v[0]}, {v[1]}, {v[2]})}}\) e \(\\color{{#A80}}{{\\vec u=({u[0]}, {u[1]}, {u[2]})}}\)<b>{'' if e == 0 else ' não'} são perpendiculares</b>.<br>

<br><b>OBS:</b> Para saber como calcular o produto escalar passo a passo, vá até a seção "Produto Escalar" nesta calculadora.
</body>
</html>"""
    )

    with open("calculo1.html", "w") as file:
        file.write(text)


def gerar_calculo_paralelismo(v=(0, 0, 0), u=(0, 0, 0)):
    w = calcularProdutoVetorial(v, u)
    neq = "\\neq"
    text = (
        HTML_BASE
        + f"""Quando dois vetores \(\\color{{teal}}{{\\vec v=(a, b, c)}}\) e \(\\color{{#A80}}{{\\vec u=(d, e, f)}}\) são paralelos, o seu produto vetorial é um vetor nulo, então \(\\color{{teal}}{{\\vec v}} \\times \\color{{#A80}}{{\\vec u}} = (0, 0, 0) = \\vec o\).<br>

<br>Sendo \(\\color{{teal}}{{\\vec v=({v[0]}, {v[1]}, {v[2]})}}\) e \(\\color{{#A80}}{{\\vec u=({u[0]}, {u[1]}, {u[2]})}}\).
Temos:
\(\\color{{teal}}{{({v[ 0]}, {v[1]}, {v[2]})}} \\times \\color{{#A80}}{{({u[0]}, {u[1]}, {u[2]})}} = ({w[0]}, {w[1]}, {w[2]}) {'=' if w == (0, 0, 0) else neq}\\vec o\). Como \(({w[0]}, {w[1]}, {w[2]})\){'' if w == (0, 0, 0) else ' não'} é um vetor nulo, então os vetores \(\\color{{teal}}{{\\vec v=({v[0]}, {v[1]}, {v[2]})}}\) e \(\\color{{#A80}}{{\\vec u=({u[0]}, {u[1]}, {u[2]})}}\)<b>{'' if w == (0, 0, 0) else ' não'} são paralelos</b>.<br>

<br><b>OBS:</b> Para saber como calcular o produto vetorial passo a passo, vá até a seção "Produto Vetorial" nesta calculadora.
</body>
</html>"""
)
    

    with open("calculo1.html", "w") as file:
        file.write(text)


def gerar_calculo_produto_escalar(v=(0, 0, 0), u=(0, 0, 0)):
    text = (
        HTML_BASE
        + f"""Para calcular o produto escalar de dois vetores \(\\vec v=(a, b, c)\) e \(\\vec u=(d, e, f)\), podemos usar a fórmula: \(\\vec v \\cdot \\vec u = ((ad) + (be) + (cf))\).
<br>Sendo \(\\vec v=({v[0]}, {v[1]}, {v[2]})\) e \(\\vec u=({u[0]}, {u[1]}, {u[2]})\).
Temos:
    \(\\vec v \\cdot \\vec u = (({v[0]})({u[0]}) + ({v[1]})({u[1]}) + ({v[2]})({u[2]}))\).<br>
    \(\\vec v \\cdot \\vec u = (({v[0]*u[0]}) + ({v[1]*u[1]}) + ({v[2]*u[2]}))\).<br>
    \(\\vec v \\cdot \\vec u = (({(v[0]*u[0]) + (v[1]*u[1]) + (v[2]*u[2])}))\).<br>

</body>
</html>"""
    )

    with open("calculo1.html", "w") as file:
        file.write(text)


def gerar_calculo_produto_vetorial(v=(0, 0, 0), u=(0, 0, 0)):
    """Para facilitar na hora de resolver o determinante, eu repeti algumas colunas do lado.
        \[
          \\begin{{array}}{{cc|ccc|cc}}
          & & \\hat i & \\hat j & \\hat k & & \\\\
          & \\color{{red}}{{{v[2]}}} & \\color{{teal}}{{{v[0]}}} & \\color{{teal}}{{{v[1]}}} & \\color{{red}}{{{v[2]}}} \\\\
          \\color{{#A80}}{{{u[0]}}} & \\color{{#A80}}{{{u[1]}}} & \\color{{#A80}}{{{u[2]}}} 
          \\end{{array}}
          
          \]"""
    
    text = (
        HTML_BASE
        + f"""Para calcular o produto vetorial de dois vetores \(\\vec a=(x_a, y_a, z_a)\) e \(\\vec b=(x_b, y_b, z_b)\), podemos usar dois métodos. Vamos ver agora o método do <b>determinante simbólico</b>:<br>
        1. Colocamos \(\\hat i\) \(\\hat j\) \(\\hat k\) na primeira linha do determinante.<br>
        2. Colocamos as coordenadas do vetor \(\\color{{teal}}{{\\vec a=(x_a, y_a, z_a)}}\) na segunda linha do determinante.<br>
        3. Colocamos as coordenadas do vetor \(\\color{{#A80}}{{\\vec b=(x_b, y_b, z_b)}}\) na terceira linha do determinante.<br>

        Assim, o determinante fica:
        \[
          \\begin{{vmatrix}}
          \\hat i & \\hat j & \\hat k \\\\
          \\color{{teal}}{{x_a}} & \\color{{teal}}{{y_a}} & \\color{{teal}}{{z_a}} \\\\
          \\color{{#A80}}{{x_b}} & \\color{{#A80}}{{y_b}} & \\color{{#A80}}{{z_b}} 
          \\end{{vmatrix}}
          \]

Resolvendo o determinante simbólico temos:<br>
\[\\vec a \\times \\vec b = \\hat i((y_a z_b) - (z_a y_b)) \\\\+ \\hat j((z_a x_b) - (x_a z_b)) \\\\+ \\hat k((x_ay_b) - (y_ax_b))\]

Sendo \(\\color{{teal}}{{\\vec a=({v[0]}, {v[1]}, {v[2]})}}\) e \(\\color{{#A80}}{{\\vec b=({u[0]}, {u[1]}, {u[2]})}}\).<br>
O determinante fica:
        \[
          \\begin{{vmatrix}}{{}}
          \\hat i & \\hat j & \\hat k \\\\
          \\color{{teal}}{{{v[0]}}} & \\color{{teal}}{{{v[1]}}} & \\color{{teal}}{{{v[2]}}} \\\\
          \\color{{#A80}}{{{u[0]}}} & \\color{{#A80}}{{{u[1]}}} & \\color{{#A80}}{{{u[2]}}} 
          \\end{{vmatrix}}
          \]
Vamos resolver o determinante:<br>
1. Obtemos o \(\\hat i (\\color{{red}}{{({v[1]})({u[2]})}})\)
\[
  \\begin{{vmatrix}}{{}}
  \\color{{red}}{{\\hat i}} & \\hat j & \\hat k \\\\
  \\color{{teal}}{{{v[0]}}} & \\color{{red}}{{{v[1]}}} & \\color{{teal}}{{{v[2]}}} \\\\
  \\color{{#A80}}{{{u[0]}}} & \\color{{#A80}}{{{u[1]}}} & \\color{{red}}{{{u[2]}}} 
  \\end{{vmatrix}}
  \]

2. Obtemos o \(\\hat i (({v[1]})({u[2]}) - \\color{{red}}{{({v[2]})({u[1]})}})\)
\[
  \\begin{{vmatrix}}{{}}
  \\color{{red}}{{\\hat i}} & \\hat j & \\hat k \\\\
  \\color{{teal}}{{{v[0]}}} & \\color{{teal}}{{{v[1]}}} & \\color{{red}}{{{v[2]}}} \\\\
  \\color{{#A80}}{{{u[0]}}} & \\color{{red}}{{{u[1]}}} & \\color{{#A80}}{{{u[2]}}} 
  \\end{{vmatrix}}
  \]

Então temos \(\\hat i (({v[1]*u[2]}) - ({v[2]*u[1]})) = \\hat i ({(v[1]*u[2]) - (v[2]*u[1])}) = {(v[1]*u[2]) - (v[2]*u[1])}\\hat i\).<br>

3. Obtemos o \({(v[1]*u[2]) - (v[2]*u[1])}\\hat i + \\hat j (\\color{{red}}{{({v[2]})({u[0]})}})\)
\[
  \\begin{{vmatrix}}{{}}
  \\hat i & \\color{{red}}{{\\hat i}} & \\hat k \\\\
  \\color{{teal}}{{{v[0]}}} & \\color{{teal}}{{{v[1]}}} & \\color{{red}}{{{v[2]}}} \\\\
  \\color{{red}}{{{u[0]}}} & \\color{{#A80}}{{{u[1]}}} & \\color{{#A80}}{{{u[2]}}} 
  \\end{{vmatrix}}
  \]

4. Obtemos o \({(v[1]*u[2]) - (v[2]*u[1])}\\hat i +  \\hat j (({v[2]})({u[0]}) - \\color{{red}}{{({v[0]})({u[2]})}})\)
\[
  \\begin{{vmatrix}}{{}}
  \\hat i & \\color{{red}}{{\\hat j}} & \\hat k \\\\
  \\color{{red}}{{{v[0]}}} & \\color{{teal}}{{{v[1]}}} & \\color{{teal}}{{{v[2]}}} \\\\
  \\color{{#A80}}{{{u[0]}}} & \\color{{#A80}}{{{u[1]}}} & \\color{{red}}{{{u[2]}}} 
  \\end{{vmatrix}}
  \]

Então temos \(\\hat j (({v[2]*u[0]}) - ({v[0]*u[2]})) = \\hat j ({(v[2]*u[0]) - (v[0]*u[2])}) = {(v[2]*u[0]) - (v[0]*u[2])}\\hat j\).<br>

5. Obtemos o \({(v[1]*u[2]) - (v[2]*u[1])}\\hat i {((v[2]*u[0]) - (v[0]*u[2])) if ((v[2]*u[0]) - (v[0]*u[2])) < 0 else f'+{((v[2]*u[0]) - (v[0]*u[2]))}'}\\hat j + \\hat k (\\color{{red}}{{({v[0]})({u[1]})}})\)
\[
  \\begin{{vmatrix}}{{}}
  \\hat i & \\hat j & \\color{{red}}{{\\hat k}} \\\\
  \\color{{red}}{{{v[0]}}} & \\color{{teal}}{{{v[1]}}} & \\color{{teal}}{{{v[2]}}} \\\\
  \\color{{#A80}}{{{u[0]}}} & \\color{{red}}{{{u[1]}}} & \\color{{#A80}}{{{u[2]}}} 
  \\end{{vmatrix}}
  \]

6. Obtemos o \({(v[1]*u[2]) - (v[2]*u[1])}\\hat i {((v[2]*u[0]) - (v[0]*u[2])) if ((v[2]*u[0]) - (v[0]*u[2])) < 0 else f'+{((v[2]*u[0]) - (v[0]*u[2]))}'}\\hat j + \\hat k (({v[2]})({u[0]}) - \\color{{red}}{{({v[1]})({u[0]})}})\)
\[
  \\begin{{vmatrix}}
  \\hat i & \\hat j & \\color{{red}}{{\\hat k}} \\\\
  \\color{{teal}}{{{v[0]}}} & \\color{{red}}{{{v[1]}}} & \\color{{teal}}{{{v[2]}}} \\\\
  \\color{{red}}{{{u[0]}}} & \\color{{#A80}}{{{u[1]}}} & \\color{{#A80}}{{{u[2]}}} 
  \\end{{vmatrix}}
  \]

Então temos \(\\hat k (({v[0]*u[1]}) - ({v[1]*u[0]})) = \\hat k ({(v[0]*u[1]) - (v[1]*u[0])}) = {(v[0]*u[1]) - (v[1]*u[0])}\\hat k\).<br>

Assim o resultado do produto vetorial é:<br>
\(\\vec a \\times \\vec b ={(v[1]*u[2]) - (v[2]*u[1])}\\hat i {((v[2]*u[0]) - (v[0]*u[2])) if ((v[2]*u[0]) - (v[0]*u[2])) < 0 else f'+{((v[2]*u[0]) - (v[0]*u[2]))}'}\\hat j {((v[0]*u[1]) - (v[1]*u[0])) if ((v[0]*u[1]) - (v[1]*u[0])) < 0 else f'+{(v[0]*u[1]) - (v[1]*u[0])}'}\\hat k\)<br>
\(\\vec a \\times \\vec b =({(v[1]*u[2]) - (v[2]*u[1])}, {(v[2]*u[0]) - (v[0]*u[2])}, {(v[0]*u[1]) - (v[1]*u[0])})\)

</body>
</html>"""
    )

    with open("calculo1.html", "w") as file:
        file.write(text)


def gerar_calculo_produto_misto(v=(0, 0, 0), u=(0, 0, 0), w=(0, 0, 0)):
    text = (
        HTML_BASE
        + f"""Para calcular o produto misto de três vetores \(\\color{{teal}}{{\\vec a=(x_a, y_a, z_a)}}\), \(\\color{{#A80}}{{\\vec b=(x_b, y_b, z_b)}}\), \(\\color{{#080}}{{\\vec c=(x_c, y_c, z_c)}}\). Vamos ver resolver o determinante:<br>
        1. Colocamos as coordenadas do vetor \(\\color{{teal}}{{\\vec a=(x_a, y_a, z_a)}}\) na primeira linha do determinante.<br>
        2. Colocamos as coordenadas do vetor \(\\color{{#A80}}{{\\vec b=(x_b, y_b, z_b)}}\) na segunda linha do determinante.<br>
        3. Colocamos as coordenadas do vetor \(\\color{{#080}}{{\\vec c=(x_c, y_c, z_c)}}\) na terceira linha do determinante.<br>

        Assim, o determinante fica:
        \[
          \\begin{{vmatrix}}
          \\color{{teal}}{{x_a}} & \\color{{teal}}{{y_a}} & \\color{{teal}}{{z_a}} \\\\
          \\color{{#A80}}{{x_b}} & \\color{{#A80}}{{y_b}} & \\color{{#A80}}{{z_b}} \\\\
          \\color{{#080}}{{x_c}} & \\color{{#080}}{{y_c}} & \\color{{#080}}{{z_c}}
          \\end{{vmatrix}}
          \]
Para obter o valor do produto misto, \(\\left |\\left [\\color{{teal}}{{\\vec a}}, \\color{{#A80}}{{\\vec b}}, \\color{{#080}}{{\\vec c}}\\right ]\\right |\) é só calcular o determinante.<br>
Sendo \(\\color{{teal}}{{\\vec a=({v[0]}, {v[1]}, {v[2]})}}\), \(\\color{{#A80}}{{\\vec b=({u[0]}, {u[1]}, {u[2]})}}\) e \(\\color{{#080}}{{\\vec c=({w[0]}, {w[1]}, {w[2]})}}\).<br>
O determinante fica:
        \[
          \\begin{{vmatrix}}{{}}
          \\color{{teal}}{{{v[0]}}} & \\color{{teal}}{{{v[1]}}} & \\color{{teal}}{{{v[2]}}} \\\\
          \\color{{#A80}}{{{u[0]}}} & \\color{{#A80}}{{{u[1]}}} & \\color{{#A80}}{{{u[2]}}} \\\\
          \\color{{#080}}{{{w[0]}}} & \\color{{#080}}{{{w[1]}}} & \\color{{#080}}{{{w[2]}}} 
          \\end{{vmatrix}}
          \]
Vamos resolver o determinante:<br>
1. Multiplicamos todos os itens na diagonal pintada de azul e adicionamos a conta:<br>
\(\\left |\\left [\\color{{teal}}{{\\vec a}}, \\color{{#A80}}{{\\vec b}}, \\color{{#080}}{{\\vec c}}\\right ]\\right | = \\color{{#00F}}{{({v[0]*u[1]*w[2]})}}\)<br>
\[
  \\begin{{vmatrix}}{{}}
  \\color{{#00F}}{{{v[0]}}} & \\color{{teal}}{{{v[1]}}} & \\color{{teal}}{{{v[2]}}} \\\\
  \\color{{#A80}}{{{u[0]}}} & \\color{{#00F}}{{{u[1]}}} & \\color{{#A80}}{{{u[2]}}} \\\\
  \\color{{#080}}{{{w[0]}}} & \\color{{#080}}{{{w[1]}}} & \\color{{#00F}}{{{w[2]}}} 
  \\end{{vmatrix}}
  \]

2. Multiplicamos todos os itens na diagonal pintada de azul e adicionamos a conta <b>subtraindo</b>:<br>
\(\\left |\\left [\\color{{teal}}{{\\vec a}}, \\color{{#A80}}{{\\vec b}}, \\color{{#080}}{{\\vec c}}\\right ]\\right | = {v[0]*u[1]*w[2]} 
\\color{{#00F}}{{{f'- ({v[0]*u[2]*w[1]})'}}}\)<br>

\[
  \\begin{{vmatrix}}
  \\color{{#00F}}{{{v[0]}}} & \\color{{teal}}{{{v[1]}}} & \\color{{teal}}{{{v[2]}}} \\\\
  \\color{{#A80}}{{{u[0]}}} & \\color{{#A80}}{{{u[1]}}} & \\color{{#00F}}{{{u[2]}}} \\\\
  \\color{{#080}}{{{w[0]}}} & \\color{{#00F}}{{{w[1]}}} & \\color{{#080}}{{{w[2]}}} 
  \\end{{vmatrix}}
  \]
3. Multiplicamos todos os itens na diagonal pintada de azul e adicionamos a conta <b>somando</b>:<br>
\(\\left |\\left [\\color{{teal}}{{\\vec a}}, \\color{{#A80}}{{\\vec b}}, \\color{{#080}}{{\\vec c}}\\right ]\\right | = {v[0]*u[1]*w[2]} 
{-1*v[0]*u[2]*w[1] if (-1*v[0]*u[2]*w[1]) < 0 else f'+{-1*v[0]*u[2]*w[1]}'} 
\\color{{#00F}}{{{f'+ ({v[1]*u[2]*w[0]})'}}}\)<br>
\[
  \\begin{{vmatrix}}{{}}
  \\color{{teal}}{{{v[0]}}} & \\color{{#00F}}{{{v[1]}}} & \\color{{teal}}{{{v[2]}}} \\\\
  \\color{{#A80}}{{{u[0]}}} & \\color{{#A80}}{{{u[1]}}} & \\color{{#00F}}{{{u[2]}}} \\\\
  \\color{{#00F}}{{{w[0]}}} & \\color{{#080}}{{{w[1]}}} & \\color{{#080}}{{{w[2]}}} 
  \\end{{vmatrix}}
  \]
4. Multiplicamos todos os itens na diagonal pintada de azul e adicionamos a conta <b>subtraindo</b>:<br>
\(\\left |\\left [\\color{{teal}}{{\\vec a}}, \\color{{#A80}}{{\\vec b}}, \\color{{#080}}{{\\vec c}}\\right ]\\right | = {v[0]*u[1]*w[2]} 
{v[0]*u[2]*w[1] if (v[0]*u[2]*w[1]) < 0 else f'+{v[0]*u[2]*w[1]}'} 
{v[1]*u[2]*w[0] if (v[1]*u[2]*w[0]) < 0 else f'+{v[1]*u[2]*w[0]}'} 
\\color{{#00F}}{{{f'- ({v[1]*u[0]*w[2]})'}}}\)<br>
\[
  \\begin{{vmatrix}}{{}}
  \\color{{teal}}{{{v[0]}}} & \\color{{#00F}}{{{v[1]}}} & \\color{{teal}}{{{v[2]}}} \\\\
  \\color{{#00F}}{{{u[0]}}} & \\color{{#A80}}{{{u[1]}}} & \\color{{#A80}}{{{u[2]}}} \\\\
  \\color{{#080}}{{{w[0]}}} & \\color{{#080}}{{{w[1]}}} & \\color{{#00F}}{{{w[2]}}} 
  \\end{{vmatrix}}
  \]

5. Multiplicamos todos os itens na diagonal pintada de azul e adicionamos a conta <b>somando</b>:<br>
\(\\left |\\left [\\color{{teal}}{{\\vec a}}, \\color{{#A80}}{{\\vec b}}, \\color{{#080}}{{\\vec c}}\\right ]\\right | = {v[0]*u[1]*w[2]} 
{-1*v[0]*u[2]*w[1] if (-1*v[0]*u[2]*w[1]) < 0 else f'+{-1*v[0]*u[2]*w[1]}'} 
{v[1]*u[2]*w[0] if (v[1]*u[2]*w[0]) < 0 else f'+{v[1]*u[2]*w[0]}'} 
{-1*v[1]*u[0]*w[2] if (-1*v[1]*u[0]*w[2]) < 0 else f'+{-1*v[1]*u[0]*w[2]}'} 
\\color{{#00F}}{{{f'+ ({v[2]*u[0]*w[1]})'}}}\)<br>
\[
  \\begin{{vmatrix}}{{}}
  \\color{{teal}}{{{v[0]}}} & \\color{{teal}}{{{v[1]}}} & \\color{{#00F}}{{{v[2]}}} \\\\
  \\color{{#00F}}{{{u[0]}}} & \\color{{#A80}}{{{u[1]}}} & \\color{{#A80}}{{{u[2]}}} \\\\
  \\color{{#080}}{{{w[0]}}} & \\color{{#00F}}{{{w[1]}}} & \\color{{#080}}{{{w[2]}}} 
  \\end{{vmatrix}}
  \]
6. Multiplicamos todos os itens na diagonal pintada de azul e adicionamos a conta <b>subtraindo</b>:<br>
\(\\left |\\left [\\color{{teal}}{{\\vec a}}, \\color{{#A80}}{{\\vec b}}, \\color{{#080}}{{\\vec c}}\\right ]\\right | = {v[0]*u[1]*w[2]} 
{-1*v[0]*u[2]*w[1] if (-1*v[0]*u[2]*w[1]) < 0 else f'+{-1*v[0]*u[2]*w[1]}'} 
{v[1]*u[2]*w[0] if (v[1]*u[2]*w[0]) < 0 else f'+{v[1]*u[2]*w[0]}'} 
{-1*v[1]*u[0]*w[2] if (-1*v[1]*u[0]*w[2]) < 0 else f'+{-1*v[1]*u[0]*w[2]}'} 
{v[2]*u[0]*w[1] if (v[2]*u[0]*w[1]) < 0 else f'+{v[2]*u[0]*w[1]}'}
\\color{{#00F}}{{{f'- ({v[2]*u[1]*w[0]})'}}} 
\)<br>
\[
  \\begin{{vmatrix}}{{}}
  \\color{{teal}}{{{v[0]}}} & \\color{{teal}}{{{v[1]}}} & \\color{{#00F}}{{{v[2]}}} \\\\
  \\color{{#A80}}{{{u[0]}}} & \\color{{#00F}}{{{u[1]}}} & \\color{{#A80}}{{{u[2]}}} \\\\
  \\color{{#00F}}{{{w[0]}}} & \\color{{#070}}{{{w[1]}}} & \\color{{#070}}{{{w[2]}}} 
  \\end{{vmatrix}}
  \]
Então temos: <br>
\(\\left |\\left [\\color{{teal}}{{\\vec a}}, \\color{{#A80}}{{\\vec b}}, \\color{{#080}}{{\\vec c}}\\right ]\\right | = {v[0]*u[1]*w[2]} 
{-1*v[0]*u[2]*w[1] if (-1*v[0]*u[2]*w[1]) < 0 else f'+{-1*v[0]*u[2]*w[1]}'} 
{v[1]*u[2]*w[0] if (v[1]*u[2]*w[0]) < 0 else f'+{v[1]*u[2]*w[0]}'} 
{-1*v[1]*u[0]*w[2] if (-1*v[1]*u[0]*w[2]) < 0 else f'+{-1*v[1]*u[0]*w[2]}'} 
{v[2]*u[0]*w[1] if (v[2]*u[0]*w[1]) < 0 else f'+{v[2]*u[0]*w[1]}'}
{-1*v[2]*u[1]*w[0] if (-1*v[2]*u[1]*w[0]) < 0 else f'+{-1*v[2]*u[1]*w[0]}'} =
{
(v[0]*u[1]*w[2]) +
(-1*v[0]*u[2]*w[1]) +
(v[1]*u[2]*w[0]) +
(-1*v[1]*u[0]*w[2]) +
(v[2]*u[0]*w[1]) +
(-1*v[2]*u[1]*w[0])
}

\)<br>
Assim o resultado do produto vetorial é:<br>
\(\\left |\\left [\\color{{teal}}{{\\vec a}}, \\color{{#A80}}{{\\vec b}}, \\color{{#080}}{{\\vec c}}\\right ]\\right | = 
{
(v[0]*u[1]*w[2]) +
(-1*v[0]*u[2]*w[1]) +
(v[1]*u[2]*w[0]) +
(-1*v[1]*u[0]*w[2]) +
(v[2]*u[0]*w[1]) +
(-1*v[2]*u[1]*w[0])
}
\)<br>

</body>
</html>"""
    )

    with open("calculo1.html", "w") as file:
        file.write(text)


def gerar_calculo_pos_relativa_duas_retas(pR = (0, 0, 0), vR = (0, 0, 0), pS = (0, 0, 0), uS = (0, 0, 0)):
    w = calcularProdutoVetorial(vR, uS)
    pRpS = obterVetorDePontos(pR, pS)
    pSpR = obterVetorDePontos(pS, pR)

    x = calcularProdutoEscalar(pRpS, w)
    tp = ((pSpR[0]*uS[0]) == (pSpR[1]*uS[1]) == (pSpR[2]*uS[2]))
    text = (
        HTML_BASE
        + f"""Duas retas \(r: A + \\vec v\) e \(s: B + \\vec u\) podem ser:<br>
- Paralelas distintas (Quando \(\\vec v \\times \\vec u = \\vec o\) e teste do ponto da negativo);<br>
- Paralelas coincidentes (Quando \(\\vec v \\times \\vec u = \\vec o\) e teste do ponto da positivo);<br>
- Concorrentes (Quando \(|\\vec AB, \\vec v, \\vec u| = 0\));<br>
- Reversas (Quando \(|\\vec AB, \\vec v, \\vec u| \\neq 0\)).<br>
<br>
Sendo \(r: {pR} + \\color{{teal}}{{h{vR}}}\) e \(s: {pS} + \\color{{#A80}}{{t{uS}}}\).<br>
<br>
1. Vamos checar se os vetores diretores das retas são paralelos.
\(\\color{{teal}}{{{vR}}} \\times \\color{{#A80}}{{{uS}}} = {w}\)<br>""")

    text += (f"""Os vetores diretores são paralelos então as retas são parelas.<br>

<br> 2. Teste do ponto. Uma forma de se fazer é usando a fórmula \(A-B * \\color{{#A80}}{{\\vec u}} = (k, k, k)\) ou \(B-A * \\color{{teal}}{{\\vec v}} = (k, k, k)\); onde \(A\) é um ponto da reta \(r\) e \(B\) da reta \(s\). Se o resultado dessa conta for um vetor com <i>todas as cordenadas iguais</i>, então o teste do ponto é positivo e as retas são paralelas coicidentes.<br>
Sendo \(A{pR}\), \(B{pS}\) e \(\\color{{#A80}}{{{uS}}}\) o vetor diretor da reta \(s\). Temos que \((A{pR} - B{pS})(\\color{{#A80}}{{{uS}}}) 
\(= {pSpR}\\color{{#A80}}{{{uS}}}\)
\(= ({pR[0]} - {pS[0]}, {pR[1]} - {pS[1]}, {pR[2]} - {pS[2]})\\color{{#A80}}{{{uS}}}\)
\(= (({pSpR[0]})(\\color{{#A80}}{{{uS[0]}}}), ({pSpR[1]})(\\color{{#A80}}{{{uS[1]}}}), ({pSpR[2]})(\\color{{#A80}}{{{uS[2]}}}))\)
\(= {(pSpR[0]*uS[0], pSpR[1]*uS[1], pSpR[2]*uS[2])}\).<br>
Já que no resultado{'' if tp else ' nem'} todas as cordenadas são iguais, então as duas retas são <b>paralelas {'coincidentes' if tp else 'distintas'}</b>. 

""" if w == (0,0,0) else f"""<br>Os vetores diretores não são paralelos então as retas não são parelas. Vamos calcular o produto misto, para saber se as retas são concorrentes ou reversas. Sendo \(A{pR}\) ponto de \(r\), \(B{pS}\) ponto de \(s\), e \({w}\) o resultado do produto vetorial dos vetores diretores das retas \(r\) e \(s\). Formando o vetor \(\\color{{blue}}{{\\overrightarrow{{AB}}}} = {pS}-{pR}\) \(= \\color{{blue}}{{{pRpS}}}\) Sabemos que o produto misto \(\left [\\vec x, \\vec y, \\vec z \\right] = \\vec x \\cdot (\\vec y \\times \\vec z)\). 
Já sabemos que \(\\color{{teal}}{{{vR}}} \\times \\color{{#A80}}{{{uS}}} = {w}\), agora só falta fazer o produto escalar entre {w} e \(\\color{{blue}}{{\\overrightarrow{{AB}}}}\), para obter o resultado do produto misto. Temos que \(\\color{{blue}}{{{pRpS}}} \\cdot {w} = {x}\).
<br> Como o produto escalar entre \(\\color{{blue}}{{{pRpS}}} \\cdot {w}\) é {'igual' if x == 0 else 'diferente'} a 0. Então as duas retas são {'concorrentes' if x == 0 else 'reversas'}.
""")
    text += ("""
<br><br><b>OBS</b>: Para saber como formar um vetor de dois pontos, checar se vetores são paralelos, calcular produto escalar, vetorial e misto; Vá até a respectiva seção nesta calculadora.

</body>
</html>""")
    

    with open("calculo1.html", "w") as file:
        file.write(text)


def fractex(n, d, simplifcar=False):
    f = Fraction(n, d)
    n = f.numerator
    d = f.denominator

    if simplifcar and n % 2 == 0:
        return f'\\frac{{{n*2}}}{{2}} = {n}'
    else:
        return f'{n}' if d == 1 else f'\\frac{{{n}}}{{{d}}}'
def sinal(n):
    return '+' if n >= 0 else ''


def completar_incognita(a = 1, b = 2, x = 'x'):
    result = []
    if a==1:
        result.append(f'''<p>Vamos operar agora a equação \({x}^2 + {b}{x}\).</p><ol>
    <li>Como \(a = 1\) não precisamos colocar \(a\) em evidência, a equação continua a mesma: \({x}^2 + {b}{x}\)</li>
    <li>Começamos a completar quadrado usando essa estrutura e copiando as partes pintadas: \(\color{{#A80}}{{{x}}}^2
      \color{{#A80}}{{{sinal(b)}}} {b}{x} \\to \left(\color{{#A80}}{{{x} +}}\ \\right)^2\)</li>
    <li>Adicionamos \(-()^2\) no local pintado: \(\left({x} +\ \\right)^2 \color{{#A80}}{{-()^2}}\)</li>
    <li>Dividimos \({b}\) por \(2\), teremos \({fractex(b, 2, True)}\) e colocamos no local pintado: \[\left({x} {sinal(b)}
      \color{{#A80}}{{{fractex(b, 2)}}}\ \\right)^2 - \left(\color{{#A80}}{{{fractex(b, 2)}}}\\right)^2\]</li>
  </ol>''')
        result.append(f'\left({x} {sinal(b)} {fractex(b, 2)}\\right)^2')
        result.append(f'\left({fractex(b, 2)}\\right)^2')

    else:
        result.append(f'''<p>Vamos operar agora a equação \({a}{x}^2 {sinal(b)} {b}{x}\).</p>
        <ol>
    <li>Como \(a \\neq 1\) colocamos \(a\) em evidência: \({a}\left[{x}^2 {sinal(Fraction(b, a))} \\frac{{{b}{x}}}{a}\\right]\)</li>
    <li>Começamos a completar quadrado usando essa estrutura e copiando as partes pintadas: \({a}\left[\color{{#A80}}{{{x}}}^2
      \color{{#A80}}{{{sinal(Fraction(b, a))}}} \\frac{{{b}{x}}}{{{a}}} \\right] \\to {a}\left[ \left(\color{{#A80}}{{{x} +}}\ \\right)^2 \\right]\)
    </li>

    <li>Adicionamos \(-()^2\) no local pintado: \({a}\left[ \left({x} +\ \\right)^2 \color{{#A80}}{{-()^2}} \\right]\)
    <li>Dividimos \({fractex(b, a, simplifcar=True)}\) por \(2\), teremos \({fractex(b, 2*a, simplifcar=True)}\) e colocamos no local pintado: 
    \({a}\left[ \left({x} {sinal(Fraction(b, a))}
      \color{{#A80}}{{{fractex(b, 2*a)}}}\ \\right)^2 - \left(\color{{#A80}}{{{fractex(b, 2*a)}}} \\right)^2 \\right]\)</li>
    <li>Operando a equação teremos: \[\color{{#A80}}{{{a}}}\left[ \left({x} {sinal(Fraction(b, a))} {fractex(b, 2*a)}\ \\right)^2 - \left({fractex(b, 2*a)} \\right)^2 \\right]\\\
    \color{{#A80}}{{{a}}}\left({x} {sinal(Fraction(b, a))} {fractex(b, 2*a)}\ \\right)^2 - \color{{#A80}}{{{a}}}\left({fractex(b, 2*a)} \\right)^2\]</li>
  </ol>''')
    result.append(f'{a}\left({x} {sinal(Fraction(b, a))} {fractex(b, 2*a)}\ \\right)^2')
    result.append(f'{a}\left({fractex(b, 2*a)}\\right)^2')

    return result

def gerar_completar_quadrado(equation, result, x, y = None, z = None, F = 0):

    if F:
        F *= -1
    else:
        F = 0

    resultado = ""
    incognitas = {}
    if x and x[0] and x[1] and x[0] != 0:
        incognitas['x'] = {"a": x[0], "b": x[1], "c": 0, 'd':1, 'expr':[]}
    if y and y[0] and y[1] and (y[0] != 0):
        incognitas['y'] = {"a": y[0], "b": y[1], "c": 0, 'd':1, 'expr':[]}
    if z and z[0] and z[1] and z[0] != 0:
        incognitas['z'] = {"a": z[0], "b": z[1], "c": 0, 'd':1, 'expr':[]}
    if not incognitas:
        raise ValueError

    text = (
        HTML_BASE
        + f"""<p>Completar quadrado é justamente o contrário de expandir um produto notável. Por exemplo, expandindo \((a + b)^2\) vamos obter \(a² + 2ab + b^2\). Já ao completar quadrado vamos começar com \(a² + 2ab + b^2\) e chegar a \((a + b)^2\), seguimos os passos:</p>
        <details>
    <summary>Clique para ver os passos</summary>
    <ol>
      <li>Começamos com uma equação do tipo \(ax^2 + bx + c = 0\).</li>
      <li>Passamos o \(c\) para o outro lado: \(ax^2 + bx = -c\).</li>
      <li>Se \(a \\neq 1\) colocamos \(a\) em evidência: \(a\left[x^2 + \\frac{{bx}}{{a}}\\right] = -c\)</li>
      <li>Começamos a completar quadrado usando essa estrutura e copiando as partes pintadas: \(a\left[\color{{#A80}}{{x}}^2
        \color{{#A80}}{{+}} \\frac{{bx}}{{a}}\\right] = -c \\to a\left[ \left(\color{{#A80}}{{x +}}\ \\right)^2\\right] = -c\)</li>
      <li>Adicionamos \(-()^2\) no local pintado: \(a\left[ \left(x +\ \\right)^2 \color{{#A80}}{{-()^2}}\\right] = -c\)</li>
      <li>Dividimos \(\\frac{{b}}{{a}}\) por 2, teremos \(\\frac{{b}}{{2a}}\) e colocamos no local pintado: \(a\left[ \left(x +
        \color{{#A80}}{{\\frac{{b}}{{2a}}}}\ \\right)^2 - \left(\color{{#A80}}{{\\frac{{b}}{{2a}}}}\\right)^2\\right] = -c\)</li>
      <li>Operando a equação teremos: \[\color{{#A80}}{{a}}\left[ \left(x + \\frac{{b}}{{2a}}\ \\right)^2 -
        \left(\\frac{{b}}{{2a}}\\right)^2\\right] = -c\\
        \color{{#A80}}{{a}}\left(x + \\frac{{b}}{{2a}}\ \\right)^2 - \color{{#A80}}{{a}}\left(\\frac{{b}}{{2a}}\\right)^2 = -c\\
        a\left(x + \\frac{{b}}{{2a}}\ \\right)^2 = -c + \color{{#A80}}{{a\left(\\frac{{b}}{{2a}}\\right)^2}}\]</li>
    </ol>
  </details>
  <p>Temos a equação \({equation}\), vamos completar quadrado nela.</p>""")
    for k, i in incognitas.items():
        incognitas[k]['expr'] = completar_incognita(i['a'], i['b'], k)
        text += incognitas[k]['expr'][0]

    text += f"""<p>Após completar quadrado nossa equação \({equation}\), fica:
    \["""
    for k, i in incognitas.items():
        if text[-1] == '[':
            text += f"{i['expr'][1]} - {i['expr'][2]}"
        else:
            text += f"{'+' if i['expr'][1] != '-' else ''} {i['expr'][1]} - {i['expr'][2]}"
    text += f' = {F} \\\\'
    final = ''
    for k, i in incognitas.items():
        if text[-1] == '\\':
            text += f"{i['expr'][1]}"
        else:
            text += f"{'+' if i['expr'][1] != '-' else ''} {i['expr'][1]}"
        if final == '':
            final += f"{i['expr'][2]}"
        else:
            final += f"{'+' if i['expr'][2] != '-' else ''}{i['expr'][2]}"
    text += f" = {final}{'+' if F >= 0 else ''}{F} \\\\"
    text += f'{result}\] </body></html>'


    with open("calculo1.html", "w") as file:
        file.write(text)