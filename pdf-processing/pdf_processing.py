import PyPDF2


"""
 Author: {Abhishek Borse}
 Email:  {abhishek.borse10@gmail.com}
 Github: {https://github.com/abhishekborse/text-processing}
 LinkedIn: {https://www.linkedin.com/in/abhishekborse}
"""


class PdfProcessing:

    def __init__(self):
        pass

    @staticmethod
    def extract_text_from_pdf(source_file_path):
        """
        :param source_file_path: absolute file path with extension
        :return: page-wise dictionary of text data
        """
        pdf_file = open(source_file_path, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        total_pages = pdf_reader.numPages
        text_by_page_number = {}
        for pg_no in range(0, total_pages):
            page_obj = pdf_reader.getPage(pg_no)
            text = page_obj.extractText()
            text_by_page_number.update({pg_no: text})
        return text_by_page_number

    @staticmethod
    def decrypt_pdf(source_file_path, pdf_password):
        """
        :param source_file_path: absolute file path with extension
        :param pdf_password: password string
        :return: void
        """
        pdf_file = open(source_file_path, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        is_encrypted = pdf_reader.isEncrypted
        text_by_page_number = {}
        if not is_encrypted:
            text_by_page_number.update({'status': False, 'message': 'File Not Encrypted'})
            print(text_by_page_number)
            return text_by_page_number
        pdf_reader.decrypt(pdf_password)
        total_pages = pdf_reader.numPages
        pdf_writer = PyPDF2.PdfFileWriter()
        for page_num in range(total_pages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))
        new_file_name = 'decrypted_{}'.format(source_file_path.split('/')[-1])
        output_file = open('./data/{}'.format(new_file_name), 'wb')
        pdf_writer.write(output_file)
        output_file.close()

    @staticmethod
    def encrypt_pdf(source_file_path, file_password):
        """
        :param source_file_path: absolute file path with extension
        :param file_password: password string
        :return: void
        """
        pdf_file = open(source_file_path, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        is_encrypted = pdf_reader.isEncrypted
        total_pages = pdf_reader.numPages
        text_by_page_number = {}
        if is_encrypted:
            text_by_page_number.update({'status': False, 'message': 'File Already Encrypted'})
            print(text_by_page_number)
            return text_by_page_number
        pdf_writer = PyPDF2.PdfFileWriter()
        for page_num in range(total_pages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))
        pdf_writer.encrypt(file_password)
        new_file_name = 'encrypted_{}'.format(source_file_path.split('/')[-1])
        output_file = open('./data/{}'.format(new_file_name), 'wb')
        pdf_writer.write(output_file)
        output_file.close()

    @staticmethod
    def copy_pdf(source_file_path, new_file_name=None):
        """
        :param source_file_path: absolute file path with extension
        :param new_file_name: absolute file path with extension for new file to be generate
        :return: void
        """
        source_file = open(source_file_path, 'rb')

        source_pdf_reader = PyPDF2.PdfFileReader(source_file)

        pdf_writer = PyPDF2.PdfFileWriter()

        for page_num in range(source_pdf_reader.numPages):
            page_obj = source_pdf_reader.getPage(page_num)
            pdf_writer.addPage(page_obj)
        if not new_file_name:
            new_file_name = 'copy_{}'.format(source_file_path.split('/')[-1])
        output_pdf_file = open('./data/{}'.format(new_file_name), 'wb')
        pdf_writer.write(output_pdf_file)
        output_pdf_file.close()

    @staticmethod
    def rotate_pdf_file(source_file_path, page_number=0, rotate_degree=90):
        """
        :param source_file_path: absolute file path with extension
        :param page_number: if NOT 0 then rotate specific page otherwise full document
        :param rotate_degree: multiple of 90 in integer
        :return: void
        """

        minutes_file = open(source_file_path, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(minutes_file)
        pdf_writer = PyPDF2.PdfFileWriter()

        if page_number:
            page = pdf_reader.getPage(page_number - 1)
            page.rotateClockwise(rotate_degree)
            pdf_writer.addPage(page)
        else:
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                page.rotateClockwise(rotate_degree)
                pdf_writer.addPage(page)
        file_name = source_file_path.split('/')[-1]
        result_pdf_file = open('./data/rotate_{}_{}'.format(rotate_degree, file_name), 'wb')
        pdf_writer.write(result_pdf_file)
        result_pdf_file.close()
        minutes_file.close()
