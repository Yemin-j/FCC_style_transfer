# import os
# import cv2
#
# # 폴더 경로 설정
# input_folder = "D:/gems/third_year/final_experiment/fcc_improvement/data/inverse_crop_kor/512/"
# output_folder = "D:/gems/third_year/final_experiment/fcc_improvement/result/cv2/histequal/"
#
# # CLAHE 매개변수 설정
# clipLimit = 2.0
# tilesize = (8, 8)
# clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=tilesize)
#
# # 폴더 안의 모든 파일에 대해 처리
# for filename in os.listdir(input_folder):
#     if filename.endswith(".tif"):
#         # 이미지 파일 읽기
#         src = cv2.imread(os.path.join(input_folder, filename), -1)
#
#         # 이미지 채널 분리
#         b, g, r = cv2.split(src)
#
#         # CLAHE 적용
#         # b = clahe.apply(b)
#         # g = clahe.apply(g)
#         # r = clahe.apply(r)
#
#         # CLAHE 적용
#         b = cv2.equalizeHist(b)
#         g = cv2.equalizeHist(g)
#         r = cv2.equalizeHist(r)
#
#         # 채널 합치기
#         dst = cv2.merge((b, g, r))
#
#         # 결과 이미지 저장
#         cv2.imwrite(os.path.join(output_folder, f"{filename}"), dst)


import os
import cv2

# 폴더 경로 설정
input_folder = "D:/gems/phd_student/style_transfer/styleid/test/input/style"
output_folder = "D:/gems/phd_student/style_transfer/styleid/test/input/style"

# CLAHE 매개변수 설정
clipLimit = 2.0
tilesize = (8, 8)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

# 폴더 안의 모든 파일에 대해 처리
for filename in os.listdir(input_folder):
    if filename.endswith(".tif"):
        # 이미지 파일 읽기
        src = cv2.imread(os.path.join(input_folder, filename), -1)

        # 이미지 채널 분리
        b, g, r = cv2.split(src)

        # CLAHE 적용
        b = clahe.apply(b)
        g = clahe.apply(g)
        r = clahe.apply(r)

        # histequal 적용
        # b = cv2.equalizeHist(b)
        # g = cv2.equalizeHist(g)
        # r = cv2.equalizeHist(r)

        # 채널 합치기
        dst = cv2.merge((b, g, r))

        # 결과 이미지 저장
        cv2.imwrite(os.path.join(output_folder, f"{filename}_clahe.tif"), dst)
        # cv2.imwrite('D:/gems/third_year/final_experiment/fcc_improvement/result/cv2/full/clahe/clahe_2.0_(4, 4).tif', dst)