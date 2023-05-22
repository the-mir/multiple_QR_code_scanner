import cv2
from pyzbar import pyzbar

def read_qr_code(image):
    # Load the input image
    img = cv2.imread(image)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find QR codes in the image
    qr_codes = pyzbar.decode(gray)

    # Process each QR code
    for qr_code in qr_codes:
        # Extract the data and type of the QR code
        data = qr_code.data.decode("utf-8")
        code_type = qr_code.type

        # Print the data and type
        print("Data:", data)
        print("Type:", code_type)

        # Draw a bounding box around the QR code
        (x, y, w, h) = qr_code.rect
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the image with bounding boxes
    cv2.imshow("QR Code Scanner", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Usage example
for i in range(574):
    image_path = f"C:/Users/88016/Downloads/Concealed/qr_codes/qr_{i}.png"  #path[C:/Users/88016/Downloads/Concealed/qr_codes/qr_{i}.png]
    read_qr_code(image_path)

