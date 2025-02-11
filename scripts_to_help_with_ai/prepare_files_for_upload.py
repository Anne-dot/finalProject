import os
import shutil
from pathlib import Path

# Get current working directory
current_dir = os.getcwd()

# Source and output directories (using relative paths)
source_dir = os.path.join(current_dir, '..', 'macros')
output_dir = os.path.join(current_dir, '..', 'files_for_claude_ai')

def copy_files():
    try:
        # Create output directory if it doesn't exist
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        print(f"Source directory: {source_dir}")
        print(f"Output directory: {output_dir}")
        
        # Check if source directory exists
        if not os.path.exists(source_dir):
            print(f"Error: Source directory '{source_dir}' does not exist!")
            return
            
        # Walk through all directories and files
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                try:
                    # Get full path of source file
                    src_file = os.path.join(root, file)
                    
                    # If file is .m1s, change extension to .txt
                    if file.lower().endswith('.m1s'):
                        new_file = os.path.splitext(file)[0] + '.txt'
                    else:
                        new_file = file
                        
                    # Create destination path
                    dst_file = os.path.join(output_dir, new_file)
                    
                    # Copy file to new location
                    shutil.copy2(src_file, dst_file)
                    print(f"Copied: {file} -> {new_file}")
                    
                except Exception as e:
                    print(f"Error copying {file}: {str(e)}")
                    
    except Exception as e:
        print(f"Main error: {str(e)}")

if __name__ == "__main__":
    copy_files()
    print("Process complete!")