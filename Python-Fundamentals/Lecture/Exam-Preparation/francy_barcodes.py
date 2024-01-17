import re

count_of_barcodes = int(input())
invalid_flag = False
for current_barcode in range(0, count_of_barcodes):
    barcode = input()
    if barcode.count('@#') == 2:
        pattern = r"@|#"
        content = ''.join(re.split(pattern, barcode))
        if len(content) >= 6:
            # print(f'content len => {len(content)}')
            if content[0].isupper():
                # print(f'{content[0]} => is upper')
                if content.isalnum():
                    # print(f'Yes content contain only num and alpha')
                    if content[-1].isupper():
                        # print(f"{content}")
                        pattern = r"[A-z]"
                        content_num = ''.join(re.split(pattern, content))
                        if content_num.isnumeric():
                            print(f"Product group: {content_num}")
                        else:
                            print(f"Product group: 00")
                        continue
    print("Invalid barcode")



