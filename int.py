from docx import Document

# Read content from txt file
with open("output.txt", "r", encoding="utf-8") as txt_file:
    content = txt_file.read()

# Create a Word document
doc = Document()
doc.add_paragraph(content)

# Save as .docx
doc.save("example.docx")
