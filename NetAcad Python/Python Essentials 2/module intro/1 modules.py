import example_module
import sys

for p in sys.path:
    print(p)

print(type(sys.path))