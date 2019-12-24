import os

def get_title(folder):
    title_file = os.path.join(folder, 'title.txt')

    try:
        with open(title_file, 'r') as file:
            return file.read().replace('\n', '')
    except:
        return 'Title folder not present'

def get_text(folder):
    text_file = os.path.join(folder, 'text.txt')

    try:
        with open(text_file, 'r') as file:
            return file.read().split('\n')
    except:
        return []

def create_text_html(folder):
    text = get_text(folder)
    html = ''

    for paragraph in text:
        html += '<p>' + paragraph + '</p>'

    return html

def create_selectors_html(folder):
    media_folder = os.path.join(folder, 'media')
    html = ''

    for filename in os.listdir(media_folder):
         html += "<div class='project-page-selector' onclick='selectorClick(this)'></div>"

    return html

def open_template():
    with open('template.html', 'r') as file:
        return file.read();

def write_page(folder, html):
    filename = os.path.join(folder, folder + '.html');
    
    with open(filename, 'w') as file:
        file.write(html)

def write_media_js(folder):
    media_folder = os.path.join(folder, 'media')
    javascript = 'let media=['

    for filename in os.listdir(media_folder):
         javascript += "'" + 'media/' + filename + "',"

    javascript += ']'

    with open(os.path.join(folder, 'media.js'), 'w') as file:
        file.write(javascript)

template = open_template();

for filename in os.listdir():
    if os.path.isdir(filename):
        page = template;
        page = page.replace('###TITLE###', get_title(filename))
        page = page.replace('###TEXT###', create_text_html(filename))
        page = page.replace('###SELECTORS###', create_selectors_html(filename))

        print(get_title(filename))
        write_page(filename, page);
        write_media_js(filename)
        
