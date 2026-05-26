import os
import sys

try:
    from huggingface_hub import HfApi
except ImportError:
    print("❌ Error: 'huggingface_hub' is not installed in your Python environment.")
    print("Please install it by running: pip install huggingface_hub")
    sys.exit(1)

def run_upload():
    print("=" * 60)
    print("🚀 HealthAI Chatbot - Hugging Face Space Uploader")
    print("=" * 60)
    print("This script uploads only your lightweight source files directly to Hugging Face.")
    print("It completely bypasses Git and avoids browser freezing by ignoring the large '.venv' folder.\n")

    # Get user credentials
    username = input("👤 Enter your Hugging Face Username: ").strip()
    if not username:
        print("❌ Username cannot be empty.")
        return

    space_name = input("📦 Enter your Hugging Face Space Name (e.g. healthai-chatbot): ").strip()
    if not space_name:
        print("❌ Space name cannot be empty.")
        return

    print("\n🔑 Enter your Hugging Face Write Token.")
    print("   (To get one, go to: https://huggingface.co/settings/tokens)")
    print("   (Ensure the token role is set to 'Write' or 'Fine-grained Write')")
    token = input("👉 Token: ").strip()
    if not token:
        print("❌ Token cannot be empty.")
        return

    repo_id = f"{username}/{space_name}"
    print(f"\n⏳ Preparing files for repository: spaces/{repo_id}...")

    # Define files/folders to upload
    ignore = [
        ".venv/**",
        "venv/**",
        "__pycache__/**",
        "**/.git/**",
        "*.pyc",
        "*.pyo",
        "upload_to_hf.py",  # exclude the script itself
        ".env"
    ]

    api = HfApi()

    try:
        print("📤 Uploading files... (This should take less than 10 seconds)")
        api.upload_folder(
            folder_path=".",
            repo_id=repo_id,
            repo_type="space",
            token=token,
            ignore_patterns=ignore
        )
        print("\n" + "=" * 60)
        print("🎉 SUCCESS! All files have been successfully uploaded.")
        print(f"🔗 View your Live Space here: https://huggingface.co/spaces/{repo_id}")
        print("=" * 60)
    except Exception as e:
        print("\n❌ Upload Failed!")
        error_msg = str(e)
        if "401" in error_msg or "Unauthorized" in error_msg:
            print("👉 Error: The token you entered is invalid. Please double-check it.")
        elif "403" in error_msg or "Forbidden" in error_msg:
            print("👉 Error: Your token does not have 'Write' access. Please create a token with 'Write' permissions.")
        elif "404" in error_msg:
            print(f"👉 Error: Space 'spaces/{repo_id}' was not found. Please make sure you created the Space on Hugging Face first.")
        else:
            print(f"👉 Details: {error_msg}")
        print("Please resolve the error and try running the script again.")

if __name__ == "__main__":
    try:
        run_upload()
    except KeyboardInterrupt:
        print("\n\n👋 Upload cancelled by user.")
        sys.exit(0)
