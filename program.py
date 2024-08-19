import marshal, sys, os

def clear():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

clear()

def obfuscate_code(source_file, output_file):
    with open(source_file, 'r', encoding='utf-8') as file:
        source_code = file.read()
    
    code_object = compile(source_code, source_file, 'exec')
    
    serialized_code = marshal.dumps(code_object)
    
    executable_script = f"""
import marshal as k
import sys
if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding('utf-8')
serialized_code = {repr(serialized_code)}
code_object = k.loads(serialized_code)
exec(code_object)
    """
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(executable_script)
    
    print(f"[*] Executable script generated as '{output_file}'")

if __name__ == "__main__":
    source_file = input("[*] Enter the name of the Python file to obfuscate: ")
    output_file = input("[*] Enter the name of the executable file to generate: ")
    
    if not os.path.isfile(source_file):
        print(f"[*] The file '{source_file}' does not exist")
        sys.exit(1)
    
    obfuscate_code(source_file, output_file)
