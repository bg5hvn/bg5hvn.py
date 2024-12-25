import os
import time
import shutil  # 用于删除非空文件夹
import logging

# 设置日志记录
logging.basicConfig(
    filename="clean_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def delete_old_files_and_folders(root_dir, days=3):
    """
    删除 root_dir 下修改时间超过指定天数的文件和文件夹（包括子目录）
    """
    current_time = time.time()
    time_limit = days * 86400  # 转换为秒
    
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        
        try:
            # 获取文件或文件夹的最后修改时间
            last_mod_time = os.path.getmtime(item_path)
            age_seconds = current_time - last_mod_time
            
            if age_seconds > time_limit:
                if os.path.isdir(item_path):
                    # 删除文件夹及其内容
                    shutil.rmtree(item_path)
                    logging.info(f"Deleted folder: {item_path}")
                    print(f"Deleted folder: {item_path}")
                else:
                    # 删除文件
                    os.remove(item_path)
                    logging.info(f"Deleted file: {item_path}")
                    print(f"Deleted file: {item_path}")
            else:
                # 如果是文件夹，递归检查其子目录
                if os.path.isdir(item_path):
                    print(f"Recursing into folder: {item_path}")
                    delete_old_files_and_folders(item_path, days)
        except Exception as e:
            logging.error(f"Error processing {item_path}: {e}")
            print(f"Error processing {item_path}: {e}")

# 指定多个目标目录
target_directories = [
    r"D:\ZXI\APC4.0\Data\Audio",        # 目录 1
    r"D:\ZXI\APC4.0\Data\MeasureRaw"    # 新增的目录
]

# 遍历目录并清理
for target_directory in target_directories:
    print(f"Processing directory: {target_directory}")
    delete_old_files_and_folders(target_directory, days=3)
