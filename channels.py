from pathlib import Path
from collections import defaultdict

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

def removeChannelHeaders():
    for f in Path(".").glob("CH_*.h"):
        f.unlink()

def generateChannelHeaders():
    channels = defaultdict(lambda: {"send": [], "recv": []})

    for file, ch in send.items():
        channels[ch]["send"].append(file)

    for file, ch in recv.items():
        channels[ch]["recv"].append(file)

    for ch, data in channels.items():
        header = Path(f"CH_{ch}.h")
        with open(header, "w") as h:
            h.write(f"#ifndef CH_{ch}_H\n")
            h.write(f"#define CH_{ch}_H\n\n")

            h.write(f"#endif // CH_{ch}_H\n\n")



def main():
    listFiles()
    bindChannels()
    print("SEND FILES:")
    print(send)
    print("RECV FILES:")
    print(recv)
    removeChannelHeaders()
    generateChannelHeaders()


main()
