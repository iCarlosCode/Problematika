c=8
f ='\\\(\\\)'
print(f)
def gerar_calculo(v=(0, 0, 0), u=(0, 0, 0)):
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
<body>""" + f"""Para somar dois vetores \(\\vec v=(a, b, c)\) e \(\\vec u=(d, e, f)\), podemos usar a fórmula: \(\\vec v + \\vec u = (a + d, b + e, c + f)\).
<br>Sendo \(\\vec v=({v[0]}, {v[1]}, {v[2]})\) e \(\\vec u=({u[0]}, {u[1]}, {u[2]})\).
Temos:
    \(\\vec v + \\vec u = ({v[0]} + {u[0]}, {v[1]} + {u[1]}, {v[2]} + {u[2]})\).<br>
    \(\\vec v + \\vec u = ({v[0]+u[0]}, {v[1]+u[1]}, {v[2]+u[2]})\).

\[\sqrt{{{c}}}\]
</body>
</html>"""


    with open('calculo1.html', 'w') as file:
        file.write(text)

gerar_calculo((1,2,3), (4,5,6))