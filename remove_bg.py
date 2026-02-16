from PIL import Image
import math

def remove_white_bg(path):
    try:
        img = Image.open(path).convert("RGBA")
        datas = img.getdata()
        new_data = []
        
        # Check top-left pixel to see what "background" is likely to be
        bg_sample = datas[0]
        print(f"Background sample (0,0): {bg_sample}")

        for item in datas:
            # Calculate distance from white
            r, g, b, a = item
            dist = math.sqrt((255-r)**2 + (255-g)**2 + (255-b)**2)
            
            # If it's very close to white (distance < 100), make it transparent
            # 100 covers light grays and off-whites
            if dist < 100:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)
                
        img.putdata(new_data)
        img.save(path, "PNG")
        print(f"Successfully processed {path} with distance-based removal")
    except Exception as e:
        print(f"Error processing image: {e}")

remove_white_bg("/Users/raidlassel/Desktop/bkpr/Bkeeprs chat gpt vers/beetravel-logo.png")
