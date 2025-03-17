FROM python:3.12

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        texlive-latex-base \
        texlive-fonts-recommended \
        texlive-fonts-extra \
        texlive-latex-extra && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY latex_generator ./latex-generator

WORKDIR /app/latex-generator

RUN mkdir -p ./artifacts/task_1

COPY img ./img

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "python generate_latex.py && pdflatex res.tex && tail -f /dev/null"]

# tail -f /dev/null используется, чтобы контейнер оставался живым для проверки сгенерированного PDF