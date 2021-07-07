import cv2

imagem = cv2.imread('Imagem.png')
gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)

cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
	epsilon = 0.01*cv2.arcLength(c,True)
	approx = cv2.approxPolyDP(c,epsilon,True)

	x,y,w,h = cv2.boundingRect(approx)

	if len(approx)==3:
		cv2.putText(imagem,'Triangulo ', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==4:
		aspect_ratio = float(w)/h
		print('aspect_ratio= ', aspect_ratio)
		if aspect_ratio == 1:
			cv2.putText(imagem,'Quadrado', (x,y-5),1,1,(0,255,0),1)
		else:
			cv2.putText(imagem,'Retangulo', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==5:
		cv2.putText(imagem,'Pentagono', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==6:
		cv2.putText(imagem,'Hexagono', (x,y-5),1,1,(0,255,0),1)

	if len(approx)>10:
		cv2.putText(imagem,'Circulo', (x,y-5),1,1,(0,255,0),1)

	cv2.drawContours(imagem, [approx], 0, (0,255,0),2)
	cv2.imshow('imagem',imagem)
	cv2.waitKey(0)