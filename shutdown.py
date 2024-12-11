import os
import time
import ctypes

# create directory
download_folder = "C:/Users/PC/Downloads"


# check file in directory and add to the set
def get_files_in_downloads():
    print(set(os.listdir(download_folder)))
    return set(os.listdir(download_folder))


def shutdown_computer():
    print("Komputer akan mati dalam 10 detik.")
    os.system("shutdown /s /t 10")

def main():
    print("Monitoring folder unduhan...")
    before_files = get_files_in_downloads()
    # to run code and monitoring
    while True:
        time.sleep(1800)  
        after_files = get_files_in_downloads()

        #if any new file
        new_files = after_files - before_files
        if new_files:
            print(f"File baru selesai diunduh: {', '.join(new_files)}")
            shutdown_computer()
            break
        before_files = after_files

if __name__ == "__main__":
    main()
