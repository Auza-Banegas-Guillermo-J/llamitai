Followin Repo is a simple example of a rag based LLM that uses txt files.

**DOOCKER FILE NON-FUNCTIONAL, Work in progress**

the local version requieres ollama to be serving an embeding model and an llm model, in this case nomic and deepseek respectively.
a yaml file is attached to replicate the enviroment, in my case a conda env.

the api version requieres a .env file to be in the working directory to acces openai API services for both embeding and LLM services.

```OPEN_API_KEY="My open ai api key"```

the repo has a cli version that uses a predetermined question and a gui version that uses streamlit and receives user input prompts.

Finally, the algorithms expect there is a ./docs/txt directory to work for rag functionaly, a ./chroma_db directory can be inserted or created if there is none.

![image showing Gui](./imgs/GUI_Example.png)

```plaintext
.
├── chroma_db
│   ├── chroma.sqlite3
│   └── f7addd67-f77e-40a3-a548-d9827348035a
│       ├── data_level0.bin
│       ├── header.bin
│       ├── length.bin
│       └── link_lists.bin
├── Dockerfile
├── docs
│   ├── pdfs
│   │   ├── DIY_Drone_1.pdf
│   │   └── DIY_Drone_2.pdf
│   └── txt
│       └── case_1.txt
├── my_LLM.py
└── streamlit.py
```
