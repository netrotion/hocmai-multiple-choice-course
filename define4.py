import html
from sympy import latex

# Chuỗi cần chuyển đổi
html_string = "x<sub>1</sub>"

# Sử dụng thư viện html để parse và trích xuất chỉ số dưới
decoded_string = html.unescape(html_string)

# Chuyển đổi thành cú pháp LaTeX bằng sympy
latex_expr = latex(decoded_string)

print(latex_expr)
