import os

c = "\[\sqrt{{{c}}}\]"
HTML_BASE = """<!DOCTYPE html>
<html>
<head>
<title>MathJax TeX Test Page</title>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\\(','\\\)']]}});
</script>
<script type="text/javascript" async src="mathjax2/MathJax.js?config=TeX-AMS_CHTML"></script>

<!--
  <script type="text/javascript" async src="mathjax2/MathJax.js?config=TeX-AMS_CHTML"></script>
  <script src="mathjax3/tex-chtml.js" id="MathJax-script" async></script>
  </!-->
<!--
  <script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"></script>
!-->
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
        + f"""Para formar um vetor \(\\overrightarrow{{AB}}=(a, b, c)\) com os pontos \(A(x_a, y_a, z_a)\) e \(B(x_b, y_b, z_b)\), podemos usar a fórmula: \[\\overrightarrow{{AB}}= “B-A” \\\\ \\overrightarrow{{AB}}= (x_b, y_b, z_b) - (x_a, y_a, z_a) \\\\ \\overrightarrow{{AB}}= (x_b - x_a, y_b - y_a, z_b - z_a)\].
<br>Sendo \(A({v[0]}, {v[1]}, {v[2]})\) e \(B({u[0]}, {u[1]}, {u[2]})\).
Temos:
\(\\overrightarrow{{AB}}= “B-A”\)
\(\\overrightarrow{{AB}}= B({u[0]}, {u[1]}, {u[2]})- A({v[0]}, {v[1]}, {v[2]})\)
\(\\overrightarrow{{AB}}= ({u[0]} - ({v[0]}), {u[1]} - ({v[1]}), {u[2]} - ({v[2]}))\)
\(\\overrightarrow{{AB}}= ({u[0] - v[0]}, {u[1] - v[1]}, {u[2] - v[2]})\)
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
        + f"""Para 
        
        Para subtrair dois vetores \(\\vec v=(a, b, c)\) e \(\\vec u=(d, e, f)\), podemos usar a fórmula: \(\\vec v + \\vec u = (a + d, b + e, c + f)\).
<br>Sendo \(\\vec v=({v[0]}, {v[1]}, {v[2]})\) e \(\\vec u=({u[0]}, {u[1]}, {u[2]})\).
Temos:
    \(\\vec v + \\vec u = ({v[0]} + {u[0]}, {v[1]} + {u[1]}, {v[2]} + {u[2]})\).<br>
    \(\\vec v + \\vec u = ({v[0]+u[0]}, {v[1]+u[1]}, {v[2]+u[2]})\).
</body>
</html>"""
    )

    with open("calculo1.html", "w") as file:
        file.write(text)
