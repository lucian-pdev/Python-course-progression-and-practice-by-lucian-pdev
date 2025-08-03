from os import strerror
import password_generator

try:
    file = open('generated_passwords.txt', 'wt' )
    for l in range(10):
        newline = f"line #{str(l + 1)}: {password_generator.main(14)}\n"
        file.write(newline)
    file.close()
except IOError as e:
    print(f'I/O Error:', strerror(e.errno))