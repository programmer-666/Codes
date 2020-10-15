import base64, sys
def main():
    a=base64.b64encode(sys.argv[1].encode('utf-8'))
    return str(a.decode())
print(main())
