from libs import *
from config import bd_name

@dataclass
class Product:
    name: str
    link: str
    price: float

def create_bd():
    with sqlite3.connect(bd_name) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS source (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                link TEXT NOT NULL,
                price REAL NOT NULL
            )
        """)


def parse(url:str, max_item: int):
    page = 1
    count_items = 0
    create_bd()
    while max_item > count_items:
        list_product = []
        res = requests.get(f"{url}/{page}/")
        soup = BeautifulSoup(res.text, "lxml")
        products = soup.find_all("div", class_="catalog-item")
        for product in products:
            if count_items >= max_item:
                break
            count_items += 1
            name_product = product.find("div", class_ = "name")
            link = "https://elektronik-shop.ru" + name_product.find("a", itemprop = "url").get("href")
            name = name_product.find("span", class_= "text").text
            price = float("".join(product.find("span", class_= "value").text.split()))
            list_product.append(Product(name=name, link=link, price=price))
        insert_db(list_product)
        page += 1



def insert_db (products: list[Product]):
    with sqlite3.connect(bd_name) as connection:
        cursor = connection.cursor()
        for product in products:
            cursor.execute('INSERT INTO source (name, link, price) VALUES (?, ?, ?)', (product.name, product.link, product.price))
        connection.commit()

#Печатаем все строки в БД
def print_all():
    with sqlite3.connect(bd_name) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM source')
        answers = cursor.fetchall()
        for answer in answers:
          print(answer)

# Выбираем и сортируем холодильники по убыванию цены (Выводит id и цену)
def sort_in_descending_order():
    with sqlite3.connect(bd_name) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT id, price FROM source ORDER BY price DESC')
        results = cursor.fetchall()
        for row in results:
          print(row)

# Выбираем и сортируем холодильники по возрастанию цены (Выводит id и цену)
def sort_in_ascending_order():
    with sqlite3.connect(bd_name) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT id, price FROM source ORDER BY price ASC')
        results = cursor.fetchall()
        for row in results:
          print(row)

# Выбираем холодильники у которых цена больше n рублей (Выводит название и цену)
def the_output_is_more_than_price(min_price: int):
    with sqlite3.connect(bd_name) as connection:
        cursor = connection.cursor()
        cursor.execute('''                                                              
        SELECT name, price
        FROM source
        GROUP BY price
        HAVING AVG(price) > ?
        ORDER BY price DESC
        ''', (min_price,))
        results = cursor.fetchall()
        for row in results:
          print(row)


# Выбираем холодильники у которых цена меньше n рублей (Выводит название и цену)
def the_output_is_less_than_price(max_price: int):
    with sqlite3.connect(bd_name) as connection:
        cursor = connection.cursor()
        cursor.execute('''                                                              
        SELECT name, price
        FROM source
        GROUP BY price
        HAVING AVG(price) < ?
        ORDER BY price DESC
        ''', (max_price,))
        results = cursor.fetchall()
        for row in results:
          print(row)


