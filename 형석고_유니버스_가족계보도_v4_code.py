
from PIL import Image, ImageDraw, ImageFont
import os

# 캔버스 설정
width, height = 2200, 1800
img = Image.new("RGB", (width, height), color=(255, 255, 255))
draw = ImageDraw.Draw(img)
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# 제목
title_font = ImageFont.truetype(font_path, 70)
desc_font = ImageFont.truetype(font_path, 22)
draw.text((width//2 - 600, 30), "형석고 유니버스 가족 계보도", font=title_font, fill=(255, 105, 180))

# 박스 그리기 함수
def draw_box(name, desc, x, y, color):
    box_w, box_h = 320, 160
    draw.rectangle([x, y, x + box_w, y + box_h], fill=color, outline="black", width=4)
    name_font = ImageFont.truetype(font_path, 32)
    draw.text((x + 15, y + 15), name, font=name_font, fill="black")
    draw.text((x + 15, y + 65), desc, font=desc_font, fill="black")

# 전우철 가족
draw_box("연은숙", "전우철 엄마 / 꼬꼬빌 청소부", 100, 150, "#FFFF99")
draw_box("전홍기", "아빠 / 백수", 450, 150, "#FFCCCB")
draw_box("전다은", "누나 / 중국에서 판다처럼 삶", 800, 150, "#CCFFCC")
draw_box("전우철", "본인 / 형석고 고3", 1150, 150, "#ADD8E6")

# 정우주 가족
draw_box("정빅뱅", "아빠 / 인민군", 100, 400, "#E1BEE7")
draw_box("정하늘", "형", 450, 400, "#F8BBD0")
draw_box("정자연", "누나", 800, 400, "#F8BBD0")
draw_box("정자왕", "막내", 1150, 400, "#F8BBD0")
draw_box("정우주", "본인 / 형석고 고3", 1500, 400, "#CE93D8")

# 김수욱 가족
draw_box("김광수", "형 / 미친 물 / 국어 알려줌", 100, 650, "#FFF176")
draw_box("김수욱", "본인 / 형석고 고3 / 아랍인", 450, 650, "#FFD54F")

# 안세형 가족
draw_box("안철근", "아빠 / 풀무원 배달", 800, 650, "#E6EE9C")
draw_box("김소연", "엄마 / 잡혀사는 중", 1150, 650, "#FFECB3")
draw_box("안재혁", "형 / 폐급 병장", 1500, 650, "#FFAB91")
draw_box("안세형", "본인 / 형석고 고3", 1850, 650, "#AED581")

# 이재현 가족
draw_box("이재민", "형 / 요리사 / 혼자 다 먹음", 200, 900, "#B3E5FC")
draw_box("이재현", "본인 / 형석고 고3", 550, 900, "#81D4FA")

# 로고/깃발 박스
draw.rectangle([1700, 100, 2000, 280], fill="#EEEEEE", outline="black", width=3)
draw.text((1720, 130), "HSHU 로고", font=desc_font, fill="gray")

draw.rectangle([1700, 300, 2000, 480], fill="#EEEEEE", outline="black", width=3)
draw.text((1720, 330), "HSHU 깃발", font=desc_font, fill="gray")

img.save("형석고_유니버스_가족계보도_최종_v4.png")
