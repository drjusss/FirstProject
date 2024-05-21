KEY_MARKER = '<k> = '
USER_STRING_MARKER = '<user_string> = '
ENCODING_STRING_MARKER = '<encoding_string> = '
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def get_input_data(file_name: str) -> list:
    with open(file=f'input_data/{file_name}', mode='r', encoding='utf-8') as file:
        content = file.read()

    content_list = content.strip().split('\n\n')
    result = list()

    for element in content_list:
        element = element.split('\n')
        key = int(element[0].replace(KEY_MARKER, '').strip())
        user_string = element[1].replace(USER_STRING_MARKER, '').strip()
        input_dict = {
            'key': key,
            'user_string': user_string
        }
        result.append(input_dict)

    return result


def encode_data(key: int, user_string: str) -> str:
    result = str()

    for symbol in user_string:
        if symbol.lower() not in ALPHABET:
            result += symbol
            continue

        if symbol.isupper():
            alphabet = ALPHABET.upper()
        else:
            alphabet = ALPHABET.lower()

        alphabet_index = alphabet.index(symbol)
        alphabet_index = (alphabet_index + key) % len(alphabet)
        result += alphabet[alphabet_index]

    return result


def get_output_data(input_data: list) -> str:
    result = str()

    for element in input_data:
        key = element['key']
        user_string = element['user_string']
        encoding_string = encode_data(key=key, user_string=user_string)
        sub_result = f'{KEY_MARKER}{key}\n{USER_STRING_MARKER}{user_string}\n{ENCODING_STRING_MARKER}{encoding_string}\n\n'
        result += sub_result
    return result


def write_to_file(file_name: str, result: str) -> None:
    with open(file=f'input_data/{file_name}', mode='w', encoding='utf-8') as file:
        file.write(result)


def main():
    input_data = get_input_data(file_name='input.txt')
    result = get_output_data(input_data=input_data)
    write_to_file(file_name='input.txt', result=result)


if __name__ == '__main__':
    main()
