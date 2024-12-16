from PIL import Image
import numpy as np

# Carregar a imagem
image_path = '/content/brasil.jpg'  # Substitua com o caminho correto da imagem
img = Image.open(image_path)

# Converter a imagem para escala de cinza e array NumPy
img_gray = img.convert('L')
img_array = np.array(img_gray)

# Contagem de pixels
total_pixels = img_array.size
pixels_no_data = np.sum(img_array == 0)
pixels_soja = np.sum(img_array == 39)
pixels_pastagem = np.sum(img_array == 15)

# Pixels válidos (excluindo os sem dados)
pixels_validos = total_pixels - pixels_no_data

# Dados para o cálculo de áreas
area_brasil_hectares = 851576700  # Área total do Brasil em hectares

# Cálculo das áreas proporcionais
percent_soja = pixels_soja / pixels_validos
percent_pastagem = pixels_pastagem / pixels_validos

area_soja_hectares = percent_soja * area_brasil_hectares
area_pastagem_hectares = percent_pastagem * area_brasil_hectares

# Exibir resultados
print(f"1. Quantidade total de pixels: {total_pixels}")
print(f"2. Quantidade de pixels sem dados (código 0): {pixels_no_data}")
print(f"3. Quantidade de pixels de plantio de soja (código 39): {pixels_soja}")
print(f"4. Quantidade de pixels de pastagem (código 15): {pixels_pastagem}")
print()
print(f"Área de plantio de soja: {area_soja_hectares:.2f} hectares ({pixels_soja} pixels)")
print(f"Área de pastagem: {area_pastagem_hectares:.2f} hectares ({pixels_pastagem} pixels)")
