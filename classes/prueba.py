import pygame
import sys
import time
# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600
SCREEN_SIZE = (WIDTH, HEIGHT)

# Inicializar la ventana
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Elige y coloca bloques")

# Cargar las imágenes de los bloques
block_images = [
    pygame.image.load("assets/Wood.png"),
    pygame.image.load("assets/Concrete.png"),
    pygame.image.load("assets/Iron.png")
]

# Lista para almacenar los bloques
blocks = []

# Fuente para el cuadro de texto
font = pygame.font.Font(None, 36)

# Bucle principal
running = True

# Bloque activo
active_block = None

# Límites de bloques por tipo
block_limits = [10, 10, 10]

# Contadores de bloques por tipo
block_counts = [0, 0, 0]

# Restablecer el tiempo cada 25 segundos
reset_time = 10
last_reset = time.time()

# Restablecer los contadores de bloques
def reset_block_counts():
    for i in range(len(block_counts)):
        block_counts[i] = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botón izquierdo del ratón
                if active_block is not None:
                    x, y = event.pos
                    block_type = block_images.index(active_block)
                    if block_counts[block_type] < block_limits[block_type]:
                        # Crear un bloque como un diccionario que almacena la imagen y la posición
                        block = {"image": active_block, "rect": active_block.get_rect(center=(x, y))}
                        blocks.append(block)
                        block_counts[block_type] += 1
            elif event.button == 3:  # Botón derecho del ratón
                x, y = event.pos
                for block in blocks:
                    if block["rect"].collidepoint(x, y):
                        block_type = block_images.index(block["image"])
                        block_counts[block_type] -= 1
                        blocks.remove(block)

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, image in enumerate(block_images):
                x, y = event.pos
                if pygame.Rect(50 + i * 100, 50, image.get_width(), image.get_height()).collidepoint(event.pos):
                    active_block = block_images[i]

    current_time = time.time()
    if current_time - last_reset >= reset_time:
        reset_block_counts()
        last_reset = current_time


    # Limpiar la pantalla
    screen.fill((255, 255, 255))

    # Dibujar los bloques en la pantalla
    for block in blocks:
        screen.blit(block["image"], block["rect"])

    # Dibujar los botones con imágenes y la cantidad restante
    for i, image in enumerate(block_images):
        screen.blit(image, (50 + i * 100, 50))
        text = f"AMO: {block_limits[i] - block_counts[i]}"
        text_render = font.render(text, True, (0, 0, 0))
        text_x = 50 + i * 100
        text_y = 50 + image.get_height()
        screen.blit(text_render, (text_x, text_y))

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
