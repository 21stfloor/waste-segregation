import cv2
import numpy as np
import tensorflow as tf

# Load the pre-trained MobileNetV2 model
model = tf.keras.applications.MobileNetV2(weights="imagenet")

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No camera detected. Make sure your camera is connected.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Preprocess the image to the format expected by MobileNetV2
        img = cv2.resize(frame, (224, 224))
        img = tf.keras.applications.mobilenet_v2.preprocess_input(img)
        img = np.expand_dims(img, axis=0)

        # Make predictions
        predictions = model.predict(img)

        # Decode the predictions and display the top result
        decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions)
        top_prediction = decoded_predictions[0][0]

        # Display the recognition result on the frame
        label = f"{top_prediction[1]} ({top_prediction[2] * 100:.2f}%)"
        cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Webcam Feed', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
