import cv2
import face_recognition
import time

def draw_face_box(frame, left, top, right, bottom, label, color):
    cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
    cv2.putText(frame, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

def start_face_detection():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Error: Could not open camera.")
        return False

    print("✅ Camera started...")

    # Load and encode reference face
    try:
        reference_image = face_recognition.load_image_file("pranay face.png")
        image_encoding = face_recognition.face_encodings(reference_image)[0]
    except Exception as e:
        print(f"❌ Error loading face image: {e}")
        cap.release()
        return False

    access_granted = False
    process_frame = True

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Failed to grab frame")
            break

        if process_frame:
            # Resize frame to speed up processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
                match = face_recognition.compare_faces([image_encoding], face_encoding, tolerance=0.45)[0]

                # Scale coordinates back to original frame size
                top *= 2
                right *= 2
                bottom *= 2
                left *= 2

                if match:
                    label = "Access Granted"
                    color = (0, 255, 0)
                    access_granted = True
                else:
                    label = "Access Denied"
                    color = (0, 0, 255)

                draw_face_box(frame, left, top, right, bottom, label, color)

                if access_granted:
                    cv2.putText(frame, 'Hello my name is Pranay pelapkar', (10, 450),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

        process_frame = not process_frame  # Skip alternate frames to reduce lag

        cv2.imshow("Face Detection", frame)

        if access_granted:
            # Show success message for 3 seconds without freezing
            start_time = time.time()
            while time.time() - start_time < 3:
                ret, frame = cap.read()
                if not ret:
                    break
                draw_face_box(frame, left, top, right, bottom, "Access Granted", (0, 255, 0))
                cv2.putText(frame, 'Hello my name is Pranay pelapkar', (10, 450),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
                cv2.imshow("Face Detection", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            break  # Exit outer loop

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return access_granted

if __name__ == "__main__":
    start_face_detection()
