import subprocess

def publish_site():
    try:
        subprocess.run(["quarto", "render"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during Quarto render: {e}")
        return

    try:
        subprocess.run(["git", "add", "."], check=True)
        commit_message = input("Enter commit message: ")
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error pushing changes to repo: {e}")
        return

publish_site()
