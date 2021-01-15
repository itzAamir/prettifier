# Author: itzAamir
# Date : 14/01/2021

import os


def prettify_file(file_type):
    filtered_file_type = file_type.replace(".", "")
    destination = f"{os.getcwd()}/{filtered_file_type}"

    files_arr = os.listdir(os.getcwd())

    print(f"\nThese are the {file_type} files present in your directory: ")
    for files in files_arr:
        if files.endswith(file_type):
            print(files)

    confirmation = input("\nPress [y] to continue or any key to quit: ")

    if confirmation.lower() == "y":
        try:
            os.mkdir(filtered_file_type)
        except WindowsError:
            pass
        finally:
            file_count = 0
            for files in files_arr:
                if files.endswith(file_type):
                    os.replace(f"{os.getcwd()}/{files}",
                               f"{destination}/{files}")
                    file_count += 1

        print(
            f"\nTotal Files Transferred: {file_count}\nTransferred to file name: '{filtered_file_type}'\n")


if __name__ == "__main__":
    file_type = input("\nEnter the file type (Eg. '.txt'): ")
    try:
        prettify_file(file_type)
    except Exception as e:
        print(e)
