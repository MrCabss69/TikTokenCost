import os 

def extract_folder_texts(folder_path):
    all_texts = ''
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                all_texts += file.read() + ' '
    return all_texts.strip() 