import os
c='\[\sqrt{{{c}}}\]'

def gerar_calculo_soma(v=(0, 0, 0), u=(0, 0, 0)):
    text = """<!DOCTYPE html>
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
<body>""" + f"""Para subtrair dois vetores \(\\vec v=(a, b, c)\) e \(\\vec u=(d, e, f)\), podemos usar a fórmula: \(\\vec v + \\vec u = (a + d, b + e, c + f)\).
<br>Sendo \(\\vec v=({v[0]}, {v[1]}, {v[2]})\) e \(\\vec u=({u[0]}, {u[1]}, {u[2]})\).
Temos:
    \(\\vec v + \\vec u = ({v[0]} + {u[0]}, {v[1]} + {u[1]}, {v[2]} + {u[2]})\).<br>
    \(\\vec v + \\vec u = ({v[0]+u[0]}, {v[1]+u[1]}, {v[2]+u[2]})\).
</body>
</html>"""


    with open('calculo1.html', 'w') as file:
        file.write(text)

def gerar_calculo_subtração(v=(0, 0, 0), u=(0, 0, 0)):
    text = """<!DOCTYPE html>
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
<body>""" + f"""Para subtrair dois vetores \(\\vec v=(a, b, c)\) e \(\\vec u=(d, e, f)\), podemos usar a fórmula: \(\\vec v - \\vec u = (a - d, b - e, c - f)\).
<br>Sendo \(\\vec v=({v[0]}, {v[1]}, {v[2]})\) e \(\\vec u=({u[0]}, {u[1]}, {u[2]})\).
Temos:
    \(\\vec v - \\vec u = ({v[0]} - ({u[0]}), {v[1]} - ({u[1]}), {v[2]} - ({u[2]}))\).<br>
    \(\\vec v - \\vec u = ({v[0]-u[0]}, {v[1]-u[1]}, {v[2]-u[2]})\).


</body>
</html>"""
    
    with open('calculo1.html', 'w') as file:
        file.write(text)
    

def gerar_calculo_formar_vetores(v=(0, 0, 0), u=(0, 0, 0)):
    text = """<!DOCTYPE html>
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
<body>""" + f"""Para formar um vetor \(\\overrightarrow{{AB}}=(a, b, c)\) com os pontos \(A(x_a, y_a, z_a)\) e \(B(x_b, y_b, z_b)\), podemos usar a fórmula: \[\\overrightarrow{{AB}}= “B-A” \\\\ \\overrightarrow{{AB}}= (x_b, y_b, z_b) - (x_a, y_a, z_a) \\\\ \\overrightarrow{{AB}}= (x_b - x_a, y_b - y_a, z_b - z_a)\].
<br>Sendo \(A({v[0]}, {v[1]}, {v[2]})\) e \(B({u[0]}, {u[1]}, {u[2]})\).
Temos:
\(\\overrightarrow{{AB}}= “B-A”\)
\(\\overrightarrow{{AB}}= B({u[0]}, {u[1]}, {u[2]})- A({v[0]}, {v[1]}, {v[2]})\)
\(\\overrightarrow{{AB}}= ({u[0]} - ({v[0]}), {u[1]} - ({v[1]}), {u[2]} - ({v[2]}))\)
\(\\overrightarrow{{AB}}= ({u[0] - v[0]}, {u[1] - v[1]}, {u[2] - v[2]})\)
</body>
</html>"""


    with open('calculo1.html', 'w') as file:
        file.write(text)