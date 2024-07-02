from docx import Document

text = input("Введите текст: ")

doc = Document()
doc.add_paragraph(text)

doc.save("output.docx")
