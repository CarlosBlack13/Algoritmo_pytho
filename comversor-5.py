
def metros_para_centimetros(metros):
    centimetros = metros * 100  # 1 metro = 100 centímetros
    return centimetros


metros = float(input("Digite o valor em metros: "))
centimetros = metros_para_centimetros(metros)
print(f"{metros} metros equivalem a {centimetros} centímetros.")
