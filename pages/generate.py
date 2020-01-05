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

def get_links(folder):
    links_file = os.path.join(folder, 'links.txt')

    try:
        with open(links_file, 'r') as file:
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
        if filename.endswith(".png") or filename.endswith(".mp4"):
         html += "<div class='project-page-selector' onclick='selectorClick(this)'></div>"

    return html

def create_preloads_html(folder):
    media_folder = os.path.join(folder, 'media')
    html = ''

    for filename in os.listdir(media_folder):
         html += "<img src='media/" + filename + "' width='1' height='1' border='0'>"

    return html

def create_links_html(folder):
    link_pairs = get_links(folder)
    html = ''

    print(link_pairs)

    for link_pair in link_pairs:
        parts = link_pair.split(',')
        html += "<li><a href='" + parts[1] + "'>" + parts[0] + "</a></li>"

    return html

def count_media(folder):
    media_folder = os.path.join(folder, 'media')

    return len(os.listdir(media_folder))

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
        if filename.endswith(".png") or filename.endswith(".mp4"):
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
        page = page.replace('###PRELOADS###', create_preloads_html(filename))
        page = page.replace('###LINKS###', create_links_html(filename))

        if count_media(filename) > 1:
            page = page.replace('###OMIT_START###', '')
            page = page.replace('###OMIT_END###', '')
        else:
            page = page.replace('###OMIT_START###', '<!--')
            page = page.replace('###OMIT_END###', '-->')

        print(get_title(filename))
        write_page(filename, page);
        write_media_js(filename)
        
