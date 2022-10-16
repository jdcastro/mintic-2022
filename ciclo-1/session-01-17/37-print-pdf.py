from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

c = canvas.Canvas("hola-mundo.pdf", pagesize=letter)
for i in range(120):
    page_num = c.getPageNumber()
    text = "%s" % page_num
    c.drawString(286, 45, text)
    c.showPage()
c.save()
