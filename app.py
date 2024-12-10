import cv2
import numpy as np

def preprocess_image(image_path): 
    """
    Reads, resizes, and binarizes an image.
    """
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) 
    if img is None:
        raise ValueError(f"Image not found at {image_path}")
    
    img = cv2.resize(img, (200, 100))
    _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
    return img

def compare_signatures(ref_img, input_img): 
    """
    Compares two images using template matching.
    """
    result = cv2.matchTemplate(ref_img, input_img, cv2.TM_CCOEFF_NORMED) 
    _, similarity_score, _, _ = cv2.minMaxLoc(result) 
    return similarity_score

if __name__ == "__main__":
    # File paths
    ref_image_path = 'img1.jpg'
    input_image_path = 'img2.jpg'

    try:
        # Preprocess images
        ref_img = preprocess_image(ref_image_path)
        input_img = preprocess_image(input_image_path)

        # Compare signatures
        similarity_score = compare_signatures(ref_img, input_img)
        
        # Define threshold
        threshold = 0.8

        # Print results
        if similarity_score >= threshold:
            print(f"Signatures match (Similarity Score: {similarity_score:.2f})")
        else:
            print(f"Signatures do not match (Similarity Score: {similarity_score:.2f})")
    
    except Exception as e:
        print(f"Error: {e}")
