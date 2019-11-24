from PIL import Image, ImageColor


def gen_chess_board():
    cell_size = 100  # width == height
    img = Image.new("1", (cell_size * 8, cell_size * 8), 0)
    cell_img = Image.new("1", (cell_size, cell_size), 1)

    for y in range(0, 8 * cell_size, cell_size):
        for x in range(0, 8 * cell_size, cell_size):
            if y % (2 * cell_size) == 0 and x % (2 * cell_size) == 0:
                img.paste(cell_img, (x, y))
            elif y % (2 * cell_size) != 0 and x % (2 * cell_size) != 0:
                img.paste(cell_img, (x, y))

    img.save("test/chess_board.jpg")


def gen_rainbow(direction="horizontal"):
    if direction == "diagonal":
        size = 180  # 360 / 2
    else:
        size = 360
    img = Image.new("RGB", (size, size))
    data = img.load()

    for hue in range(0, 360):
        color = ImageColor.getrgb(f"hsl({hue}, 100%, 50%)")
        if direction == "horizontal":
            for y in range(0, 360):
                data[hue, y] = color
        elif direction == "vertical":
            for x in range(0, 360):
                data[x, hue] = color
        else:  # diagonal
            for n in range(0, hue):
                try:
                    data[n, hue - n] = color
                except IndexError:
                    pass

    img.save(f"test/rainbow_{direction}.jpg")


if __name__ == "__main__":
    gen_chess_board()
    gen_rainbow("horizontal")
    gen_rainbow("vertical")
    gen_rainbow("diagonal")