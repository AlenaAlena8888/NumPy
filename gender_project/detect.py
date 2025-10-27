import cv2
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('models/gender_model.h5')

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    face = cv2.resize(frame, (128,128))
    face = face / 255.0
    face = np.expand_dims(face, axis=0)

    pred = model.predict(face)
    label = "Male" if pred[0][0] < 0.5 else "Female"

    cv2.putText(frame, f"Gender: {label}", (50,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Gender Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()