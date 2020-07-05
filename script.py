# text recognition
import cv2
import pandas as pd
TEST_DIR='Data Files/Test.csv'
import pytesseract
# read image
#pytesseract.pytesseract.tesseract_cmd =r'tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe'
def __str(path):
	image = cv2.imread(path)
	# configurations
	 # importing modules

	# read image

	# configurations
	config = ('-l eng --oem 1 --psm 3')
	# pytessercat
	text = pytesseract.image_to_string(image, config=config)
	# print text
	#text = text.split('\n')
	#print(text)
	conv=[]
	for texter in text:
		if texter!='' and texter!='\n':
			conv.append(texter)
	return conv	
#print(conv)
df=pd.read_csv(TEST_DIR)
'''for con in conv:
					f.write(con)'''
print(df.head())
import os
path_files='Data Files/Dataset'
for images in os.listdir(path_files):
	img_path=os.path.join(path_files,images)
	#print(img_path)
	img=cv2.imread(img_path)
	text=__str(img_path)
	print(text)