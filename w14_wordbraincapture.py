from os import listdir
import skimage.io as sk
import numpy as np
import json
import itertools
import sys


def main():
    puzzle = listdir()
    puzzles = []
    for i in puzzle:
        if i.endswith('png') and i.startswith('train'):
            puzzles.append(i)
    puzzles = sorted(puzzles)
    dict3 = build_3_dict(puzzles)
    four_by_dictionary = buil_4_dict(puzzles)
    five_by_dict = build_5_dict(puzzles)
    for line in sys.stdin:
        line_input = str.strip(line)
        img = sk.imread(line_input, as_grey=True)  # 2
        size = find_grid_size(img)
        lengths = find_word_size(img, size)
        grid = find_letters_in_image(img, dict3,
                                     four_by_dictionary,
                                     five_by_dict)
        data = load_json(grid, size, lengths)
        jsonData = json.dumps(data)
        print(jsonData)


def find_letters_in_image(img, dict3,
                          four_by_dictionary,
                          five_by_dict):
    example_image = img
    example_tiles = chop_board(example_image, find_grid_size(example_image))
    dicionaries = [dict3,
                   four_by_dictionary,
                   five_by_dict]
    size = find_grid_size(example_image)-3
    letters = []
    columns = []
    for i in example_tiles:
        most_similar = 0
        for j in dicionaries[size]:
            similarity = letter_simularity(i, j[1])
            if similarity > most_similar:
                most_similar = similarity
                guessed_letter = j[0]
            else:
                pass
        letters.append(guessed_letter)
    if size == 0:
        for i in range(3):
            columns.append(letters[i]+letters[i+3]+letters[i+6])
    if size == 1:
        for i in range(4):
            columns.append(letters[i]+letters[i+4]+letters[i+8]+letters[i+12])
    if size == 2:
        for i in range(5):
            columns.append(letters[i]+letters[i+5] +
                           letters[i+10]+letters[i+15]+letters[i+20])
    else:
        pass
    return columns


def build_3_dict(puzzles):
    dict3 = 'E N R D B A I L S H S S I S O F K C F Y E S L L I C K J N '
    dict3 += 'F A E T A P L B X E A R O R B L H E E O O R S U A T J U A '
    dict3 += 'S S I R G N L M W O E L E L S D O H G L O V E'
    dict3 = dict3.lower().split()
    puzzles = sorted(puzzles)
    three_puzzles = puzzles[0:9]
    three_images = []
    three_tiles = []
    for i in three_puzzles:
        three_images.append(sk.imread(i, as_grey=True))
    for i in three_images:
        three_tiles.extend(chop_board(i, find_grid_size(i)))
    for j in range(len(three_tiles)):
        dict3[j] = (dict3[j],
                    three_tiles[j])
    return(dict3)


def buil_4_dict(puzzles):
    # build 4 letter dictionary
    four_by_dictionary = 'E A T I G A V E E E M A L G N R B T L E E X F F O '
    four_by_dictionary += 'I R E T A H S Y S O N E L N N H N C A O L A B E W '
    four_by_dictionary += 'C U O P I S C L M E A T K L U L L S N E B M O O R '
    four_by_dictionary += 'A D S L L T N Y T O P P U F O M M R I J E B T E N '
    four_by_dictionary += 'I T E L K N Z Z A R U P'
    four_by_dictionary = four_by_dictionary.lower().split()
    puzzles = sorted(puzzles)
    four_puzzles = puzzles[9:16]
    four_images = []
    four_tiles = []
    for i in four_puzzles:
        four_images.append(sk.imread(i, as_grey=True))
    for i in four_images:
        four_tiles.extend(chop_board(i, find_grid_size(i)))
    p = 0
    for j in range(len(four_tiles)):
        four_by_dictionary[j] = (four_by_dictionary[j],
                                 four_tiles[j])
    return (four_by_dictionary)


def build_5_dict(puzzles):
    # 5 letter dictionary
    letter_indices = [12, 20, 9, 28, 18, 24, 56, 4, 1, 331, 8,
                      27, 6, 17, 2, 22, 7, 0, 5, 38, 49, 50, 226]
    five_by_dict = 'A B C D E F G H I J K L M N O P R S T U V W Y'
    five_by_dict = five_by_dict.lower().split()
    puzzles = sorted(puzzles)
    five_puzzles = puzzles[16:]
    five_images = []
    five_tiles = []
    for i in five_puzzles:
        five_images.append(sk.imread(i, as_grey=True))
    for i in five_images:
        five_tiles.extend(chop_board(i, find_grid_size(i)))
    for j in range(len(letter_indices)):
        five_by_dict[j] = (five_by_dict[j],
                           five_tiles[letter_indices[j]])
    return five_by_dict


def find_grid_size(img):
    size_list = (img[570, 785], img[570, 660], img[570, 605])
    s = 0
    for i in size_list:
        if round(i) == 0.0:
            return(s+3)
        else:
            s += 1


def letter_simularity(A, B):
    return np.sum(A == B)/(B.size)


def chop_board(img, size):
    tiles = []
    img = img[525:1925, 325:1725]
    if size == 3:
        col_positions_3 = [38, 500, 963]
        row_positions_3 = [43, 506, 968]
        for i in col_positions_3:
            for j in row_positions_3:
                tiles.append(img[i:i+397, j:j+397])
        for i in range(len(tiles)):
            tiles[i] = tiles[i][110:290, 110:290]
    if size == 4:
        col_positions_4 = [36, 382, 729, 1077]
        row_positions_4 = [24, 371, 718, 1065]
        for i in col_positions_4:
            for j in row_positions_4:
                tiles.append(img[i:i+313, j:j+309])
        for i in range(len(tiles)):
            tiles[i] = tiles[i][90:215, 90:215]
    if size == 5:
        row_positions_5 = [19, 296, 574, 851, 1129]
        col_positions_5 = [32, 310, 587, 865, 1143]
        for i in col_positions_5:
            for j in row_positions_5:
                tiles.append(img[i:i+250, j:j+250])
        for i in range(len(tiles)):
            tiles[i] = tiles[i][75:175, 75:175]
    return tiles


def find_word_size(img, size):
    s = int(size)
    # 450 pixels, 450/2 = 225, 450/3 = 150, 450/4 = 112
    ##################################
    word_size = []
    if s == 3:
        pxl_row = 225
        word_size = find_words(img, pxl_row)
    elif s == 4:
        word_size_t = []
        for pxl_row in [150, 300]:
            temp_w = find_words(img, pxl_row)
            word_size_t.append(temp_w)
            word_size = list(itertools.chain.from_iterable(word_size_t))
    elif s == 5:
        word_size_2 = []
        word_size_3 = []
        word_size_t = []
        for pxl_row in [150, 300]:
            temp_w = find_words(img, pxl_row)
            word_size_2.append(temp_w)
        for pxl_row in [112, 224, 336]:
            temp_w = find_words(img, pxl_row)
            word_size_3.append(temp_w)
        if [-9999] in word_size_3:
            word_size_t = word_size_2
        else:
            word_size_t = word_size_3
        word_size = list(itertools.chain.from_iterable(word_size_t))
    else:
        word_size = [0]
    return word_size


def find_grid_size(img):
    size_list = (img[570, 785], img[570, 660], img[570, 605])
    s = 0
    for i in size_list:
        if round(i) == 0.0:
            return(s+3)
        else:
            s += 1
    return s


def find_words(img, pxl_row):
    img = (img[1950:2400])
    lines = 0
    word_size = []
    black = []
    loc = []
    for i in range(len(img[pxl_row])):
        if float(img[pxl_row][i]) <= 0.5376360784:
            black.append(1)
        else:
            loc.append(sum(black))
            loc.append(0)
            black = []
    loc2 = []
    count = 0
    if not loc or len(loc) < 3:
        return [-9999]
    words = []
    w = 0
    for j in loc:
        if j == 0:
            count += 1
        else:
            loc2.append(count)
            loc2.append(j)
            count = 0
    loc2.append(count)
    del loc2[0]
    del loc2[0]
    for k in loc2:
        if k <= (5):
            w += 1
        if k > (loc2[1]+10):
            if (w % 2 != 0):
                return [-8888]
            words.append(int(w/2))
            w = 0
    if (w % 2 != 0):
        return [-8888]
    words.append(int(w/2))
    return words


def load_json(grid, size, lengths):
    data = {}
    data['grid'] = grid
    data['size'] = size
    data['lengths'] = lengths
    return data

if __name__ == "__main__":
    main()
