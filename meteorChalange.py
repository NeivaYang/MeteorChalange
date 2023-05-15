from PIL import Image
from collections import defaultdict
##################################################################
# # Carregar a imagem
# image = Image.open("C:\meteor chalange\meteor_challenge_01.png")

# # Exibir a imagem
# image.show()
def find_color_ranges(image_path, target_color):
    # Abre a imagem
    image = Image.open(image_path)

    # Verifica o modo de cor da imagem e converte para RGB, se necessário
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Obtém as dimensões da imagem
    width, height = image.size

    # Lista para armazenar as faixas de coordenadas das porções de cores
    color_ranges = []

    # Variável para acompanhar a faixa atual
    current_range = None

    # Varre todos os pixels da imagem
    for y in range(height):
        for x in range(width):
            # Obtém a cor do pixel (R, G, B)
            r, g, b = image.getpixel((x, y))

            # Verifica se a cor do pixel corresponde à cor alvo
            if (r, g, b) == target_color:
                if current_range is None:
                    # Inicia uma nova faixa
                    current_range = [x, x]
                else:
                    # Continua a faixa atual
                    current_range[1] = x
            else:
                if current_range is not None:
                    # Finaliza a faixa atual
                    color_ranges.append(current_range)
                    current_range = None

    # Verifica se há uma faixa inacabada no final da imagem
    if current_range is not None:
        color_ranges.append(current_range)

    # Retorna a lista de faixas de coordenadas das porções de cores
    return color_ranges


##################################################################

def count_colors(image_path):
    # Abre a imagem
    image = Image.open(image_path)
    
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Obtém as dimensões da imagem
    width, height = image.size
    
    # Dicionário para armazenar a contagem de cada cor
    color_counts = defaultdict(int)

    # Varre todos os pixels da imagem
    for y in range(height):   
        for x in range(width):
            # Obtém a cor do pixel (R, G, B)
            r, g, b = image.getpixel((x, y))
            
            # Verifica se a cor corresponde aos valores RGB desejados
            if r == 255 and g == 255 and b == 255:  #branco
                color_counts["numeroDeEstrelas"] += 1
            elif r == 255 and g == 0 and b == 0:  #vermelho
                color_counts["numeroDeMeteoros"] += 1


            if r == 255 and g == 0 and b == 0:
                if((x >= 59 and x <= 94) or (x >= 126 and x <= 160) or (x >= 241 and x <= 296) or (x >= 473 and x <= 533) or (x >= 664 and x <= 696)):
                    color_counts["meteorosCaindoNaAgua"] += 1
            
    # Retorna a contagem
    return color_counts

# Caminho da imagem do meteor chalange
image_path = r"C:\meteor chalange\meteor_challenge_01.png"

# Chama a função para contar as cores
colors = count_colors(image_path)

target_color = (0, 0, 255) 

# Chama a função para encontrar as faixas de coordenadas da cor alvo
color_ranges = find_color_ranges(image_path, target_color)
sorted_ranges = sorted(color_ranges, key=lambda x: x[0])

# Imprime as faixas de coordenadas da cor alvo
for range in sorted_ranges:
    x_inicial, x_final = range
    # largura = x_final - x_inicial
    
    # print(largura)
    
    # print(f"Faixa de Coordenadas: {x_inicial} a {x_final}")

print("=============================================")
print("=============================================")
# Imprime a contagem de cada cor
for color, count in colors.items():
    print(f"{color}: {count}")
print("=============================================")
print("=============================================")