import os
import time

# Before Section
def find_latest_log_file(directory):
    log_files = []
    for f in os.listdir(directory):
        if f.endswith('.log'):
            log_files.append(f)

    if not log_files:
        return "No log files found in the directory."

    latest_file = log_files[0]
    latest_mtime = os.path.getmtime(os.path.join(directory, latest_file))
    
    for f in log_files[1:]:
        mtime = os.path.getmtime(os.path.join(directory, f))
        if mtime > latest_mtime:
            latest_file = f
            latest_mtime = mtime
    
    return os.path.join(directory, latest_file)

def read_new_content(file_path, last_size):
    current_size = os.path.getsize(file_path)
    if current_size > last_size:
        with open(file_path, 'r') as file:
            file.seek(last_size)
            new_content = file.read()
        return new_content, current_size
    return "", current_size

def before():
    directory = "C:\\logfiles\\OEA2"
    latest_log_file = find_latest_log_file(directory)
    if "No log files found" in latest_log_file:
        print(latest_log_file)
        return None, None

    # Time 1: Seek to the end of the file
    last_size = os.path.getsize(latest_log_file)
    print("Time 1: Positioned at end of file, size:", last_size)
    return latest_log_file, last_size

# TestSection
def find_and_click(imageName): 
    wait(imageName)
    click(imageName)

def test_section():
    print("---------------------\nSTEP 1: Hit the renew btn")
    find_and_click("renew_btn.png")

    print("---------------------\nSTEP 2: FILL IN CHECK BOXES in the Pre-check-Auth.vue")
    questions = ["page1_text1.png", 
            "page1_text2.png", 
            "page1_text3.png", 
            "page1_text4.png", 
            "page1_text5.png"]
    for img in questions:
                find_and_click(img)
    find_and_click("complete.png");
    # find_and_click("cancel.png");
    find_and_click("I_accept.png");
    find_and_click("I_accept.png");
    find_and_click("quit.png");
    # find_and_click("I_accept.png");

# AfterTest
def after_test(latest_log_file, last_size):
    # Pause for 1 second before proceeding
    time.sleep(1)

    # Time 2: Read new content appended to the file
    new_content, last_size = read_new_content(latest_log_file, last_size)
    print("Time 2: New content appended:")
    print(new_content)

def main():
    latest_log_file, last_size = before()
    if latest_log_file and last_size is not None:
        test_section()
        after_test(latest_log_file, last_size)

if __name__ == "__main__":
    main()
