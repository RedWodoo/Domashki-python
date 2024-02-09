"""
program
"""
import docx
text = input("Enter a sentence: ")
doc = docx.Document()
head = doc.add_heading(text)
doc.save("someshit.docx")
