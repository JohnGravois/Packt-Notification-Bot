import requests
from bs4 import BeautifulSoup

def search():
  response = requests.get('https://www.packtpub.com/free-learning')
  content = response.content
  soup = BeautifulSoup(content, 'html.parser')
  book_name = str(soup.findAll('h3'))
  if len(book_name) > 0: 
    book_name = book_name[46:-6]
    print(book_name)
    spans = soup.findAll('span')
    authors = ""
    pub = ""
    pages = ""
    desc = ""
    image = ""
    for x in spans:
      if "By" in str(x) and len(authors) <= 0: 
        authors = str(x)[58:-8].translate({ ord("\n"): " " })
        print(authors)
      elif "Publication date: " in str(x) and len(pub) <= 0:
        pub = str(x)[6:-7]
        print(pub)
      elif "Pages: " in str(x) and len(pages) <= 0:
        pages = str(x)[6:-7]
        print(pages)
      elif len(str(x)) > 100:
        desc = str(x)[6:-7]
        print(desc)
    image = str(soup.findAll('img')[1]).split(" ")
    image = image[len(image)-1].split('"')[1]
    print(image)
  
    message = book_name + '\n' + authors + '\n' + pub + '\n' + pages + '\n' + desc + '\n' +'https://www.packtpub.com/free-learning'
    return message, image
  else:
    return "Could not establish a connection with PackT", ""