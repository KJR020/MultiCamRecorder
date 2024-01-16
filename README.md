# MultiCamRecorder

## 概要 
**MultiCamRecorder** は、ffmpegを利用して複数のカメラからの映像ストリームを録画するツールです。
複数台のIPカメラを並列し録画したいという経緯で作成しました。

## インストール方法

### 前提条件
- このツールは**ffmpeg**に依存しており、ffmpegがシステムにインストールされている必要があります。

### Windowsでのffmpegインストール
1. **ダウンロード**: [公式ffmpegウェブサイト](https://ffmpeg.org/download.html) からWindows用のビルドをダウンロードしてください。
2. **解凍**: ダウンロードしたZIPファイルを解凍し、任意の場所に保存します。
3. **PATH設定**: ffmpegのbinディレクトリ（例：`C:\ffmpeg\bin`）をシステムのPATH環境変数に追加します。
