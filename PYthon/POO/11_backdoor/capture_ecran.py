from PIL import ImageGrab


capture_ecran = ImageGrab.grab()

capture_ecran.save("capture.png", "PNG")