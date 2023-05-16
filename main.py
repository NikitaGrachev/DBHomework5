import psycopg2

with psycopg2.connect(database="DBHomework5", user="postgres", password="postgres") as conn:
    with conn.cursor() as cur:
        # 1. Функция, создающая структуру БД (таблицы).
        # Правильно ли я понял, что в скобках после def create_table указал имя обьекта подключения к БД?
        # И первым значением во всех функциях будет именно conn?

        def create_table(conn):
            cur.execute("""
            CREATE TABLE IF NOT EXISTS Client(
                client_id SERIAL PRIMARY KEY,
                name VARCHAR(40) NOT NULL,
                surname VARCHAR(40) NOT NULL,
                email VARCHAR(40) NOT NULL
            );
            """)
            cur.execute("""
            CREATE TABLE IF NOT EXISTS Phone(
                phone_id SERIAL PRIMARY KEY,
                client_id INTEGER REFERENCES Client(client_id),
                phone CHAR(12)
            );
            """)
            return conn.commit()
        create_table(conn)
        pass

        # 2. Функция, позволяющая добавить нового клиента.
        # Функция прописана правильно, все данные добавились в таблицу, но при повторном нажатии пуска, когда я создал следующую функцию для телефонов,
        # он написал ошибку: File "C:\Development\Data_bases\DBHomework5\main.py", line 38, in <module>
        #     add_client(conn)
        #   File "C:\Development\Data_bases\DBHomework5\main.py", line 31, in add_client
        #     cur.execute("""
        # psycopg2.errors.UniqueViolation: ОШИБКА:  повторяющееся значение ключа нарушает ограничение уникальности "client_pkey"
        # DETAIL:  Ключ "(client_id)=(1)" уже существует.
        # при этом я через DBeaver проверил данные перебросились.

        def add_client(conn):
            # cur.execute("""
            # INSERT INTO Client(client_id, name, surname, email) VALUES(1, 'Петр', 'Романов', 'P1@mail.ru');
            # """)
            cur.execute("""
            INSERT INTO Client(client_id, name, surname, email) VALUES(2, 'Иван', 'Грозный', 'IG@mail.ru');
            """)
            return conn.commit()
        add_client(conn)
        pass

        # 3. Функция, позволяющая добавить телефон для существующего клиента.

        def add_phone(conn):
            # cur.execute("""
            # INSERT INTO Phone(phone_id, client_id, phone) VALUES(1, 1, '89997775533');
            # """)
            cur.execute("""
            INSERT INTO Phone(phone_id, client_id, phone) VALUES(2, 2, '89997775531');
            """)
            return conn.commit()
        add_phone(conn)
        pass

        # 4. Функция, позволяющая изменить данные о клиенте.
        # a) Прописал ниже 2 варианта функции. Оба пишут ошибку. В лекции это толком не проговаривалось.
        # b) При этом 2ая функция, где я меняю телефон работает, а с именем так не работает.
        # c) Написал 3ью функцию по подобию 2ой и все получилось. Нам на уроке объясняли только 1 вариант функции по подобию 1ого варианта.

        def update_client(conn):
            cur.execute("""
                UPDATE Cliant SET name=%s WHERE id=%s;
                """, ('Николай', client_id))
            return conn.commit()
        update_client(conn)
        pass

        def update_client(conn):
            cur.execute("""
                UPDATE Phone
                SET phone = 85
                WHERE phone_id = 2;
                """)
            return conn.commit()
        update_client(conn)

        def update_client(conn):
            cur.execute("""
                UPDATE Client
                SET name = 'Николай'
                WHERE client_id = 1;
                """)
            return conn.commit()
        update_client(conn)
        pass


        # 5. Функция, позволяющая удалить телефон для существующего клиента.

        def delete_phone(conn):
            cur.execute("""
                DELETE FROM Phone WHERE phone_id=%s;
                """, (2,))
            return conn.commit()
        delete_phone(conn)
        pass

        # 6. Функция, позволяющая удалить существующего клиента.

        def delete_client(conn):
            cur.execute("""
                DELETE FROM Client WHERE client_id=%s;
                """, (2,))
            return conn.commit()
        delete_client(conn)
        pass

        # 7. Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.
        # a) Прошу пояснить почему не получается функция на подобии той, что разбирали в лекции. Можно объяснить подробнее.

        def search_client(cursor, name: str) -> int:
            cursor.execute("""
                SELECT client_id FROM Client WHERE name=%s;
                """, (name,))
            return cur.fetchone()[0]

        search_cl = search_client(cur, 'Николай')
        print('client_id', client_id)

        # б) Здесь код проходит, но пишет ошибку:
        # print('client_id', client_id)
        # NameError: name 'client_id' is not defined
        # Прошу подсказать в чем ошибка и как ее исправить.

        def search_client(conn):
            cur.execute("""
                SELECT client_id FROM Client
                WHERE name=%s;
                """, ('Николай',))
            return cur.fetchone()[0]
        search_client(conn)
        print('client_id', client_id)








conn.close()