import subprocess
from pathlib import Path

def compile_latex(tex_file: str):
    tex_path = Path(tex_file)

    if not tex_path.exists():
        raise FileNotFoundError(f"{tex_file} not found")

    cmd = [
        "lualatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        tex_path.name
    ]

    subprocess.run(
        cmd,
        cwd=tex_path.parent,
        check=True
    )

    print("✅ PDF compiled successfully using LuaLaTeX")

if __name__ == "__main__":
    compile_latex("doc.tex")  # change filename if needed
