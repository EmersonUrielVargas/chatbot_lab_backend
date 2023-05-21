from llama_index import SimpleDirectoryReader

def pdfDataReader(path):
    pdf = SimpleDirectoryReader(path).load_data()
    return pdf