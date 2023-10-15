import cv2
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow as tf
import tensorflow_hub as hub


# Load the MobileNetV2 model from TensorFlow Hub
hub_model = hub.load("https://tfhub.dev/google/circularnet_1/1")

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
        # img = tf.image.convert_image_dtype(img, tf.float32)
        # img = tf.keras.applications.mobilenet_v2.preprocess_input(img)
        # img = np.expand_dims(img, axis=0)

        # get an input size of images on which an Instance Segmentation model is trained
        hub_model_fn = hub_model.signatures["serving_default"]
        height=hub_model_fn.structured_input_signature[1]['inputs'].shape[1]
        width = hub_model_fn.structured_input_signature[1]['inputs'].shape[2]
        input_size = (height, width)

        # apply pre-processing functions which were applied during training the model
        img = cv2.resize(img[0], input_size[::-1], interpolation = cv2.INTER_AREA)
        img = tf.image.convert_image_dtype(img, tf.float32)
        # image_np = build_inputs_for_segmentation(image_np_cp)
        img = tf.expand_dims(img, axis=0)

        # running inference
        # results = hub_model_fn(img)
        # Make predictions
        predictions = hub_model_fn(img)

        # Decode the predictions
        # predicted_class = tf.argmax(predictions, axis=1)
        # class_id = predicted_class.numpy()[0]

        # Display the recognition result on the frame
        # label = f"Class: {class_id}"
        cv2.putText(frame, predictions, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Webcam Feed', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

