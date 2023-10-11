import cv2 
import pytesseract 
import time
webcam = cv2.VideoCapture(0)
tempo_inicial = time.time()
esperar = 4
if webcam:
    validacao, frame = webcam.read()
    caminho = r"C:\Users\Bernardo\AppData\Local\Programs\Tesseract-OCR"
    pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
    while validacao:
        validacao, frame = webcam.read()
        cv2.imshow("video da webcam", frame)
        tempo_atual = time.time()
        if tempo_atual - tempo_inicial >= esperar:
            texto = pytesseract.image_to_string(frame)
            print(texto)
            tempo_inicial = tempo_atual
        key = cv2.waitKey(5)
        if key == 27:
            break
    cv2.imwrite("fotoBernardo.png", frame)
webcam.release()
cv2.destroyAllWindows()      