
from PIL import Image, ImageDraw, ImageFont

width, height = 1800, 1300
bg_color = (255, 255, 255)
title_text = "형석고 유니버스 가족 계보도"
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

img = Image.new("RGB", (width, height), color=bg_color)
draw = ImageDraw.Draw(img)

title_font = ImageFont.truetype(font_path, 60)
draw.text((width//2 - 500, 30), title_text, font=title_font, fill=(255, 0, 255))

def draw_box(name, desc, x, y, color):
    box_w, box_h = 300, 150
    draw.rectangle([x, y, x + box_w, y + box_h], fill=color, outline="black", width=4)
    name_font = ImageFont.truetype(font_path, 28)
    desc_font = ImageFont.truetype(font_path, 20)
    draw.text((x + 10, y + 10), name, font=name_font, fill="black")
    draw.text((x + 10, y + 60), desc, font=desc_font, fill="black")

draw_box("연은숙", "전우철 엄마 / 꼬꼬빌 청소부", 50, 150, "#FFEB3B")
draw_box("전홍기", "전우철 아빠 / 백수", 400, 150, "#FFCDD2")
draw_box("전다은", "누나 / 중국 판다처럼 삶", 750, 150, "#C5E1A5")
draw_box("전우철", "형석고 고3", 1150, 150, "#81D4FA")

draw_box("정빅뱅", "정우주 아빠 / 인민군", 50, 350, "#E1BEE7")
draw_box("정하늘", "정우주 형", 400, 350, "#F8BBD0")
draw_box("정자연", "정우주 누나", 750, 350, "#F8BBD0")
draw_box("정자왕", "막내", 1150, 350, "#F8BBD0")
draw_box("정우주", "형석고 고3", 1550, 350, "#CE93D8")

draw_box("김광수", "김수욱 형 / 미친 물", 100, 550, "#FFF176")
draw_box("김수욱", "형석고 고3 / 별명: 아랍인", 450, 550, "#FFD54F")

draw_box("안철근", "안세형 아빠 / 풀무원 배달", 800, 550, "#E6EE9C")
draw_box("김소연", "엄마 / 잡혀사는 중", 1150, 550, "#FFECB3")
draw_box("안재혁", "형 / 폐급 병장", 1450, 550, "#FFAB91")
draw_box("안세형", "형석고 고3", 1750, 550, "#AED581")

draw_box("이재민", "형 / 요리사 혼자 다 먹음", 200, 750, "#B3E5FC")
draw_box("이재현", "형석고 고3", 550, 750, "#81D4FA")

img.save("형석고_유니버스_가족계보도_최종_v2.png")
