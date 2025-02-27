FROM continuumio/miniconda3

WORKDIR /streamlit_app

COPY environment.yml .

RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "llamitai", "/bin/bash", "-c"]

COPY my_LLM.py ./
COPY streamlit.py ./

EXPOSE 8501

CMD ["conda", "run", "--no-capture-output", "-n", "llamitai", "streamlit", "run", "streamlit.py", "--server.address=0.0.0.0"]