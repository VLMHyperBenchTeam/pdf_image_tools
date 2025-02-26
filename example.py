from pdf_image_tools.pdf_utils import pdf_splitter, pdf_merger


if __name__ == "__main__":

    # Определение путей
    input_pdf_path = "test.pdf"
    output_pdf_path = "output_test.pdf"

    # Разделение PDF-файла на изображения
    split_result = pdf_splitter(input_pdf_path, zoom_x=2.0, zoom_y=2.0)
    if split_result:
        print(split_result)

    # Сборка PDF-файла из изображений
    merge_result = pdf_merger(output_pdf_path)
    if merge_result:
        print(merge_result)
