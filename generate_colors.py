
import colorsys

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

def mix_color(color1, color2, weight):
    # Linear interpolation
    w2 = weight
    w1 = 1 - w2
    return (
        color1[0] * w1 + color2[0] * w2,
        color1[1] * w1 + color2[1] * w2,
        color1[2] * w1 + color2[2] * w2
    )

def generate_palette(base_hex, name):
    base_rgb = hex_to_rgb(base_hex)
    white = (255, 255, 255)
    black = (0, 0, 0)
    
    # Simple algorithm: 
    # 50-400: mix white with base
    # 500: base
    # 600-950: mix black with base
    
    palette = {}
    
    # Light shades (mix with white)
    # Weights define how much of the original color is kept (approximate)
    # 50 is very light (mostly white), 400 is close to base
    
    # Let's use a scale for mixing with white
    # 50: 95% white, 5% base
    # 100: 90% white, 10% base
    # ...
    # This naive mixing might be too washed out or not vibrant enough, but it is a start.
    # Better approach might be HSL manipulation but linear mixing is standard for many generators.
    
    # Trying to emulate Tailwind's distribution roughly
    shades = {
        50: (white, 0.95),
        100: (white, 0.9),
        200: (white, 0.75),
        300: (white, 0.6),
        400: (white, 0.3),
        500: (None, 0), # Base
        600: (black, 0.1),
        700: (black, 0.25),
        800: (black, 0.45),
        900: (black, 0.6),
        950: (black, 0.75),
    }

    results = []
    print(f"/* {name} Palette */")
    for step in [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]:
        target, weight = shades[step]
        if step == 500:
            final_hex = base_hex
        else:
            final_rgb = mix_color(base_rgb, target, weight)
            final_hex = rgb_to_hex(final_rgb)
        
        # Format name to kebab-case
        kebab_name = name.lower().replace(" ", "-")
        print(f"  --color-{kebab_name}-{step}: {final_hex};")
        results.append((step, final_hex))
    print("")

colors = [
    ("#E9AD2F", "Golden Rod"),
    ("#28272A", "Black Beauty"),
    ("#AB0C29", "Barbados Cherry"), # Fixed typo from user input ABOC29 to AB0C29
    ("#2A512F", "Formal Garden"),
]

for hex_code, name in colors:
    generate_palette(hex_code, name)
