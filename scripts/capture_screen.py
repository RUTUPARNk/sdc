from PIL import Image
import numpy as np

def capture_screen(driver):
    # Capture the screenshot
    screenshot = driver.get_screenshot_as_png()
    
    # Convert to a PIL image
    image = Image.open(BytesIO(screenshot))
    
    # Convert to a NumPy array
    image_np = np.array(image)
    
    return image_np

screen = capture_screen(driver)

