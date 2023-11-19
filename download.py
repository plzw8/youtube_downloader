import subprocess
from concurrent.futures import ProcessPoolExecutor


def download_video(url, download_path):
    # for windows
    # command = f'yt-dlp -f bestvideo+bestaudio -o "{download_path}\\%(title)s.%(ext)s" "{url}"'
    # for linux
    command = f'yt-dlp -f bestvideo+bestaudio -o "{download_path}/%(title)s.%(ext)s" "{url}"'
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Downloaded video from {url}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while downloading {url}: {e}")


def download_youtube_videos_concurrently(url_list, download_path, max_processes=8):
    with ProcessPoolExecutor(max_workers=max_processes) as executor:
        futures = [executor.submit(download_video, url, download_path) for url in url_list]
        for future in futures:
            future.result()


def read_url_list(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    url_list = read_url_list('list2.txt')
    download_youtube_videos_concurrently(url_list, "./download")
