import requests


# urls = ['https://oir.mobi/uploads/posts/2021-04/1619701495_42-oir_mobi-p-sonnii-kotik-zhivotnie-krasivo-foto-43.jpg',
#        'https://images.ast.ru/upload/resize_cache/content.constructor/3cf/480_480_2/img_1608045122_3762_843_scale_1200_1_.png',
#        'https://st.europaplus.ru/mf/p/236802/news/373/037400/content/4958e76b84a6ff53fbff9da9b922e260.jpg',
#        'https://cdn.iportal.ru/news/2015/99/preview/44da4b05194891d4830f8781b1c9557c009f5333_1200_800_c.jpg']

# for url in urls:
#     image_name = url.split('/')[-1]
#     response = requests.get(url=url)
#     with open(file=f'images/{image_name}', mode='wb') as file:
#         file.write(response.content)
#
#     with open(file='images/Name_of_kotiki.txt', mode='a', encoding='utf-8') as file:
#         file.write(f'{image_name}\n')

# url = 'https://replit.com/@AndrieiKravtsov?tab=status'
#
# response = requests.get(url=url)
# response = requests.post(url=url)
# print(response.status_code)

# with open(file='page.html', mode='w', encoding='utf-8') as file:
#     file.write(response.text)

# urls = {
#     'https://alloder.pro/uploads/monthly_2017_04/2.png.4dc1d9f253b0d8197a65827802149088.png': 'Paladin',
#     'https://alloder.pro/uploads/monthly_2017_04/8.png.02967e18b7a713d26e166bed334687cb.png': 'Mage',
#     'https://alloder.pro/uploads/monthly_2018_07/848466756_.jpg.a90f188363797ac617689dbd060c8433.jpg': 'Necromancer',
#     'https://alloder.pro/uploads/monthly_2017_04/4.png.69f11b0bd2f6b7cd297e4fbf536e2a85.png': 'Priest',
#     'https://alloder.pro/uploads/monthly_2017_04/6.png.e2074d83c7ebf34d977b77413e7043af.png': 'Archer',
#     'https://alloder.pro/uploads/monthly_2017_04/7.png.187e0009926b33d8dcc02b488b854d55.png': 'Shaman'
# }
#
#
# for url, file_name in urls.items():
#     image_name = file_name + '.' + url.split('.')[-1]
#     response = requests.get(url=url)
#     with open(file=f'Heroes/images/{image_name}', mode='wb') as file:
#         file.write(response.content)


# def plus_two_numbers(number1: int, number2: int) -> int:
#     result = number1 + number2
#     return result


# def main():
#     for index in range(1, 3):
#         input_file_name = f'input_data/{index}.txt'
#         with open(file=input_file_name, mode='r', encoding='utf-8') as file:
#             file_content = file.read()
#             input_number1 = int(file_content.split('\n')[0])
#             input_number2 = int(file_content.split('\n')[1])
#             result = plus_two_numbers(number1=input_number1, number2=input_number2)
#             print(f'На входных данных из файла {input_file_name}: {result}')
#
#
# if __name__ == '__main__':
#     main()


# def custom_filter(any_string: str) -> str:
#     result = str()
#     for symbol in any_string:
#         if symbol.isdigit():
#             symbol = str(int(symbol) + 1)
#         result += symbol
#     return result


# def main():
#     with open(file='input_data/input.txt', mode='r', encoding='utf-8') as file:
#         content = file.read().split('\n\n')
#     counter = 0
#     for input_string in content:
#         counter += 1
#         result = custom_filter(input_string.strip())
#         with open(file='input_data/output.txt', mode='a', encoding='utf-8') as file_2:
#             file_2.write(f'{counter}. {result}\n')

# INPUT_MARKER = '<ВХОДНЫЕ ДАННЫЕ>:'
# OUTPUT_MARKER = '<РЕЗУЛЬТАТ>:'
#
#
# def get_modified_data(content_list: list) -> list:
#     result = list()
#     for element in content_list:
#         element = element.split('\n')[0]
#         element = element.replace(INPUT_MARKER, '')
#         element = element.strip()
#         output_data = custom_filter(element)
#         sub_result = {
#             'input_data': element,
#             'output_data': output_data
#         }
#         result.append(sub_result)
#     return result
#
#
# def generate_output_string(result_list: list) -> str:
#     result_string = str()
#     for element in result_list:
#         sub_result_string = f'{INPUT_MARKER} {element["input_data"]}\n{OUTPUT_MARKER} {element["output_data"]}'
#         result_string = f'{result_string}\n\n{sub_result_string}'
#     result_string = result_string.strip()
#     return result_string
#
#
# def main():
#     with open(file='input_data/input.txt', mode='r', encoding='utf-8') as file:
#         content = file.read()
#         content_list = content.split('\n\n')
#         print(content_list)
#
#     result = get_modified_data(content_list=content_list)
#     output_value = generate_output_string(result_list=result)
#
#     with open(file='input_data/input.txt', mode='w', encoding='utf-8') as file:
#         file.write(output_value)
#
#
# if __name__ == '__main__':
#     main()

# def get_input_data(file_name: str) -> dict:
#     with open(file=f'input_data/{file_name}', mode='r', encoding='utf-8') as file:
#         content = file.read()
#     content_list = content.split('\n')
#     key = content_list[0].split('=')[-1].strip()
#     input_string = content_list[1].split('=')[-1].strip()
#     return {'key': int(key),'input_string': input_string}
#
#
# def encode_input_data(key: int, input_string: str) -> str:
#     result = str()
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
#     for symbol in input_string:
#         if symbol.lower() not in alphabet:
#             result += symbol
#             continue
#
#         if symbol.isupper():
#             alphabet = alphabet.upper()
#         else:
#             alphabet = alphabet.lower()
#
#         index = alphabet.index(symbol)
#         index = (index + key) % len(alphabet)
#         result += alphabet[index]
#
#     return result
#
#
# def write_to_file(file_name: str, result: str) -> None:
#     with open(file=f'input_data/{file_name}', mode='a', encoding='utf-8') as file:
#         file.write(f' {result}')
#
#
# def main():
#     input_data = get_input_data(file_name='input.txt')
#     key = input_data['key']
#     input_string = input_data['input_string']
#     result = encode_input_data(key=key, input_string=input_string)
#     write_to_file(file_name='input.txt', result=result)
#
#
# if __name__ == '__main__':
#     main()




