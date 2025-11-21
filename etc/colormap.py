import numpy as np
from PIL import Image
import random
import matplotlib.pyplot as plt

def create_balanced_random_grid_image(width=256, height=256, grid_size=16, colors=None):
    """
    width, height: 이미지 크기
    grid_size: 격자 크기 (격자 몇 개로 나눌지)
    colors: RGB 색상 목록 [r, g, b] 형태로 지정
    
    각 색상이 전체 격자의 약 1/len(colors) 비율로 나타나도록 함
    """
    if colors is None:
        # 기본 색상 5가지
        colors = [
            [10, 21, 32],     # 짙은 검정색
            [22, 39, 54],     # 중간 톤의 남색
            [255, 255, 255],  # 흰색
            [179, 107, 40],   # 주황색
            [105, 48, 32]     # 적갈색
        ]
    
    # 이미지 생성
    img = np.zeros((height, width, 3), dtype=np.uint8)
    
    # 각 격자의 크기 계산
    cell_height = height // grid_size
    cell_width = width // grid_size
    
    # 총 격자 수
    total_cells = grid_size * grid_size
    
    # 각 색상의 목표 셀 수 계산 (비율을 맞추기 위함)
    cells_per_color = total_cells // len(colors)
    
    # 모든 격자 위치를 리스트로 만듦
    all_positions = [(i, j) for i in range(grid_size) for j in range(grid_size)]
    
    # 리스트 섞기
    random.shuffle(all_positions)
    
    # 색상별로 할당할 위치 분할
    color_positions = {}
    start_idx = 0
    
    for i, color in enumerate(colors):
        if i == len(colors) - 1:  # 마지막 색상은 남은 모든 위치 사용
            color_positions[i] = all_positions[start_idx:]
        else:
            color_positions[i] = all_positions[start_idx:start_idx + cells_per_color]
            start_idx += cells_per_color
    
    # 각 색상을 지정된 위치에 배치
    for color_idx, positions in color_positions.items():
        color = colors[color_idx]
        for i, j in positions:
            y_start = i * cell_height
            y_end = (i + 1) * cell_height
            x_start = j * cell_width
            x_end = (j + 1) * cell_width
            
            img[y_start:y_end, x_start:x_end] = color
    
    return img

# 함수 사용 예시
if __name__ == "__main__":
    # 이미지 생성
    grid_image = create_balanced_random_grid_image(
        width=256, 
        height=256, 
        grid_size=16,  # 16x16 격자
        colors=[
            [10, 21, 32],     # 짙은 검정색
            [22, 39, 54],     # 중간 톤의 남색
            [255, 255, 255],  # 흰색
            [179, 107, 40],   # 주황색
            [105, 48, 32]     # 적갈색
        ]
    )
    
    # 이미지 저장
    pil_image = Image.fromarray(grid_image)
    pil_image.save("D:/gems/phd_student/style_transfer/styleid/test/input/style/five_color_balanced_grid.png")
    
    # # 이미지 표시
    # plt.figure(figsize=(6, 6))
    # plt.imshow(grid_image)
    # plt.axis('off')
    # plt.title("5가지 색상의 256x256 랜덤 격자 이미지")
    # plt.show()