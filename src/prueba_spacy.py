import spacy

# Cargar el modelo de español
nlp = spacy.load("es_core_news_sm")

# Texto de prueba
doc = nlp("Hola, este es un asistente inteligente en desarrollo.")

# Mostrar cada token con su categoría gramatical
for token in doc:
    print(token.text, token.pos_)
