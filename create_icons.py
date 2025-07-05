from PIL import Image, ImageDraw
import os

# Make sure the Graphics directory exists
graphics_dir = os.path.join("Frontend", "Graphics")
os.makedirs(graphics_dir, exist_ok=True)

# Create a Send icon
def create_send_icon():
    img = Image.new('RGBA', (24, 24), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw paper airplane shape
    points = [(2, 12), (20, 12), (14, 6), (2, 12), (14, 18), (20, 12)]
    draw.polygon(points, fill=(86, 204, 242, 255), outline=(76, 194, 232))
    
    # Save the image
    img.save(os.path.join(graphics_dir, "Send.png"))

# Create an Upload icon
def create_upload_icon():
    img = Image.new('RGBA', (24, 24), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw upload arrow
    # Arrow shaft
    draw.rectangle((10, 8, 14, 18), fill=(155, 89, 182, 255))
    # Arrow head
    points = [(7, 10), (12, 4), (17, 10)]
    draw.polygon(points, fill=(155, 89, 182, 255))
    # Base line
    draw.rectangle((6, 18, 18, 20), fill=(155, 89, 182, 255))
    
    # Save the image
    img.save(os.path.join(graphics_dir, "Upload.png"))

# Create Minimize icon
def create_minimize_icon():
    img = Image.new('RGBA', (24, 24), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw minimize line
    draw.rectangle((4, 12, 20, 16), fill=(200, 200, 200, 255))
    
    # Save the image
    img.save(os.path.join(graphics_dir, "Minimize.png"))

# Create Maximize icon
def create_maximize_icon():
    img = Image.new('RGBA', (24, 24), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw maximize square
    draw.rectangle((4, 4, 20, 20), outline=(200, 200, 200, 255), width=2)
    
    # Save the image
    img.save(os.path.join(graphics_dir, "Maximize.png"))

# Create icons
create_send_icon()
create_upload_icon()
create_minimize_icon()
create_maximize_icon()

print("Icons created successfully in", graphics_dir) 