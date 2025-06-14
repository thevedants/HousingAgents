# CACI Legal Document Generator

A Python-based system for automatically generating filled CACI (California Civil Jury Instructions) forms from legal documents using Google's Gemini AI API.

## Overview

This project automates the process of filling out CACI jury instruction forms by:
1. Analyzing legal case documents (PDF format)
2. Extracting relevant information using AI
3. Identifying required CACI forms from LA CIV 244 submissions
4. Generating properly formatted Word documents with filled placeholders

## Project Structure

### Core Files

#### `web_application.py`
**Main Flask web application**
- Provides a web interface for uploading legal documents
- Handles file uploads (LA CIV 244, case details PDFs, CACI templates)
- Orchestrates the document generation process
- Includes debug mode and response logging features
- **Key Features:**
 - Bootstrap-styled web interface
 - File upload handling for multiple document types
 - Integration with Gemini AI API
 - Error handling and debug logging

#### `single_form_processor.py`
**Single CACI form processor**
- Processes individual CACI forms (specifically CACI 101 - Overview of Trial)
- Analyzes Word document templates to identify placeholders
- Uses Gemini AI to extract case information from PDFs
- Generates JSON representations of filled forms
- Converts JSON back to formatted Word documents
- **Key Functions:**
 - `analyze_template()` - Extracts template structure and placeholders
 - `generate_content()` - Uses AI to fill form placeholders
 - `json_to_docx()` - Converts structured data back to Word format

#### `multi_form_processor.py`
**Multiple CACI forms processor**
- Enhanced version that handles multiple CACI forms simultaneously
- Identifies all required forms from LA CIV 244 submissions
- Generates a single combined document with all forms
- Includes page breaks and proper formatting between forms
- **Key Features:**
 - Batch processing of multiple forms
 - Form identification from LA CIV 244 documents
 - Combined document generation with proper formatting

### Utility Files

#### `pdf_form_extractor.py`
**PDF form field extractor**
- Simple utility to extract form fields from PDF documents
- Uses PyPDF2 to identify fillable form fields
- Useful for debugging and understanding PDF structure

#### `vision_ocr_extractor.py`
**Google Vision API OCR processor**
- Extracts text from PDF documents using Google Cloud Vision API
- Converts PDF pages to images and performs OCR
- Handles multi-page documents
- **Note:** Currently configured with placeholder API key

#### `gemini_pdf_processor.py`
**Simple Gemini PDF processor**
- Basic script for processing PDFs with Gemini AI
- Demonstrates direct PDF-to-AI processing
- Used for testing and simple document analysis

#### `text_to_docx_converter.py`
**Text to Word converter**
- Simple utility to convert plain text files to Word documents
- Basic conversion without formatting preservation

### Experimental/Incomplete Files

#### `rag_system.py`
**RAG (Retrieval Augmented Generation) system**
- Incomplete implementation of a document retrieval system
- Intended for chunking and embedding legal documents
- Uses LangChain for document processing
- **Status:** Incomplete/experimental

#### `web_application_alt.py`
**Alternative web application**
- Simplified version of the main web application
- Similar functionality to `app.py` but with different error handling
- May be used for testing or as a backup implementation


## Installation

### Requirements
```bash
pip install flask
pip install python-docx
pip install google-generativeai
pip install PyPDF2
pip install pdf2image
pip install requests
pip install langchain
pip install langchain-community
```

## API Keys Required

1. Google Gemini AI API key
2. Google Cloud Vision API key (for OCR functionality)

## Usage
Using the local version is recommended as it has been tested and shows best results. Website usage is still buggy and is discouraged. The limitations and upgrades needed are explained in further depth below.

Local Interface
- Change the file paths and API keys as mentioned in the code
  
Web Interface
1. Run the main application
 ```bash
python web_application.py
```
2. Open browser to http://localhost:5000
3. Upload required documents:
    LA CIV 244 PDF (to identify required forms)
    Case details PDF (UD 105 or similar)
    CACI template file (.txt format)
4. Generate Filled Forms

Fill in API Keys and File names wherever requested.


## File Processing Flow

1. **Document Upload**  
   → Legal documents are uploaded via web interface

2. **Form Identification**  
   → LA CIV 244 is analyzed to identify required CACI forms

3. **Case Analysis**  
   → Case details PDF is processed to extract relevant information

4. **Template Processing**  
   → CACI templates are analyzed for placeholders and formatting

5. **AI Generation**  
   → Gemini AI fills placeholders with extracted case information

6. **Document Generation**  
   → Filled forms are converted back to properly formatted Word documents

---

## Key Technologies

- **Flask** – Web framework for user interface  
- **python-docx** – Word document manipulation  
- **Google Gemini AI** – Document analysis and form filling  
- **PyPDF2** – PDF processing and form field extraction  
- **Bootstrap** – Frontend styling

---

## Current Limitations

- Hard-coded file paths in many scripts  
- API keys embedded in source code (should use environment variables)  
- Limited error handling in some components  
- Some experimental features are incomplete  
- Template format assumptions may not work for all CACI forms
- Usage: The web applications are currently functional but need significant updates before production use as they have the following limitations:
- Document Formatting Issues: The generated text from Gemini is returned in a JSON styling format but needs proper conversion to a fully styled Word document with correct paragraph formatting, fonts, and layout.
- Single Form Processing: The web interface currently processes only one hardcoded CACI form (CACI 101 - Overview of Trial) per request. 
---

## Suggested Improvements

### Configuration Management

- Move API keys to environment variables  
- Create configuration files for paths and settings

### Error Handling

- Implement comprehensive error handling  
- Add input validation for uploaded files

### Website Upgrades
- Automatically assess the LA CIV 244 document to identify all required forms
- Process multiple forms in a loop based on the checked/selected options
- Generate a complete document with all necessary CACI instructions


### Code Organization

- Create a proper package structure  
- Separate configuration, utilities, and core logic

### Testing

- Add unit tests for core functions  
- Create integration tests for the full workflow

### Documentation

- Add inline documentation for complex functions  
- Create user manual for the web interface
