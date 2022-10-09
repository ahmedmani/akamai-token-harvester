import frida, code, os, time




tokens = []


def message_handler(message, payload):
    token = message["payload"]
    if tokens:
        last_token = tokens[-1]
    else:
        last_token = ''

    if last_token != token:
        print(token)
        tokens.append(token)
        last_token = token


def save_to_file():
    fp = open(os.path.join(os.path.expanduser('~')) + "/Onedrive/Bureau/akamai_tokens.txt", "w+")
    for i in tokens:
        fp.write(f"\n{i}")
    fp.close()
        

device = frida.get_usb_device()
try:
    for i in range(100):
        try:
            pid = device.spawn(["com.mcdonalds.app"])
            device.resume(pid)
            time.sleep(1)
            session = device.attach(pid)
            with open("token_hook.js") as f:
                script = session.create_script(f.read())
            
            script.on("message", message_handler)  
            script.load()
            script.exports.get_token()
        except:
            code.interact(local=locals())
            continue
except:
    code.interact(local=locals())
    save_to_file()

save_to_file()

# code.interact(local=locals())