from utils import (generate_latex_table, generate_latex_image)


def generate_latex():
    # task_1
    data = [
        ['h1', 'h2', 'h3', 'h4'],
        ['r1c1', 'r1c2', 'r1c3', 'r1c4'],
        ['r2c1', 'r2c2', 'r2c3', 'r2c4'],
        ['r3c1', 'r3c2', 'r3c3', 'r3c4'],
        ['r4c1', 'r4c2', 'r4c3', 'r4c4'],
    ]

    table = generate_latex_table(data)
    with open("artifacts/task_1/task_1.tex", "w", encoding="utf-8") as f:
        f.write(table)

    # task_2
    image = generate_latex_image(
        image_path="hw-2/artifacts/2024-08-08 13.03.49.jpg",
        height="200px",
        centering=True
    )
    result = (
            r"""\documentclass{article}
    \usepackage[utf8]{inputenc}
    \usepackage{graphicx}
    \begin{document}
    """
            + table
            + "\n"
            + image
            + "\n\\end{document}"
    )
    with open("temp/res.tex", "w", encoding="utf-8") as f:
        f.write(result)

if __name__ == "__main__":
    generate_latex()