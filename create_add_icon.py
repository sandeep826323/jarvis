from PIL import Image, ImageDraw
import os

def create_add_icon():
    # Create a new image with transparency
    size = 128
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Calculate dimensions for the plus symbol
    line_width = size // 8
    padding = size // 4

    # Draw horizontal line
    draw.rectangle(
        [padding, (size - line_width) // 2, size - padding, (size + line_width) // 2],
        fill=(46, 204, 113, 255)  # Green color matching the button style
    )

    # Draw vertical line
    draw.rectangle(
        [(size - line_width) // 2, padding, (size + line_width) // 2, size - padding],
        fill=(46, 204, 113, 255)
    )

    # Save the image
    icon_path = os.path.join("Frontend", "Graphics", "add.png")
    os.makedirs(os.path.dirname(icon_path), exist_ok=True)
    image.save(icon_path)

if __name__ == "__main__":
    create_add_icon() 