from PIL import Image
import math

def remove_background(image_path, output_path, tolerance=160): # Increased tolerance even more
    try:
        img = Image.open(image_path).convert("RGBA")
        datas = img.getdata()
        
        # Get background color from top-left pixel
        bg_color = datas[0]
        
        new_data = []
        for item in datas:
            # Calculate distance from background color
            dist = math.sqrt(
                (item[0] - bg_color[0])**2 +
                (item[1] - bg_color[1])**2 +
                (item[2] - bg_color[2])**2
            )
            
            # Simple thresholding logic
            if dist < tolerance:
                new_data.append((0, 0, 0, 0)) # Transparent
            else:
                new_data.append(item)

        img.putdata(new_data)
        img.save(output_path, "PNG")
        print(f"Processed {image_path} -> {output_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

if __name__ == "__main__":
    # Arabic Icon (Ain)
    remove_background(
        "/Users/raidlassel/.gemini/antigravity/brain/6e43b434-2324-411a-8bdc-3bcdbb833fd4/simple_icon_ar_ain_1770779844173.png",
        "/Users/raidlassel/Desktop/bkpr/Bkeeprs chat gpt vers/icon-ar-v2.png"
    )
    # English Icon (EN)
    remove_background(
        "/Users/raidlassel/.gemini/antigravity/brain/6e43b434-2324-411a-8bdc-3bcdbb833fd4/simple_icon_en_v2_1770779858172.png",
        "/Users/raidlassel/Desktop/bkpr/Bkeeprs chat gpt vers/icon-en-v2.png"
    )
