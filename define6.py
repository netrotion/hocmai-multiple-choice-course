def format_to_superscript(text):
    superscript_map = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    superscript_text = text.translate(superscript_map)
    return superscript_text

# Sử dụng hàm để chuyển đổi chuỗi "2" thành dạng mũ ²
input_text = "13"
result = format_to_superscript(input_text)
print("Dạng mũ ² của '2':", result)
