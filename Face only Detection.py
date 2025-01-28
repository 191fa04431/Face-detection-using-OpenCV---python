import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(r"C:\Users\ch.avinash chowdary\Downloads\Haarcascades\Haarcascades\haarcascade_frontalface_default.xml")

# Read the input image
img = cv2.imread(r"C:\Users\ch.avinash chowdary\Downloads\IMG20210307171353.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (450, 0, 0), 2)

# Display the output image
cv2.imshow('Detected Faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()