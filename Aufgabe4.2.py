import cv2

# Bild laden
img = cv2.imread("yoshi.png")

# Breite, Höhe und Anzahl der Farbkanäle ausgeben
height, width, channels = img.shape
print("Breite:", width)
print("Höhe:", height)
print("Anzahl der Farbkanäle:", channels)

# Bildformat in Fließkomma ändern
img_float = img.astype(float)

# Bild als Float anzeigen
#cv2.imshow("Original", img)
cv2.imshow("Float", img_float / 255.0)

# Rotes Quadrat in die Mitte des Bildes einzeichnen
square_size = 10
center_x = width // 2
center_y = height // 2
top_left = (center_x - square_size // 2, center_y - square_size // 2)
bottom_right = (center_x + square_size // 2, center_y + square_size // 2)
cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), -1)

# Jede 5. Zeile durch schwarze Pixel ersetzen
img[::5, :] = 0

# Bild auf der Festplatte speichern
cv2.imwrite("modifiziertes_yoshi.png", img)

# Modifiziertes Bild laden
modified_img = cv2.imread("modifiziertes_yoshi.png")

# Modifiziertes Bild anzeigen
cv2.imshow("Modifiziert", modified_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
