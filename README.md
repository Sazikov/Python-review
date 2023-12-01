# Python-review
Реализованный функционал:
  1) Парсинг информации о холодильниках с сайта: https://elektronik-shop.ru/catalog/kholodilniki/?view=list&page_count=12&sort=shows&by=desc&PAGEN_1=
  2) Заполнение базы данных
  3) Возможность обрабатывать данные:
       а) Печатать все строки БД: Print_all()
       б) Сортировка холодильников по убыванию цены: Sort_in_descending_order()
       в) Сортировка холодильников по возрастанию цены: Sort_in_ascending_order()
       г) Выбирать холодильники ценой больше n рублей: The_output_is_more_than_price(n):
       д) Выбирать холодильники ценой меньше n рублей: The_output_is_less_than_price(n):
  4) Развертывание сервисов с помощью Docker и Docker-compose
  5) Запуск через build.sh

Нереализованный функционал:
  1) При пересборке проекта все данные теряются
  
