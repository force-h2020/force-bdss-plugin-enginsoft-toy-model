from FileReaderWriter import FileReaderWriter

rw = FileReaderWriter("data.txt")
print(rw.getData())

d = dict()
d["force.Y"] = 80.252
d["force.X"] = 20.4242

rw.writeData(d)