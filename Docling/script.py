import os
from docling.document_converter import DocumentConverter
from docx import Document

source = "your_file_path"

converter = DocumentConverter()

result = converter.convert(source)

markdown_content = result.document.export_to_text() # can use html, text, dict also

output_directory = "output_directory_path"
output_path = os.path.join(output_directory, "Converted_SOP_Filer.docx")

if not os.path.exists(output_directory):
    os.makedirs(output_directory)
  
doc = Document()
doc.add_paragraph(markdown_content)

doc.save(output_path)

print(f"Converted document saved as: {output_path}")
