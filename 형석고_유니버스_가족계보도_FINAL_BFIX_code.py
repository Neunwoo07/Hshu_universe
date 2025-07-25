
from PIL import Image, ImageDraw, ImageFont

# 캔버스 설정
width, height = 2400, 1800
img = Image.new("RGB", (width, height), color=(255, 255, 255))
draw = ImageDraw.Draw(img)
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
title_font = ImageFont.truetype(font_path, 80)
desc_font = ImageFont.truetype(font_path, 24)
name_font = ImageFont.truetype(font_path, 36)

# 제목
draw.text((width // 2 - 500, 30), "형석고 유니버스 가족 계보도", font=title_font, fill=(255, 0, 180))

def draw_box(name, desc, x, y, color):
    box_w, box_h = 340, 160
    draw.rectangle([x, y, x + box_w, y + box_h], fill=color, outline="black", width=5)
    draw.text((x + 15, y + 15), name, font=name_font, fill="black")
    draw.text((x + 15, y + 70), desc, font=desc_font, fill="black")

# 전우철 가족
draw_box("연은숙", "엄마 / 꼬꼬빌 청소부", 100, 150, "#FFFF99")
draw_box("전홍기", "아빠 / 백수", 480, 150, "#FFCCCB")
draw_box("전다은", "누나 / 중국에서 판다처럼 삶", 860, 150, "#CCFFCC")
draw_box("전우철", "형석고 고3", 1240, 150, "#ADD8E6")

# 정우주 가족
draw_box("정빅뱅", "아빠 / 인민군", 100, 400, "#E1BEE7")
draw_box("정하늘", "형", 480, 400, "#F8BBD0")
draw_box("정자연", "누나", 860, 400, "#F8BBD0")
draw_box("정자왕", "막내", 1240, 400, "#F8BBD0")
draw_box("정우주", "형석고 고3", 1620, 400, "#CE93D8")

# 김수욱 (형 제거된 설명)
draw_box("김수욱", "형석고 고3 / 별명: 아랍인", 100, 650, "#FFD54F")

# 안세형 가족
draw_box("안철근", "아빠 / 풀무원 배달", 480, 650, "#E6EE9C")
draw_box("김소연", "엄마 / 잡혀사는 중", 860, 650, "#FFECB3")
draw_box("안재혁", "형 / 폐급 병장", 1240, 650, "#FFAB91")
draw_box("안세형", "형석고 고3", 1620, 650, "#AED581")

# 이재현 가족 (이재민은 형으로 수정됨)
draw_box("이재민", "형 / 요리사 / 혼자 다 먹음", 100, 900, "#B3E5FC")
draw_box("이재현", "형석고 고3", 480, 900, "#81D4FA")

# 로고 / 깃발
draw.rectangle([1900, 100, 2200, 220], fill="#EEEEEE", outline="black", width=4)
draw.text((1920, 130), "HSHU 로고", font=desc_font, fill="gray")
draw.rectangle([1900, 250, 2200, 370], fill="#EEEEEE", outline="black", width=4)
draw.text((1920, 280), "HSHU 깃발", font=desc_font, fill="gray")

# 저장
img.save("형석고_유니버스_가족계보도_FINAL_BFIX.png")
