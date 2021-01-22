import sys
import os
import json

def celare_notebook(tokens):
    try:
        flag = False

        if os.path.exists(".tokens.json"):
            file = open(".tokens.json", "r")
            content = file.read()
            tokens = json.loads(content)
            
            for i in range(len(arguments)):
                if i%2 == 0:
                    tokens[arguments[i].upper()] = ""
                    key = arguments[i].upper()
                else:
                    tokens[key] = arguments[i]  
            file.close()

            file = open('.tokens.json', 'w')
            file.write(json.dumps(tokens))
            file.close()
        else:
            file = open('.tokens.json', 'w')
            file.write(json.dumps(tokens))
            file.close()

    except Exception as error:
        print("Something went wrong...", error)


def main():
    args = sys.argv

    try:
        flag = False
        tokens = dict()
        arguments = args[1:]

        if os.path.exists(".tokens.json") and len(arguments) > 0:
            file = open(".tokens.json", "r")
            content = file.read()
            tokens = json.loads(content)
            
            for i in range(len(arguments)):
                if i%2 == 0:
                    tokens[arguments[i].upper()] = ""
                    key = arguments[i].upper()
                else:
                    tokens[key] = arguments[i]  
            file.close()

            file = open('.tokens.json', 'w')
            file.write(json.dumps(tokens))
            file.close()
        elif len(arguments) > 0:
            for i in range(len(arguments)):
                if i%2 == 0:
                    tokens[arguments[i].upper()] = ""
                    key = arguments[i].upper()
                else:
                    tokens[key] = arguments[i]    

            file = open('.tokens.json', 'w')
            file.write(json.dumps(tokens))
            file.close()

    except Exception as error:
        print("Something went wrong...", error)

if __name__ == "__main__":
    main()
