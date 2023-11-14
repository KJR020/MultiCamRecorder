import pytest
from ffmpeg_recorder.recorder import create_command, run_commands


def test_create_command():
    camera_name = "Test Camera"
    expected_command = f"echo Testing {camera_name}"
    assert create_command(camera_name) == expected_command


def test_run_commands():
    test_cameras = ["Test Camera 1", "Test Camera 2"]
    test_commands = [create_command(camera) for camera in test_cameras]
    # 実際のコマンド実行結果をテストするのは難しいため、この関数がエラーなく完了するかどうかを確認する
    try:
        run_commands(test_commands)
    except Exception as e:
        pytest.fail(f"run_commands threw an exception: {e}")
