import subprocess
import shutil
import os

def build_latex(tex_file="main.tex", output_dir="out", final_pdf_dir="pdfs"):
    """
    Runs latexmk, creates necessary directories, and moves the output PDF.
    """
    # 1. Ensure the directories exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists(final_pdf_dir):
        os.makedirs(final_pdf_dir)

    # 2. Define the command
    command = [
        "latexmk",
        "-pdf",
        tex_file,
        "-interaction=nonstopmode",
        f"-output-directory={output_dir}",
        "-shell-escape"
    ]

    try:
        print(f"Running: {' '.join(command)}...")
        # 3. Execute the command
        subprocess.run(command, check=True)
        
        # 4. Identify the resulting PDF path
        # latexmk puts the pdf in the output_dir with the same basename as the tex file
        base_name = os.path.splitext(os.path.basename(tex_file))[0]
        generated_pdf = os.path.join(output_dir, f"{base_name}.pdf")
        final_destination = os.path.join(final_pdf_dir, f"{base_name}.pdf")

        # 5. Move the PDF
        if os.path.exists(generated_pdf):
            shutil.move(generated_pdf, final_destination)
            print(f"Success! PDF moved to: {final_destination}")
        else:
            print("Error: PDF was not found in the output directory.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred during LaTeX compilation: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Usage
if __name__ == "__main__":
    build_latex()