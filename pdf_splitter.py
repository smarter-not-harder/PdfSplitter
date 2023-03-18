import PyPDF2

# Open the PDF file in read-binary mode
with open("ai_2_2.pdf", 'rb') as f:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(f)

    # Calculate the total number of pages
    num_pages = len(pdf_reader.pages)

    # Calculate the number of pages for each half
    half_num_pages = num_pages // 2

    # Create a PDF writer object for the first half
    pdf_writer1 = PyPDF2.PdfWriter()

    # Add pages to the first PDF writer object
    for page_num in range(half_num_pages):
        page_obj = pdf_reader.pages[page_num]
        pdf_writer1.add_page(page_obj)

    # Write the first half to a new PDF file
    with open('your_file_half1.pdf', 'wb') as f:
        pdf_writer1.write(f)

    # Create a PDF writer object for the second half
    pdf_writer2 = PyPDF2.PdfWriter()

    # Add pages to the second PDF writer object
    for page_num in range(half_num_pages, num_pages):
        page_obj = page_obj = pdf_reader.pages[page_num]
        pdf_writer2.add_page(page_obj)

    # Write the second half to a new PDF file
    with open('your_file_half2.pdf', 'wb') as f:
        pdf_writer2.write(f)
