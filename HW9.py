import bs4
import urllib.request
import re
def url_to_soup(url):
    try:
        with urllib.request.urlopen(url) as url_file:
            bytes = url_file.read()
    except urllib.error.URLError as url_err:
        print(f'Error opening url: {url} \n {url_err}')
    else:
        soup = bs4.BeautifulSoup(bytes, 'html.parser')
        return soup
def get_links(soup):
    list = []
    table = soup('table')[2]
    for each_anchor in table('a'):
        href = each_anchor.get('href',None)
        if href:
            list.append(href)
    return list
def get_info(soup):
    dictionary = {}
    table = soup('table')[2]
    regex = re.compile(r"\s*CS (046A|046B|047|049C|049J)\s*")
    all_courses = table.find_all('td',string=regex)
    school = table('td')[2].get_text()
    for each_course in all_courses:
        next_column = each_course.find_next_sibling('td').find_next_sibling('td')
        articulation = next_column.get_text(separator=' ')
        if(articulation != "No Current Equivalent"):
            dictionary[re.match(regex,each_course.get_text()).group().strip()] = ' '.join(articulation.split()) + ' at ' + school.title()
    return dictionary
def loop_links(links):
    total = {
    'CS 046A': [],
    'CS 046B': [],
    'CS 047': [],
    'CS 049C': [],
    'CS 049J': []
    }
    for link in links:
        absolute = urllib.parse.urljoin("http://info.sjsu.edu",link)
        newSoup = url_to_soup(absolute)
        dict = get_info(newSoup)
        for key in dict:
            total[key].append(dict[key])
    return total
def write_to_file(final_dictionary):
    with open('articulations.txt', 'a',encoding='utf-8') as output_file:
        for key in final_dictionary:
            for value in final_dictionary[key]:
                output_file.write(f'{key}: {value}\n')
def main():
    soup = url_to_soup("http://info.sjsu.edu/web-dbgen/artic/all-course-to-course.html")
    links = get_links(soup)
    dict_to_write = loop_links(links)
    write_to_file(dict_to_write)

if __name__ == "__main__":
    main()