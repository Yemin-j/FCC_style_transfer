import os, glob
import cv2
import numpy as np
from tqdm import tqdm
from PIL import Image
import re

# NIQE
# from basicsr.metrics.niqe import calculate_niqe
# Sharpness (Laplacian variance)
# R‑NHSIQA using PIQ to compute Fréchet distance from feature embeddings
# from piq import inception_score  # 하지만 R-NHSIQA는 직접 구현 필요
# CONTRIQUE
from subprocess import run

# 경로 설정
ref_dir = "D:/gems/phd_student/data/fcc/crop_kor/resize"
gen_dir = "D:/gems/phd_student/style_transfer/result/ecdf"

results = []

gen_imgs = sorted(glob.glob(os.path.join(gen_dir, "*.tif")))

for gen_path in tqdm(gen_imgs):
    fname = os.path.basename(gen_path)
    match = re.search(r"(\d{8}_\d{4})", fname).group(1)
    ref_path = [os.path.join(ref_dir, f) for f in os.listdir(ref_dir) if match in f][0]
    if not os.path.exists(ref_path):
        continue

    # 이미지 불러오기
    gen = cv2.imread(gen_path, cv2.IMREAD_GRAYSCALE)
    ref = cv2.imread(ref_path, cv2.IMREAD_GRAYSCALE)

    # NIQE
    # niqe_val = calculate_niqe(gen.astype(np.float32), 0)

    # Sharpness (Laplacian variance)
    lap = cv2.Laplacian(gen, cv2.CV_64F, ksize=1)
    # Sharpness (Sobel variance)
    sobel_x = cv2.Sobel(gen, cv2.CV_64F, 1, 0, ksize=1)  # x 방향
    sobel_y = cv2.Sobel(gen, cv2.CV_64F, 0, 1, ksize=1)  # y 방향
    sobel_total = cv2.magnitude(sobel_x, sobel_y)
    # Sharpness (Sobel variance)
    edges = cv2.Canny(gen, threshold1=10, threshold2=200)

    sharpness = lap.var()

    # R‑NHSIQA: feature 분포 일치도 (예시: inception embeddings + Fréchet distance)
    # 실제 구현시 이미지 feature 평균/공분산 계산 + FID 수식 적용

    # CONTRIQUE 점수 호출 (CLI 방법)
    cmd = [
        "python", "demo_score.py",
        "--im_path", gen_path,
        "--model_path", "models/CONTRIQUE_checkpoint25.tar",
        "--linear_regressor_path", "models/CLIVE.save"
    ]
    # result = run(cmd, capture_output=True, text=True)
    # contra_score = float(result.stdout.strip())

    results.append({
        "filename": fname,
        "NIQE": niqe_val,
        "Sharpness": sharpness,
        # "R-NHSIQA": rn_hsiqa_val,
        # "CONTRIQUE": contra_score
    })

# 결과 출력
for r in results[:5]:
    print(r)
