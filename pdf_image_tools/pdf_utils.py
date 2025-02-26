from pathlib import Path
from typing import Optional
import pymupdf


def pdf_splitter(
    pdf_path: str | Path,
    images_folder: str | Path = "images",
    zoom_x: float = 2.0,
    zoom_y: float = 2.0,
) -> Optional[str]:
    """Конвертирует страницы PDF в изображения и сохраняет их в указанную папку.

    Args:
        pdf_path (str или Path): Путь к PDF-файлу.
        images_folder (str или Path): Папка для сохранения изображений.
        zoom_x (float): Коэффициент масштабирования по горизонтали. По умолчанию 2.0.
        zoom_y (float): Коэффициент масштабирования по вертикали. По умолчанию 2.0.

    Returns:
        Optional[str]: Сообщение об успешном завершении или None в случае ошибки.
    """
    try:
        print(f"------Обработка PDF-файла: {pdf_path}------")

        # Создание путей
        pdf_path = Path(pdf_path)
        images_folder = Path(images_folder)

        # Чтение PDF-документа
        doc = pymupdf.open(pdf_path)
        doc_len = len(doc)

        # Создание папки для сохранения изображений, если она не существует
        images_folder.mkdir(parents=True, exist_ok=True)

        # Матрица для масштабирования
        mat = pymupdf.Matrix(zoom_x, zoom_y)

        # Конвертация каждой страницы в изображение
        for page in doc:
            pix = page.get_pixmap(
                matrix=mat
            )  # Использование масштабирования matrix=mat
            output_path = images_folder / f"{pdf_path.stem}_{page.number + 1}.png"
            pix.save(output_path)

        doc.close()

        # Проверка количества обработанных страниц
        images_list = [file.name for file in images_folder.iterdir() if file.is_file()]
        images_count = len(images_list)
        if images_count != doc_len:
            raise ValueError(
                f"Ожидаемое количество изображений: {doc_len}. Получено: {images_count}"
            )
        return f"Успешно обработано страниц: {images_count} из {doc_len}"

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def pdf_merger(
    pdf_path: str | Path, images_folder: str | Path = "images"
) -> Optional[str]:
    """Конвертирует изображения из указанной папки в PDF-файл.

    Args:
        pdf_path (str или Path): Путь для сохранения результирующего PDF-файла.
        images_folder (str или Path): Папка, содержащая изображения для конвертации.

    Returns:
        Optional[str]: Сообщение об успешном завершении или None в случае ошибки.
    """
    try:
        print(f"------Обработка изображений: /{images_folder}------")

        # Создание путей
        images_folder = Path(images_folder)
        images_list = [file.name for file in images_folder.iterdir() if file.is_file()]
        images_count = len(images_list)

        # Создание пустого PDF-документа
        doc = pymupdf.open()

        # Добавление изображений в PDF-документ
        for item in images_list:
            # Открытие изображения и его конвертация в PDF
            img = pymupdf.open(images_folder / item)
            rect = img[0].rect
            pdfbytes = img.convert_to_pdf()
            img.close()

            # Добавление страницы в PDF-документ
            img_pdf = pymupdf.open("pdf", pdfbytes)
            page = doc.new_page(width=rect.width, height=rect.height)
            page.show_pdf_page(rect, img_pdf, 0)

        doc_len = len(doc)

        # Сохранение PDF-документа
        doc.save(pdf_path)
        doc.close()

        return f"Успешно обработано изображений: {images_count} из {doc_len}"

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None
