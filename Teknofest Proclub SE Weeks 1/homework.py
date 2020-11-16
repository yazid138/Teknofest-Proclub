
def half_pyramid_pattern(rows):
    # print("""
    #     *
    #     * *
    #     * * *
    #     * * * *
    #     * * * * *
    # """)
    for x in range(1, rows + 1):
        for y in range(x):
            print("*", end=" ")
        print()

def half_pyramid_pattern_inverted(rows):
    # print("""
    #     * * *
    #     * *
    #     *
    # """)
    for x in range(1, rows + 1):
        for y in range(rows + 1, x, -1):
            print("*", end=" ")
        print()

def half_pyramid_pattern_mirrored(rows):
#     print("""
#          *
#        * *
#      * * *
#    * * * *
#     """)
    for x in range(1, rows + 1):
        for y in range(rows, x, -1):
            print(" ", end=" ")
        for z in range(x):
            print("*", end=" ")
        print()

def full_pyramid_pattern(rows):
#     print("""
#       *
#      * *
#     * * *
#    * * * *
#     """)
    for x in range(1, rows + 1):
        for y in range(rows, x, -1):
            print(end=" ")
        for z in range(x):
            print("*", end=" ")
        print()

def full_pyramid_pattern_inverted(rows):
    # print("""
    #     * * * * *
    #      * * * *
    #       * * *
    #        * *
    #         *
    # """)
    for x in range(1, rows + 1):
        for y in range(x - 1):
            print(end=" ")
        for z in range(rows + 1, x, -1):
            print("*", end=" ")
        print();


def print_pattern(pattern,row):
    if pattern == 1:
        half_pyramid_pattern(row)
    elif pattern == 2:
        half_pyramid_pattern_inverted(row)
    elif pattern == 3:
        half_pyramid_pattern_mirrored(row)
    elif pattern == 4:
        full_pyramid_pattern(row)
    elif pattern == 5:
        full_pyramid_pattern_inverted(row)
    else:
        print("Pola tidak ada!")


#¯\_(ツ)_/¯
def tampil_menu_segitiga():
    print('1.Half Pyramid Pattern')
    print('2.Half Pyramid Pattern Inverted')
    print('3.Half Pyramid Pattern Mirrored')
    print('4.Full Pyramid Pattern')
    print('5.Full Pyramid Inverted Pattern')


tampil_menu_segitiga()
pattern = int(input('Pilih jenis pattern \t: '))
row = int(input('Pilih banyak baris \t: '))
print('===============================')
print_pattern(pattern,row)
