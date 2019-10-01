import base64
import hashlib

dest_str = "fR4aHWwuFCYYVydFRxMqHhhCKBseH1dbFygrRxIWJ1UYFhotFjA="
dest_str_1 = base64.b64decode(dest_str)
def do_it():
    key = hashlib.md5('ISCC'.encode()).hexdigest()
    x = 0
    chart = ""
    result = ""
    result_2 = ""
    for index in range(0, len(dest_str_1)):
        if x == len(key):
            x = 0
        chart += key[x]
        x += 1
        index += 1
    print(chart)
    for index in range(0, len(dest_str_1)):
        print(dest_str_1[index])
        result += chr((dest_str_1[index]+128) - ord(chart[index]))
        # result_2 += chr((dest_str_1[index]) - ord(chart[index]))
    print("result 1 : {0}".format(result))
    print("result 1 : {0}".format(result_2))


if __name__ == "__main__":
    do_it()