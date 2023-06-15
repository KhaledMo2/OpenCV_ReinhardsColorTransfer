import cv2
import numpy as np

# Yoshi-Bild und Maske laden
yoshi_img = cv2.imread("yoshi.png")
mask_img = cv2.imread("mask.png", cv2.IMREAD_GRAYSCALE)

# Yoshi-Bild in den HSV-Farbraum konvertieren
hsv_img = cv2.cvtColor(yoshi_img, cv2.COLOR_BGR2HSV)

# H-Wert für weiße Pixel in der Maske ändern
hsv_img[..., 0] = np.where(mask_img == 255, 130, hsv_img[..., 0])  # Setzen Sie den H-Wert hier auf den gewünschten Wert (hier: 130)

# HSV-Bild in den BGR-Farbraum konvertieren
result_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

# Bild anzeigen (BGR-Bild)
cv2.imshow("Ergebnis", result_img)
cv2.waitKey(0)

# Optional: Schieberegler zur manuellen Anpassung des H-Werts
def on_hue_change(value):
    hsv_img[..., 0] = value
    result_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
    cv2.imshow("Ergebnis", result_img)

# Schieberegler erstellen
cv2.namedWindow("Ergebnis")
cv2.createTrackbar("H-Wert", "Ergebnis", 120, 180, on_hue_change)

cv2.waitKey(0)
cv2.destroyAllWindows()
