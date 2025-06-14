from PyPDF2 import PdfReader

reader = PdfReader("LA CIV PDF")

fields = reader.get_fields()

if fields:
    for field_name, field in fields.items():
        print(f"{field_name}: {field}")
else:
    print("No form fields found.")
