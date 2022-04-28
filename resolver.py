import base64

banner = """

 __  __     ______     __   __     ______     __   __    
/\ \/ /    /\  __ \   /\ "-.\ \   /\  __ \   /\ "-.\ \   
\ \  _"-.  \ \ \/\ \  \ \ \-.  \  \ \  __ \  \ \ \-.  \  
 \ \_\ \_\  \ \_____\  \ \_\\"\_\  \ \_\ \_\  \ \_\\"\_\ 
  \/_/\/_/   \/_____/   \/_/ \/_/   \/_/\/_/   \/_/ \/_/ 
                                                         


"""
print(banner)

class colors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def clean_string(string):
    string = string.replace("Encoding.UTF8.GetString(Convert.FromBase64String(", "")
    string = string.replace("\"))", "\"")
    return string

def Getbase(string):
    return string[find_nth(string, "\"", 1)+1:find_nth(string, "\"", 2)]

def decodeshitz(x):
    try:
        base64_bytes = x.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode('ascII')
        return sample_string
    except Exception as e:
        return "Couldnt decode Bytes to String"

def TwoOrMore(x,n=2):
    clean = clean_string(x)
    k=1
    for i in range(1,n):
        ss = x[find_nth(x, "\"", k)+1:find_nth(x,"\"",i+1)]
        k+=2
        clean = clean.replace(ss, decodeshitz(ss))
    return (clean)

def HasSlash(x):
    for i in range(len(x)):
        if x[i] == "\\":
            return True
    return False


x= 0

filename = input(colors.HEADER+"[-] Enter Your File Name (ex: file.txt) :")
print(colors.HEADER+"[+] Reading file...")
inputfile = open(filename, "r")
output = open("./output.txt", "w")
backslash = input(colors.HEADER+"[-] Wanna Relove \\ Y/N ?")
for line in inputfile.readlines():
    x+=1
    index = line.find("Encoding.UTF8.GetString")
    if "// Token:" in line:
            pass
    elif index != -1:
        if line.count("Encoding.UTF8.GetString") > 1:
            print("[*] Line : "+str(x))
            ch = TwoOrMore(line, line.count("Encoding.UTF8.GetString"))
            if backslash.upper() == "Y"and HasSlash(ch) and ch.find("OpenSubKey"):
                 ch = ch.replace("\\","\\\\")
            output.write(ch)
        else:
            print("[+] Line : "+str(x))
            GetBase64 = Getbase(clean_string(line))
            if GetBase64 != "":
                decoded = decodeshitz(GetBase64)
                ch = (line[:index] + '"' + decoded + '"')
                line = line.replace("\"))", "\"")
                ch += line[line.find(GetBase64)+len(GetBase64)+1:]

                if backslash == "Yes"and HasSlash(ch) and ch.find("OpenSubKey"):
                 ch = ch.replace("\\","\\\\")
                output.write(ch)
            elif GetBase64 == "":
                    output.write("")
            if ch[-1] != ";":
                ch = ch + ";"      
    else:
        output.write(line)
    

print(colors.HEADER +"[+] Reading file...")
print(colors.OKGREEN +"[+] Decoding base64...")
print(colors.OKGREEN +"[+] Writing to file...")
print(colors.OKGREEN + "[+] Done!")
inputfile.close()
output.close()
        


