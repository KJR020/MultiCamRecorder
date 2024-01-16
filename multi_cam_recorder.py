import subprocess
import logging
from concurrent.futures import ThreadPoolExecutor


def setup_logger():
    # ロガーの設定
    logger = logging.getLogger("ffmpeg_logger")
    logger.setLevel(logging.INFO)

    # ファイルハンドラの設定
    file_handler = logging.FileHandler("logs/ffmpeg_logs.log")
    file_handler.setLevel(logging.INFO)

    # コンソールハンドラの設定
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # フォーマッタの設定
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # ハンドラをロガーに追加
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


logger = setup_logger()


# コマンドを生成する関数
def create_command(camera_name):
    # ffmpeg コマンドのフォーマット
    cmd = f'ffmpeg -f dshow -i video="{camera_name}" -c:v libx264 -crf 23 -preset veryfast -segment_time 10 -strftime 1 "output_{camera_name.replace(" ", "_").lower()}_%Y%m%d_%H%M%S.mp4"'
    return cmd


def run_command(cmd):
    """コマンドを実行し、その出力をロギングする関数"""
    try:
        with subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True
        ) as process:
            stdout, stderr = process.communicate()
            if process.returncode != 0:
                logger.error(f"Error in command {cmd}: {stderr}")
            else:
                logger.info(f"Command completed successfully: {cmd}")
    except Exception as e:
        logger.exception(f"Exception occurred while running command: {cmd}")


if __name__ == "__main__":
    # カメラのリスト
    # この部分は外部ファイルやコマンドライン引数から取得するように調整可能
    cameras = ["Surface Camera Front", "Surface Camera Rear", "OBS Virtual Camera"]
    # コマンドリストの生成
    commands = [create_command(camera) for camera in cameras]

    # コマンドの実行
    with ThreadPoolExecutor(max_workers=len(commands)) as executor:
        futures = [executor.submit(run_command, cmd) for cmd in commands]

        for future in futures:
            future.result()
