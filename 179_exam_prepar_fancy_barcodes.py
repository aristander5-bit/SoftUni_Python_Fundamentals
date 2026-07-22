import re

def check_is_valid(barcode: str) -> str:
    pattern = "^@#+(.*)@#+$"
    # pattern = r"\b@#+(.*)@#+\b"
    barcode_match = re.search(pattern, barcode)
    if not barcode_match:
        return "Invalid barcode"
    found_barcode = barcode_match.group(1)
    if len(found_barcode) < 6:
        return "Invalid barcode"
    elif not found_barcode[0].isupper():
        return "Invalid barcode"
    elif not found_barcode.isalnum():
        return "Invalid barcode"
    elif not found_barcode[-1].isupper():
        return "Invalid barcode"

    product_group = ""
    for symbol in found_barcode:
        if symbol.isdigit():
            product_group += symbol
    if not product_group:
        product_group = "00"

    return f"Product group: {product_group}"

count_of_barcodes = int(input())

for some_barcode in range(count_of_barcodes):
    current_barcode = input()
    message = check_is_valid(current_barcode)

    print(message)
