from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["example.pdf","hello-world.pdf"]:
    merger.append(pdf)

merger.write("out-basic.pdf")
merger.close()

