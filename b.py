from keras.models import load_model
import cv2
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on the default camera of your computer
camera = cv2.VideoCapture(0)

# Set the desired window size
window_width, window_height = 800, 600
cv2.namedWindow("Webcam Image", cv2.WINDOW_NORMAL)  # Create a resizable window
cv2.resizeWindow("Webcam Image", window_width, window_height)
cardboard_index = 3

if not camera.isOpened():
    print("No camera detected. Make sure your camera is connected.")
else:
    while True:
        # Grab the webcam's image.
        ret, image = camera.read()

        if not ret:
            print("Error: Could not read a frame from the camera.")
            break

        # Resize the raw image into (224-height, 224-width) pixels
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        # Make the image a numpy array and reshape it to the model's input shape.
        image_input = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image_input = (image_input / 127.5) - 1

        # Predict the model
        prediction = model.predict(image_input)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        # Draw the class name and confidence score on the image with a smaller font
        # text = f"Class: {class_name[2:]} | Confidence Score: {str(np.round(confidence_score * 100))[:-2]}%"
        if index == 0 :
            text = "Paper"
        elif index == 1 :
            text = "Plastic"
        else:
            text = "Others"
            # text = f"{class_name[2:]}"
        cv2.putText(image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1)

        # Show the image in a window
        cv2.imshow("Webcam Image", image)

        # Listen to the keyboard for presses.
        keyboard_input = cv2.waitKey(1)

        # 27 is the ASCII for the Esc key on your keyboard.
        if keyboard_input == 27:
            break

    camera.release()
    cv2.destroyAllWindows()
