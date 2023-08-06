# Install
```
pip install latexman
```

# Quick Start
In LaTeX (as opposed to classic TeX) You should use \\(123\\) and \\[ 123\\] environments instead of \$123\$ and \$\$123\$\$ respectively. 

See https://tex.stackexchange.com/questions/510/are-and-preferable-to-dollar-signs-for-math-mode

The function `convert_dollar_sign_to_latex_counterpart()` helps converting \$123\$ in math mode to \\(123\\) and \$$123$$ to \\[123\\]
```
from latexman import convert_dollar_sign_to_latex_counterpart as conv

filepath = 'main.tex'
conv(filepath)
```