from bs4 import BeautifulSoup


with open("books.xml" , "r" , encoding="utf8") as book_file :
    books_xml = book_file.read() # File을 String으로 읽어오기
    

soup = BeautifulSoup(books_xml,"lxml") #lxml Parser를 사용해서 데이터 분석

for book_info in soup.find_all("author") :
    print(book_info)
    print(book_info.get_text())
    
    

with open("US08621662-20140107.XML" , "r" , encoding="utf8") as patent_xml :
    xml = patent_xml.read()
    
soup = BeautifulSoup(xml,"lxml")

invention_title_tag= soup.find("invention-title")
print(invention_title_tag.get_text())
    
publication_reference_tag = soup.find("publication-reference")

print(publication_reference_tag.get_text())