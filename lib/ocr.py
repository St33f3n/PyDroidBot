import pytesseract
import pyautogui, cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def Ocr(region):
    
    # img_screenshot = cv2.cvtColor(pyautogui.screenshot(region=region), cv2.COLOR_BGR2GRAY)
    img_screenshot = pyautogui.screenshot(region=region)
    img_screenshot.show()
    data = pytesseract.image_to_string(img_screenshot, lang='eng',config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789/:.')

    return data
