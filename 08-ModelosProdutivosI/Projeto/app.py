import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

# st.markdown('''
#             Isso é um Texto Simples **Isso é negrito** e *isso é itálico*.
#             ''')

st.title('Projeto Modelos Produtivos I')
st.markdown('''
            Dataset: Young People Survey\n
            https://www.kaggle.com/datasets/miroslavsabo/young-people-survey?select=responses.csv\n

            O Dataset contém 1.010 registros dos gostos musicais de pessoas da Eslováquia com idades entre 15 e 30 anos. São 17 gêneros musicais.
            ''')

st.title('História')
st.markdown('''
Uma empresa de eventos que tem como objetivo fazer um festival de música está precisando de uma orientação em como solucionar o problema de separação de uma população em grupos com interesses musicais em comum.\n
Para isso solicitou a nossa equipe para analisar os dados de seus usuários e propor uma solução para o seu problema!
            ''')

st.title('!!! Análise do Festival de Música !!!')


# Adicione controles deslizantes para hiperparâmetros
n_clusters = st.slider('Número de Dias do Festival:', 1, 10, 4)
affinity = st.selectbox('Hiperparametro - Affinity:', ['euclidean', 'manhattan', 'cosine'])
linkage = st.selectbox('Hiperparametro - Linkage:', ['ward', 'complete', 'average', 'single'])

# Botão para iniciar a simulação
if st.button('Iniciar Simulação'):
    # Carregue o conjunto de dados (substitua 'responses.csv' pelo caminho correto)
    df = pd.read_csv('responses.csv')
    musical_data = df[['Dance', 'Folk', 'Country', 'Classical music', 'Musical', 'Pop', 'Rock', 'Metal or Hardrock', 'Punk', 'Hiphop, Rap', 'Reggae, Ska', 'Swing, Jazz', 'Rock n roll', 'Alternative', 'Latino', 'Techno, Trance', 'Opera']]
    musical_data = musical_data.fillna(1)

    # Execute o modelo AgglomerativeClustering com os hiperparâmetros selecionados
    agg_cl = AgglomerativeClustering(n_clusters=n_clusters, affinity=affinity, linkage=linkage)
    agg_cl.fit(musical_data)

    # Copie os dados originais e adicione as labels de clusters
    dataset_with_clusters = musical_data.copy()
    dataset_with_clusters['clusters'] = agg_cl.labels_

    # Calcular os clusters com base no dendrograma e no número de clusters escolhidos
    linkage_matrix = sch.linkage(musical_data, method=linkage)

    # Crie uma figura para o dendrograma com cores diferentes para o número de clusters
    # plt.figure(figsize=(8, 6))
    # dendrograma = sch.dendrogram(linkage_matrix, leaf_font_size=8, color_threshold=0)
    # plt.title('Dendrograma')
    # plt.xlabel('Gêneros Musicais')
    # plt.ylabel('Distância')
    # plt.xticks([])
    # st.pyplot()

    # Define uma paleta de cores para as categorias de gêneros musicais
    genre_palette = sns.color_palette("Set1", n_colors=3)

    # Itere pelos clusters e crie um gráfico para cada um deles com as barras coloridas dos três maiores gêneros
    for cluster in range(n_clusters):
        cluster_data = dataset_with_clusters[dataset_with_clusters['clusters'] == cluster]
        genre_counts = {}
        
        for genre in musical_data.columns:
            genre_counts[genre] = cluster_data[genre].sum()
        
        top_genres = sorted(genre_counts, key=genre_counts.get, reverse=True)[:3]
        
        # Crie uma lista de cores da paleta para as categorias
        genre_colors = [genre_palette[i % len(genre_palette)] for i in range(3)]
        
        cluster_genre_counts = pd.Series({genre: genre_counts[genre] for genre in top_genres})
        
        # Criar um subplot para o gráfico do cluster
        fig, ax = plt.subplots(figsize=(8, 6))
        cluster_genre_counts.plot(kind='bar', ax=ax, color=genre_colors)
        plt.xlabel('Gênero Musical')
        plt.ylabel('Contagem')
        plt.title(f'Gêneros Musicais - Dia {cluster+1}')
        plt.xticks(rotation=45)
        st.pyplot(fig)
