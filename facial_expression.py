import cv2
import numpy as np
from fer import FER
import matplotlib.pyplot as plt

def analyze_facial_expression(image_path):
    """
    Analyze facial expressions in an image using FER (Facial Expression Recognition)
    
    Parameters:
    image_path (str): Path to the input image file
    
    Returns:
    tuple: (processed image with annotations, detected emotions)
    """
    
    detector = FER(mtcnn=True)
    
   
    img = cv2.imread(image_path)
    
    
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Detect emotions
    result = detector.detect_emotions(rgb_img)
    
    
    output_img = rgb_img.copy()
    
    detected_emotions = []
    
    # Process detected faces
    if result:
        for face in result:
            # Get face box coordinates
            x, y, w, h = [int(coord) for coord in face['box']]
            
            # Draw rectangle around face
            cv2.rectangle(output_img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            
            # Get emotions
            emotions = face['emotions']
            dominant_emotion = max(emotions.items(), key=lambda x: x[1])[0]
            
            # Add text above the rectangle
            text = f"{dominant_emotion}: {emotions[dominant_emotion]:.2f}%"
            cv2.putText(output_img, text, (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
            
            detected_emotions.append(emotions)
    
    return output_img, detected_emotions

def display_results(image, emotions):
    """
    Display the processed image and emotion analysis results
    
    Parameters:
    image: Processed image with annotations
    emotions: List of detected emotions
    """
    plt.figure(figsize=(12, 8))
    plt.imshow(image)
    plt.axis('off')
    plt.title('Facial Expression Analysis')
    plt.show()
    
    if emotions:
        print("\nDetected Emotions:")
        for idx, emotion_dict in enumerate(emotions, 1):
            print(f"\nFace #{idx}:")
            for emotion, score in emotion_dict.items():
                print(f"{emotion}: {score:.2f}%")
    else:
        print("No faces detected in the image.")


if __name__ == "__main__":
    
    image_path = "image.jpg"
    
    try:
        processed_image, emotions = analyze_facial_expression(image_path)
        display_results(processed_image, emotions)
    except Exception as e:
        print(f"Error processing image: {str(e)}")



