import sqlite3


def create_table(database_filepath, table_name):  # 新建表
    conn = sqlite3.connect(database_filepath)
    cursor = conn.cursor()
    sql = "CREATE TABLE " + table_name + \
        "(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT, fragment TEXT)"
    cursor.execute(sql)
    cursor.close()
    conn.close()
    print('新建表完成！')


def search_table(database_filepath, table_name):  # 查询表
    conn = sqlite3.connect(database_filepath)
    cursor = conn.cursor()
    sql = "SELECT * FROM " + table_name
    results = cursor.execute(sql)
    results_all = results.fetchall()
    for r in results_all:
        print(r)
    cursor.close()
    conn.close()
    print('查询表完成！')


def search_data_by_id(database_filepath, table_name, search_id, search_data):  # 条件查询数据
    conn = sqlite3.connect(database_filepath)
    cursor = conn.cursor()
    sql = "SELECT * FROM " + table_name + " WHERE " + search_id + "=?"
    results = cursor.execute(sql, (search_data,))
    results_all = results.fetchall()
    if results_all:
        for r in results_all:
            print(r)
        print('查询数据完成！')
    else:
        print('该数据表中没有要查询的数据')
    cursor.close()
    conn.close()
    return


def insert_data(database_filepath, table_name, entry_name, entry_type="Keywords", entry_path="", entry_fragment=""):  # 插入数据
    conn = sqlite3.connect(database_filepath)
    cursor = conn.cursor()
    sql = "INSERT INTO " + table_name + \
        "(name, type, path, fragment) values (?,?,?,?)"
    cursor.execute(sql, (entry_name, entry_type, entry_path, entry_fragment))
    conn.commit()
    cursor.close()
    conn.close()
    print('插入数据 ("{0}", "{1}", "{2}", "{3}")！'.format(entry_name,
                                                      entry_type, entry_path, entry_fragment))


def delete_data_by_id(database_filepath, table_name, delete_id, delete_data):  # 删除数据
    conn = sqlite3.connect(database_filepath)
    cursor = conn.cursor()
    sql_find = "SELECT * FROM " + table_name + " WHERE " + delete_id + "=?"
    results = cursor.execute(sql_find, (delete_data,))
    results_all = results.fetchall()
    if results_all:
        sql = "DELETE FROM " + table_name + " WHERE " + delete_id + "=?"
        cursor.execute(sql, (delete_data,))
        conn.commit()
        print('删除数据完成！')
    else:
        print('该数据表中没有要查询的数据')
    cursor.close()
    conn.close()
    return


def update_data_by_id(database_filepath, table_name, search_id, search_data, update_id, update_data):  # 更新数据
    conn = sqlite3.connect(database_filepath)
    cursor = conn.cursor()
    sql_find = "SELECT * FROM " + table_name + " WHERE " + search_id + "=?"
    results = cursor.execute(sql_find, (search_data,))
    results_all = results.fetchall()
    if results_all:
        sql = "UPDATE " + table_name + " SET " + \
            update_id + "=? WHERE " + search_id + "=?"
        cursor.execute(sql, (update_data, search_data))
        conn.commit()
        print('更新数据完成！')
    else:
        print('该数据表中没有要更新的数据')
    cursor.close()
    conn.close()
    return


def find_data(database_filepath, table_name, search_id, search_data):  # 查找数据是否存在
    flag = False
    conn = sqlite3.connect(database_filepath)
    cursor = conn.cursor()
    sql_find = "SELECT * FROM " + table_name + " WHERE " + search_id + "=?"
    results = cursor.execute(sql_find, (search_data,))
    results_all = results.fetchall()
    if results_all:
        flag = True
    cursor.close()
    conn.close()
    return flag


if __name__ == '__main__':
    database_filepath = 'docSet.dsidx'
    table_name = 'searchIndex'
    search_id = 'type'
    search_data = 'Statement'

    # print('-'*20)
    # create_table(database_filepath, table_name)

    # print('-' * 20)
    # # TODO: sqlite3.OperationalError: cannot modify searchIndex because it is a view
    # insert_data(database_filepath, table_name, "InsertTest",
    #             "Statement", "path", "fragment")
    # insert_data(database_filepath, table_name, "InsertTest2",
    #             "Statement", "path2", "fragment2")

    print('-'*20)
    search_table(database_filepath, table_name)

    print('-'*20)
    # # search_data(database_filepath, table_name, search_date)
    search_data_by_id(database_filepath, table_name, search_id, search_data)

    # print('-'*20)
    # delete_data_by_id(database_filepath, table_name, "type", "Statement")

    # print('-'*20)
    # update_data_by_id(database_filepath, table_name, search_id,
    #                   search_data, "path", "更新path")
