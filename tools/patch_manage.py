import sys

patch_content='''
    # Special PythonAnywhere check to mention not to use runserver
    pythonanywhere = os.getenv('PYTHONANYWHERE_DOMAIN')
    if pythonanywhere is not None and 'runserver' in sys.argv : 
        print('')
        print('*********')
        print('You should not use "runserver" on PythonAnywhere - use ')
        print('   python manage.py check')
        print('and reload your application under the Web tab or in the file editor')
        print('*********')
        quit()
    # End of PythonAnywhere check
'''.split("\n")

if len(sys.argv) < 2:
    print('Please specify the file name as a parameter')
    quit()

try:
    with open(sys.argv[1]) as file_object:
        text = file_object.read()
        lines = text.split("\n")
except:
    print("Could not read input file:", sys.argv[1])
    quit()

for line in lines:
    if "pythonanywhere" in line.lower():
        # print('File already patched..')
        quit()

output = list()
patched = False
for line in lines:
    if not patched and ('def main():' == line or 'if __name__ == "__main__":' == line) :
        output.append(line)
        patched = True
        for new in patch_content:
            output.append(new)
        continue
    output.append(line)

with open(sys.argv[1], 'w') as f:
    for line in output:
        f.write(f"{line}\n")

print('Patched file:', sys.argv[1])

