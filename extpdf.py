import io
import requests
import base64
from pdf2image import convert_from_path
import tempfile
import json

def extract_all_text_from_pdf_with_api_key(pdf_path, api_key):
    """
    Extract all text from each page of a PDF using Google Cloud Vision API with an API key.
    
    Args:
        pdf_path: Path to the PDF file
        api_key: Your Google Cloud Vision API key
        
    Returns:
        A dictionary with page numbers as keys and extracted text as values
    """
    # API endpoint
    vision_api_url = f"https://vision.googleapis.com/v1/images:annotate?key={api_key}"
    
    # Convert PDF to images
    print(f"Converting PDF to images: {pdf_path}")
    with tempfile.TemporaryDirectory() as temp_dir:
        images = convert_from_path(
            pdf_path,
            dpi=300,  # Higher DPI for better quality
            output_folder=temp_dir,
            fmt="png"
        )
        
        results = {}
        
        # Process each page
        for i, image in enumerate(images):
            page_num = i + 1
            print(f"Processing page {page_num}/{len(images)}")
            
            # Save image to memory buffer
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)
            
            # Encode image
            img_content = base64.b64encode(img_byte_arr.read()).decode('utf-8')
            
            # Create request payload
            request_json = {
                "requests": [
                    {
                        "image": {
                            "content": img_content
                        },
                        "features": [
                            {
                                "type": "DOCUMENT_TEXT_DETECTION"
                            }
                        ]
                    }
                ]
            }
            
            # Make API request
            response = requests.post(
                vision_api_url,
                json=request_json
            )
            
            if response.status_code == 200:
                response_data = response.json()
                
                # Extract full text
                try:
                    text = response_data['responses'][0]['fullTextAnnotation']['text']
                    results[page_num] = text
                except KeyError:
                    print(f"No text found on page {page_num}")
                    results[page_num] = ""
            else:
                print(f"Error on page {page_num}: {response.text}")
                results[page_num] = f"ERROR: {response.status_code}"
                
        return results

def main():
    # Your API key
    api_key = "YOUR_API_KEY_HERE"
    
    # Example usage - replace with your PDF path
    pdf_path = "UD-105.pdf"
    
    # Extract all text from the PDF
    all_text = extract_all_text_from_pdf_with_api_key(pdf_path, api_key)
    
    # Print results
    for page_num, text in all_text.items():
        print(f"\n--- PAGE {page_num} ---\n")
        print(text)
        
        # Optionally save to file
        with open(f"page_{page_num}_text.txt", "w") as f:
            f.write(text)

if __name__ == "__main__":
    main()
