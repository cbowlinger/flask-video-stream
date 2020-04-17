import cv2
import marker_detection

def process_image(img):
  cv2.rectangle(img, (0, 0), (50, 50), (0, 0, 255), thickness=5)
  return img

def capture_and_save(img):
  processed_image = process_image(img)
  cv2.imwrite("images/last.png", processed_image)