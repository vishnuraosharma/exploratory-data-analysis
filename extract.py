from bs4 import BeautifulSoup


def extract_text_from_html(html_file_path):
    result_list = []

    with open(html_file_path, 'r', encoding='utf-8') as html_file:
        print('hello')
        soup = BeautifulSoup(html_file, 'html.parser')
        # Find all <p> tags with the specified class
        target_paragraphs = soup.find_all('p', class_='sc-dnwKUv sc-kgKVFY sc-kWPZmv hOPFtS cBsaPK chOfXM')

        for p in target_paragraphs:
            # Extract the text within the <p> tag
            text = p.get_text(strip=True)
            result_list.append(text)


    return result_list


# Replace 'your_html_file.html' with the path to your HTML file
html_file_path = '/Users/vraosharma/Downloads/food nutrition dataset _ Kaggle.html'
parsed_text_list = extract_text_from_html(html_file_path)

# Print the extracted text as a comma-separated list
print(';;'.join(parsed_text_list))