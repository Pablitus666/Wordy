from PIL import Image, ImageFilter, ImageChops

def add_shadow(image: Image.Image, offset=(3, 3), shadow_color=(0, 0, 0, 90), blur_radius=3, border=5):
    """ Añade una sombra paralela profesional. """
    if image.mode != 'RGBA':
        image = image.convert('RGBA')

    pad = max(abs(offset[0]), abs(offset[1])) + border
    total_width = image.width + 2 * pad
    total_height = image.height + 2 * pad
    
    canvas = Image.new('RGBA', (total_width, total_height), (0, 0, 0, 0))
    shadow_layer = Image.new('RGBA', image.size, shadow_color)
    canvas.paste(shadow_layer, (pad + offset[0], pad + offset[1]), image.getchannel('A'))
    
    if blur_radius > 0:
        canvas = canvas.filter(ImageFilter.GaussianBlur(blur_radius))
    
    canvas.paste(image, (pad, pad), image)
    return canvas

def add_relief(image: Image.Image, intensity=2):
    """ 
    Aplica un efecto de relieve de 3 capas (Luz + Sombra + Original).
    Simula el efecto de biselado profesional.
    """
    if image.mode != 'RGBA':
        image = image.convert('RGBA')

    width, height = image.size
    # Crear capas de luz y sombra (blanco y negro con baja opacidad)
    light_layer = Image.new('RGBA', (width, height), (255, 255, 255, 120))
    dark_layer = Image.new('RGBA', (width, height), (0, 0, 0, 120))

    # Lienzo final con margen para el desplazamiento
    relief_canvas = Image.new('RGBA', (width, height), (0, 0, 0, 0))

    # 1. Dibujar Sombra (desplazada abajo-derecha)
    relief_canvas.paste(dark_layer, (intensity, intensity), image.getchannel('A'))
    
    # 2. Dibujar Luz (desplazada arriba-izquierda)
    relief_canvas.paste(light_layer, (-intensity, -intensity), image.getchannel('A'))

    # 3. Dibujar Imagen Original en el centro
    relief_canvas.paste(image, (0, 0), image)

    return relief_canvas
