#定義一個類別IO,有兩個屬性 supportedSrcs 和 read
class IO:
    supportedSrcs=["console","file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not Supported")
        else:
            print("read from",src)

#use類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")