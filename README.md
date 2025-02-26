# PDF Image Tools

`pdf_image_tools` — это Python-пакет для работы с PDF, состояющим из изображений. Он позволяет:
- Разделять PDF-файлы на изображения (по одной странице на изображение).
- Объединять изображения в один PDF-файл.

---

## Установка

Для установки пакета выполните следующую команду:

```bash
poetry add git+https://github.com/VLMHyperBenchTeam/pdf_image_tools.git@0.1.0
```

Или добавьте вручную в `pyproject.toml`:

```
pdf-image-tools = {git = "https://github.com/VLMHyperBenchTeam/pdf_image_tools.git", rev = "0.1.0"}
```

---

## Использование

### 1. Разделение PDF на изображения

Функция `pdf_splitter` конвертирует каждую страницу PDF в отдельное изображение и сохраняет их в указанную папку.

```python
from pdf_image_tools.pdf_utils import pdf_splitter

# Разделение PDF на изображения
result = pdf_splitter("example.pdf", zoom_x=2.0, zoom_y=2.0)
if result:
    print(result)  # Успешно обработано страниц: 5 из 5
```

#### Параметры для управления качеством изображений:
- `zoom_x` (float): Коэффициент масштабирования по горизонтали. По умолчанию: `2.0`.
- `zoom_y` (float): Коэффициент масштабирования по вертикали. По умолчанию: `2.0`.

---

### 2. Объединение изображений в PDF

Функция `pdf_merger` объединяет изображения из указанной папки в один PDF-файл.

```python
from pdf_image_tools.pdf_utils import pdf_merger

# Объединение изображений в PDF
result = pdf_merger("output.pdf")
if result:
    print(result)  # Успешно обработано изображений: 5 из 5
```

Пример работы скрипта доступен в файле `example.py`.
