import pread
try:
    pixels = pread.schematic("./example.png")
    pread.xlsximport("./grid.xlsx", pixels, "./example.png"), print("Done!")
except: print("Something went wrong")