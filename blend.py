from PIL import Image, ImageDraw, ImageEnhance, ImageFont

folder = 'skins/rdtoi/imgs/'

# Sizes and Crops
song_list_size = 459, 127
main_image_size = 717, 349
button_legend_size = 608, 36
difficulty_size = 435, 100
difficulty_number_highlight_resize = 72, 62
difficulty_number_list_resize = 17, 10
difficulty_number_crop_box = 0, 0, 150, 120
bpm_number_size = 20, 21
bpm_number_crop_box = 0, 0, 45, 42
percent_number_size = 18, 19
score_number_size = 15, 16
score_number_crop_box = 0, 0, 136, 122
medal_resize_highlight = 84, 36
medal_resize_list = 51, 22
medal_crop_box = 0, 2, 188, 76
grade_resize_highlight = 27, 28
grade_resize_list = 16, 17
grade_crop_box = 0, 0, 64, 65

# Static Images
background = Image.open('{}{}'.format(folder, 'bg2.jpg')).resize((1360, 768), Image.ANTIALIAS)
song_highlighted = Image.open('{}{}'.format(folder, 'msel_0.png')).resize(main_image_size, Image.ANTIALIAS)
song_list_top = Image.open('{}{}'.format(folder, 'msel_1.png')).resize(song_list_size, Image.ANTIALIAS)
song_list_bottom = Image.open('{}{}'.format(folder, 'msel_2.png')).resize(song_list_size, Image.ANTIALIAS)
song_list_level_top = Image.open('{}{}'.format(folder, 'msel_lev1.png')).resize(song_list_size, Image.ANTIALIAS)
song_list_bar = Image.open('{}{}'.format(folder, 'msel_bar.png')).resize((32, 768), Image.ANTIALIAS)
song_list_cursor = Image.open('{}{}'.format(folder, 'msel_barcur.png')).resize((32, 32), Image.ANTIALIAS)
button_legend = Image.open('{}{}'.format(folder, 'msel_info.gif')).crop((0, 0, 810, 48)).resize(button_legend_size, Image.ANTIALIAS)
button_legend_mask = Image.open('{}{}'.format(folder, 'msel_info.gif')).crop((810, 0, 1620, 48)).resize(button_legend_size, Image.ANTIALIAS).convert(mode="L")
border_animation = Image.open('{}{}'.format(folder, 'msel_bgani1.gif')).crop((0, 0, 1706, 12))
border_animation_mask = Image.open('{}{}'.format(folder, 'msel_bgani1.gif')).crop((0, 0, 1706, 12)).convert(mode="RGBA")
difficulty_background = Image.open('{}{}'.format(folder, 'msel_0_difficulty.png')).crop((0, 111, 460, 221)).resize(difficulty_size, Image.ANTIALIAS)
difficulty_cursor = Image.open('{}{}'.format(folder, 'msel_0_cur.gif')).crop((0, 859, 200, 940))
difficulty_cursor_mask = difficulty_cursor.convert(mode="L")

# Numbers and Medals
numbers_highlight = []
numbers_list = []
for _ in range(20):
    x = difficulty_number_crop_box
    y = x[0], x[1] + (120*_), x[2], x[3] + (120*_)
    z = Image.open('{}{}'.format(folder, 'msel_level.png')).crop(y).resize(difficulty_number_highlight_resize, Image.ANTIALIAS)
    numbers_highlight.append(z)
    z = Image.open('{}{}'.format(folder, 'msel_level.png')).crop(y).resize(difficulty_number_list_resize, Image.ANTIALIAS)
    numbers_list.append(z)

bpm_numbers_highlight = []
for _ in range(12):
    x = bpm_number_crop_box
    y = x[0], x[1] + (41 * _), x[2], x[3] + (41 * _)
    z = Image.open('{}{}'.format(folder, 'msel_0_bpmnum.png')).crop(y).resize(bpm_number_size, Image.ANTIALIAS)
    bpm_numbers_highlight.append(z)

score_numbers = []
percent_numbers = []
for _ in range(10):
    x = score_number_crop_box
    y = x[0], x[1] + (120 * _), x[2], x[3] + (120 * _)
    z = Image.open('{}{}'.format(folder, 'num0.png')).crop(y).resize(score_number_size, Image.ANTIALIAS)
    score_numbers.append(z)
    z = Image.open('{}{}'.format(folder, 'num0.png')).crop(y).resize(percent_number_size, Image.ANTIALIAS)
    percent_numbers.append(z)

medals_highlight = []
medals_list = []
for _ in range(8):
    x = medal_crop_box
    y = x[0], x[1] + (78 * _), x[2], x[3] + (78 * _)
    z = Image.open('{}{}'.format(folder, 'msel_medal.png')).crop(y).resize(medal_resize_highlight, Image.ANTIALIAS)
    medals_highlight.append(z)
    z = Image.open('{}{}'.format(folder, 'msel_medal.png')).crop(y).resize(medal_resize_list, Image.ANTIALIAS)
    medals_list.append(z)

grade_highlight = []
grade_list = []
for _ in range(8):
    x = grade_crop_box
    y = x[0], x[1] + (65 * _), x[2], x[3] + (65 * _)
    z = Image.open('{}{}'.format(folder, 'msel_grade.png')).crop(y).resize(grade_resize_highlight, Image.ANTIALIAS)
    grade_highlight.append(z)
    z = Image.open('{}{}'.format(folder, 'msel_grade.png')).crop(y).resize(grade_resize_list, Image.ANTIALIAS)
    grade_list.append(z)

enhancer = ImageEnhance.Brightness(border_animation_mask)
border_animation_mask = enhancer.enhance(0.4)
border_animation_mask = border_animation_mask.convert(mode="L")

background.paste(border_animation, (0, 16), mask=border_animation_mask)
background.paste(border_animation, (0, 705), mask=border_animation_mask)
#
background.paste(song_list_top, (485, -3), mask=song_list_top)
background.paste(numbers_list[18], (505, 40), mask=numbers_list[18])
background.paste(medals_list[2], (525, 35), mask=medals_list[2])
background.paste(grade_list[5], (589, 38), mask=grade_list[5])

fnt = ImageFont.truetype('font/MS-PGothic.ttf', 18, encoding='unic')
txt = Image.new('RGBA', size=(400, 40), color=(255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.text((0, 0), "Song Title", font=fnt, fill=(255, 255, 255, 255))
background.paste(txt, (620, 5), mask=txt)

fnt = ImageFont.truetype('font/MS-PGothic.ttf', 14, encoding='unic')
txt = Image.new('RGBA', size=(400, 40), color=(255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.text((0, 0), "Artist Name", font=fnt, fill=(255, 255, 255, 255))
background.paste(txt, (670, 28), mask=txt)
#
background.paste(song_list_top, (424, 44), mask=song_list_top)
background.paste(numbers_list[18], (445, 87), mask=numbers_list[18])
background.paste(medals_list[3], (465, 82), mask=medals_list[3])
background.paste(grade_list[6], (528, 85), mask=grade_list[6])

fnt = ImageFont.truetype('font/MS-PGothic.ttf', 18, encoding='unic')
txt = Image.new('RGBA', size=(400, 40), color=(255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.text((0, 0), "Song Title", font=fnt, fill=(255, 255, 255, 255))
background.paste(txt, (570, 53), mask=txt)

fnt = ImageFont.truetype('font/MS-PGothic.ttf', 14, encoding='unic')
txt = Image.new('RGBA', size=(400, 40), color=(255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.text((0, 0), "Artist Name", font=fnt, fill=(255, 255, 255, 255))
background.paste(txt, (620, 77), mask=txt)
#
background.paste(song_list_top, (373, 95), mask=song_list_top)
background.paste(numbers_list[18], (393, 138), mask=numbers_list[18])
background.paste(medals_list[5], (413, 133), mask=medals_list[5])
background.paste(grade_list[4], (477, 136), mask=grade_list[4])

fnt = ImageFont.truetype('font/MS-PGothic.ttf', 18, encoding='unic')
txt = Image.new('RGBA', size=(400, 40), color=(255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.text((0, 0), "Song Title", font=fnt, fill=(255, 255, 255, 255))
background.paste(txt, (520, 103), mask=txt)

fnt = ImageFont.truetype('font/MS-PGothic.ttf', 14, encoding='unic')
txt = Image.new('RGBA', size=(400, 40), color=(255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.text((0, 0), "Artist Name", font=fnt, fill=(255, 255, 255, 255))
background.paste(txt, (570, 128), mask=txt)
#
background.paste(song_list_level_top, (329, 149), mask=song_list_level_top)
fnt = ImageFont.truetype('font/MS-PGothic.ttf', 24, encoding='unic')
txt = Image.new('RGBA', size=(400, 40), color=(255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.text((0, 0), "LV 19", font=fnt, fill=(255, 255, 255, 255))
background.paste(txt, (500, 168), mask=txt)
#
background.paste(song_list_bottom, (436, 599), mask=song_list_bottom)
background.paste(numbers_list[18], (455, 701), mask=numbers_list[18])
background.paste(medals_list[0], (475, 696), mask=medals_list[0])
background.paste(grade_list[0], (540, 700), mask=grade_list[0])

fnt = ImageFont.truetype('font/MS-PGothic.ttf', 18, encoding='unic')
txt = Image.new('RGBA', size=(400, 40), color=(255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.text((0, 0), "Song Title", font=fnt, fill=(255, 255, 255, 255))
background.paste(txt, (580, 663), mask=txt)

fnt = ImageFont.truetype('font/MS-PGothic.ttf', 14, encoding='unic')
txt = Image.new('RGBA', size=(400, 40), color=(255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.text((0, 0), "Artist Name", font=fnt, fill=(255, 255, 255, 255))
background.paste(txt, (630, 696), mask=txt)
#
background.paste(song_list_bottom, (378, 545), mask=song_list_bottom)
background.paste(numbers_list[18], (398, 647), mask=numbers_list[18])
background.paste(medals_list[4], (418, 642), mask=medals_list[4])
background.paste(grade_list[4], (482, 647), mask=grade_list[4])

fnt = ImageFont.truetype('font/MS-PGothic.ttf', 18, encoding='unic')
txt = Image.new('RGBA', size=(400, 40), color=(255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.text((0, 0), "Song Title", font=fnt, fill=(255, 255, 255, 255))
background.paste(txt, (520, 608), mask=txt)

fnt = ImageFont.truetype('font/MS-PGothic.ttf', 14, encoding='unic')
txt = Image.new('RGBA', size=(400, 40), color=(255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.text((0, 0), "Artist Name", font=fnt, fill=(255, 255, 255, 255))
background.paste(txt, (580, 641), mask=txt)
#
background.paste(song_list_bottom, (330, 490), mask=song_list_bottom)
background.paste(numbers_list[18], (350, 591), mask=numbers_list[18])
background.paste(medals_list[6], (370, 586), mask=medals_list[6])
background.paste(grade_list[6], (434, 592), mask=grade_list[6])

fnt = ImageFont.truetype('font/MS-PGothic.ttf', 18, encoding='unic')
txt = Image.new('RGBA', size=(400, 40), color=(255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.text((0, 0), "Song Title", font=fnt, fill=(255, 255, 255, 255))
background.paste(txt, (470, 554), mask=txt)

fnt = ImageFont.truetype('font/MS-PGothic.ttf', 14, encoding='unic')
txt = Image.new('RGBA', size=(400, 40), color=(255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.text((0, 0), "Artist Name", font=fnt, fill=(255, 255, 255, 255))
background.paste(txt, (525, 585), mask=txt)
#
background.paste(song_highlighted, (275, 204), mask=song_highlighted)
background.paste(medals_highlight[1], (313, 502), mask=medals_highlight[1])
background.paste(grade_highlight[3], (590, 508), mask=grade_highlight[3])
background.paste(difficulty_background, (296, 358), mask=difficulty_background)
background.paste(numbers_highlight[5], (316, 368), mask=numbers_highlight[5])
background.paste(numbers_highlight[13], (424, 368), mask=numbers_highlight[13])
background.paste(numbers_highlight[18], (532, 368), mask=numbers_highlight[18])
background.paste(numbers_highlight[19], (640, 368), mask=numbers_highlight[19])
background.paste(bpm_numbers_highlight[7], (600, 297), mask=bpm_numbers_highlight[7])
background.paste(bpm_numbers_highlight[0], (620, 297), mask=bpm_numbers_highlight[0])
background.paste(bpm_numbers_highlight[11], (640, 297), mask=bpm_numbers_highlight[11])
background.paste(bpm_numbers_highlight[4], (660, 297), mask=bpm_numbers_highlight[4])
background.paste(bpm_numbers_highlight[2], (680, 297), mask=bpm_numbers_highlight[2])
background.paste(bpm_numbers_highlight[6], (700, 297), mask=bpm_numbers_highlight[6])

background.paste(score_numbers[0], (430, 518), mask=score_numbers[0])
background.paste(score_numbers[8], (446, 518), mask=score_numbers[8])
background.paste(score_numbers[7], (462, 518), mask=score_numbers[7])
background.paste(score_numbers[5], (478, 518), mask=score_numbers[5])
background.paste(score_numbers[5], (494, 518), mask=score_numbers[5])
background.paste(score_numbers[1], (510, 518), mask=score_numbers[1])
background.paste(score_numbers[3], (526, 518), mask=score_numbers[3])
background.paste(score_numbers[0], (542, 518), mask=score_numbers[0])

# background.paste(percent_numbers[1], (637, 510), mask=percent_numbers[1])
background.paste(percent_numbers[9], (652, 510), mask=percent_numbers[9])
background.paste(percent_numbers[8], (672, 510), mask=percent_numbers[8])
background.paste(difficulty_cursor, (467, 368), mask=difficulty_cursor_mask)

# Highlight Text
fnt = ImageFont.truetype('font/MS-PGothic.ttf', 26, encoding='unic')
txt = Image.new('RGBA', size=(400, 40), color=(255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.text((0, 0), "Song Title", font=fnt, fill=(255, 255, 255, 255))

background.paste(txt, (460, 218), mask=txt)

fnt = ImageFont.truetype('font/MS-PGothic.ttf', 20, encoding='unic')
txt = Image.new('RGBA', size=(400, 40), color=(255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.text((0, 0), "Artist Name", font=fnt, fill=(255, 255, 255, 255))

background.paste(txt, (460, 250), mask=txt)

fnt = ImageFont.truetype('font/MS-PGothic.ttf', 16, encoding='unic')
txt = Image.new('RGBA', size=(400, 40), color=(255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.text((0, 0), "Effecter", font=fnt, fill=(255, 255, 255, 255))

background.paste(txt, (424, 476), mask=txt)

fnt = ImageFont.truetype('font/MS-PGothic.ttf', 20, encoding='unic')
txt = Image.new('RGBA', size=(400, 40), color=(0, 0, 0, 0))
d = ImageDraw.Draw(txt)
d.text((0, 0), "Illustrator", font=fnt, fill=(0, 0, 0, 255))

background.paste(txt, (865, 468), mask=txt)

fnt = ImageFont.truetype('font/MS-PGothic.ttf', 16, encoding='unic')
txt = Image.new('RGBA', size=(400, 40), color=(255, 255, 255, 0))
d = ImageDraw.Draw(txt)
d.text((0, 0), "This is a comment message", font=fnt, fill=(255, 255, 255, 255))

background.paste(txt, (738, 509), mask=txt)

#
background.paste(song_list_bar, (1328, 0), mask=song_list_bar)
background.paste(song_list_cursor, (1328, 200), mask=song_list_cursor)
background.paste(button_legend, (715, 730), mask=button_legend_mask)
background.save('output.png', quality=100)

