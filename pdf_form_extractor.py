from PyPDF2 import PdfReader

reader = PdfReader("/Users/thevedantsingh/Desktop/SLS/LACIV244 - Breach of Covenant LAFLA.pdf")

fields = reader.get_fields()

if fields:
    for field_name, field in fields.items():
        print(f"{field_name}: {field}")
else:
    print("No form fields found.")
