FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .

RUN conda env create -f environment.yml

RUN echo "conda activate myenv" >> ~/.bashrc

COPY my_LLM.py ./
COPY streamlit.py ./

EXPOSE 8501

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "myenv", "streamlit", "run", "streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]
