from PIL import Image, ImageDraw, ImageFont
import os

size = 512
img = Image.new('RGBA', (size, size), (15, 15, 19, 255))
draw = ImageDraw.Draw(img)

# Subtle radial gradient circle
for y in range(size):
    for x in range(size):
        dx = x - size // 2
        dy = y - size // 2
        dist = (dx * dx + dy * dy) ** 0.5
        t = min(dist / (size * 0.45), 1.0)
        r = int(255 * (1 - t) * 0.15)
        g = int((209 * (1 - t) + 194 * t) * 0.12)
        b = int(220 * (1 - t) * 0.15)
        if dist < size * 0.48:
            img.putpixel((x, y), (15 + r, 15 + g, 19 + b, 255))

# Font loading
font = None
for path in [
    'C:/Windows/Fonts/arialbd.ttf',
    'C:/Windows/Fonts/segoeuib.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
]:
    try:
        font = ImageFont.truetype(path, 260)
        break
    except Exception:
        continue
if font is None:
    font = ImageFont.load_default()

bbox = draw.textbbox((0, 0), 'BTZ', font=font)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]
x = (size - tw) // 2 - bbox[0]
y = (size - th) // 2 - bbox[1]

# Gradient text: pink -> lilac blend
colors = [
    (255, 209, 220, 255),   # pink
    (248, 205, 230, 255),
    (240, 200, 238, 255),
    (232, 197, 242, 255),   # mid blend
    (224, 195, 248, 255),
    (216, 194, 255, 255),   # lilac
]
steps = len(colors)
for i, color in enumerate(colors):
    offset_x = int((i - steps // 2) * 1.5)
    offset_y = int((i - steps // 2) * 0.8)
    draw.text((x + offset_x, y + offset_y), 'BTZ', fill=color, font=font)

img.save('icon.png')
print('OK icon.png', os.path.getsize('icon.png'), 'bytes')
