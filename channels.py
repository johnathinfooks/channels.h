from pathlib import Path

send = {}
recv = {}

def listFiles():
    cf = []
    directoryPath = Path(".")
    for f in directoryPath.glob("*.c"):
        cf.append(f.name)
    return cf

def bindChannels():
    for f in listFiles():
        with open(f, 'r') as file:
            content = file.read()
            if "@[SEND:" in content:
                start = content.index("@[SEND:") + len("@[SEND:")
                end = content.index("]", start)
                send[f] = int(content[start:end])
            elif "@[RECV:" in content:
                start = content.index("@[RECV:") + len("@[RECV:")
                end = content.index("]", start)
                recv[f] = int(content[start:end])


listFiles()
bindChannels()
print("SEND FILES:")
print(send)
print("RECV FILES:")
print(recv)
