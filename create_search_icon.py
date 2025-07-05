from PIL import Image, ImageDraw
import os

def create_search_icon():
    """Create a magnifying glass search icon"""
    # Create a transparent image
    img_size = 64
    img = Image.new('RGBA', (img_size, img_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Define icon colors
    icon_color = (86, 204, 242, 255)  # Blue color matching the theme
    
    # Draw magnifying glass circle
    circle_center = (img_size * 0.4, img_size * 0.4)
    circle_radius = img_size * 0.25
    circle_width = int(img_size * 0.06)
    
    # Draw circle (outer and inner to create a ring)
    draw.ellipse(
        [(circle_center[0] - circle_radius, circle_center[1] - circle_radius),
         (circle_center[0] + circle_radius, circle_center[1] + circle_radius)],
        outline=icon_color,
        width=circle_width
    )
    
    # Draw handle
    handle_start = (
        circle_center[0] + circle_radius * 0.7,
        circle_center[1] + circle_radius * 0.7
    )
    handle_end = (
        circle_center[0] + circle_radius * 1.6,
        circle_center[1] + circle_radius * 1.6
    )
    
    # Draw handle
    draw.line([handle_start, handle_end], fill=icon_color, width=circle_width)
    
    # Save path
    graphics_dir = os.path.join(os.getcwd(), "Frontend", "Graphics")
    if not os.path.exists(graphics_dir):
        os.makedirs(graphics_dir)
        
    save_path = os.path.join(graphics_dir, "Search.png")
    img.save(save_path)
    
    print(f"Search icon created and saved to {save_path}")

if __name__ == "__main__":
    create_search_icon() 