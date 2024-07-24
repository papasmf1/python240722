import os
import shutil

# 경로 설정
download_folder = r"C:\Users\student\Downloads"
image_folder = os.path.join(download_folder, 'images')
data_folder = os.path.join(download_folder, 'data')
docs_folder = os.path.join(download_folder, 'docs')
archive_folder = os.path.join(download_folder, 'archive')

# 폴더 생성 함수
def create_folder_if_not_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# 폴더 생성
create_folder_if_not_exists(image_folder)
create_folder_if_not_exists(data_folder)
create_folder_if_not_exists(docs_folder)
create_folder_if_not_exists(archive_folder)

# 파일 이동 함수
def move_files(extension_list, destination_folder):
    for filename in os.listdir(download_folder):
        if any(filename.lower().endswith(ext) for ext in extension_list):
            shutil.move(os.path.join(download_folder, filename), destination_folder)

# 파일 이동 설정
move_files(['.jpg', '.jpeg'], image_folder)
move_files(['.csv', '.xlsx'], data_folder)
move_files(['.txt', '.doc', '.pdf'], docs_folder)
move_files(['.zip'], archive_folder)

print("파일 이동이 완료되었습니다.")
