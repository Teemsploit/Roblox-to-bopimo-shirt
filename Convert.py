from PIL import Image
import os
def prompt_file_path(prompt_message, save=False):
    from tkinter import Tk, filedialog
    Tk().withdraw()
    if save:
        file_path = filedialog.asksaveasfilename(title=prompt_message, filetypes=[('Image Files', '*.png')])
    else:
        file_path = filedialog.askopenfilename(title=prompt_message, filetypes=[('Image Files', '*.png;*.jpg;*.jpeg')])
    return file_path
def convert_roblox_to_bopimo(roblox_path, bopimo_output_path):
    roblox_img = Image.open(roblox_path)
    bopimo_img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    roblox_coords = {
        "front": (229, 72, 360, 203),
        "top": (229, 6, 360, 71),
        "left": (163, 72, 228, 203),
        "right": (361, 72, 425, 201),
        "back": (426, 72, 556, 203),
        "bottom": (229, 204, 360, 269),
        "left_arm": (17, 353, 282, 484),
        "right_arm": (306, 353, 571, 484)
    }
    bopimo_coords = {
        "front": (62, 99, 187, 227),
        "top": (62, 11, 187, 98),
        "left": (25, 99, 61, 227),
        "right": (188, 99, 222, 227),
        "back": (223, 99, 344, 227),
        "bottom": (62, 228, 187, 316),
        "left_arm": (25, 327, 193, 500),
        "right_arm": (317, 327, 485, 500)
    }

    for section, roblox_rect in roblox_coords.items():
        bopimo_rect = bopimo_coords[section]
        cropped_section = roblox_img.crop(roblox_rect)
        resized_section = cropped_section.resize((bopimo_rect[2] - bopimo_rect[0],
                                                  bopimo_rect[3] - bopimo_rect[1]))
        bopimo_img.paste(resized_section, bopimo_rect)
    bopimo_img.save(bopimo_output_path)

roblox_path = prompt_file_path("Select a Roblox shirt template to convert:")
bopimo_output_path = prompt_file_path("Save the Bopimo shirt template as:", save=True)
convert_roblox_to_bopimo(roblox_path, bopimo_output_path)
print(f"Conversion complete! Saved to: {bopimo_output_path}")
