# Create file with content
with open('data/my.data', 'wb') as f:
    f.write(b'ABCDEF')

# Read contecnt from file based on current index position
with open('data/my.data', 'rb') as f:
    print(f.read(5).decode())
    f.seek(-3,1)
    print(f.read(1).decode())
