import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

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

n_clusters = st.slider('Número de Dias do Festival', 1, 6, 3)
num_columns = st.slider('Número de Palcos no Festival', 1, 4, 3)
affinity_help = '''
                Affinity (afinidade): O parâmetro "affinity" define a função de afinidade que calcula a distância entre os pontos de dados.\n
                Opções:\n
                Euclidean (euclidiana): Usa a distância euclidiana padrão para calcular a proximidade entre pontos.\n
                Manhattan (manhattan): Usa a distância de Manhattan, que é a soma das diferenças absolutas entre as coordenadas dos pontos.\n
                Cosine (cosseno): Calcula a afinidade entre pontos de dados usando a medida de similaridade de cosseno. O cosseno é usado para avaliar a direção e a proximidade dos vetores que representam os pontos.
            '''
affinity = st.selectbox('Hiperparâmetro - Affinity:', ['euclidean', 'manhattan', 'cosine'], help=affinity_help)
linkage_help = '''
                Linkage (ligação): O parâmetro "linkage" define a métrica usada para medir a distância entre clusters durante o processo de aglomeração.\n
                Opções:\n
                Complete (completa): Usa a maior distância entre quaisquer dois pontos nos clusters para decidir como mesclá-los.\n
                Average (média): Usa a média das distâncias entre todos os pontos nos clusters para decidir como mesclá-los.\n
                Single (única): Usa a menor distância entre quaisquer dois pontos nos clusters para decidir como mesclá-los.
            '''
linkage = st.selectbox('Hiperparâmetro - Linkage:', ['complete', 'average', 'single'], help=linkage_help)

if st.button('Iniciar Simulação'):
    df = pd.read_csv('responses.csv')
    musical_data = df[['Dance', 'Folk', 'Country', 'Classical music', 'Musical', 'Pop', 'Rock', 'Metal or Hardrock', 'Punk', 'Hiphop, Rap', 'Reggae, Ska', 'Swing, Jazz', 'Rock n roll', 'Alternative', 'Latino', 'Techno, Trance', 'Opera']]
    musical_data = musical_data.fillna(1)

    agg_cl = AgglomerativeClustering(n_clusters=n_clusters, affinity=affinity, linkage=linkage)
    agg_cl.fit(musical_data)

    dataset_with_clusters = musical_data.copy()
    dataset_with_clusters['clusters'] = agg_cl.labels_

    genre_palette = sns.color_palette("Set1", n_colors=3)

    for cluster in range(n_clusters):
        cluster_data = dataset_with_clusters[dataset_with_clusters['clusters'] == cluster]
        genre_counts = {}

        for genre in musical_data.columns:
            genre_counts[genre] = cluster_data[genre].sum()

        top_genres = sorted(genre_counts, key=genre_counts.get, reverse=True)[:num_columns]

        genre_colors = sns.color_palette("Set1", n_colors=num_columns)

        cluster_genre_counts = pd.Series({genre: genre_counts[genre] for genre in top_genres})

        fig, ax = plt.subplots(figsize=(6, 3))
        cluster_genre_counts.plot(kind='bar', ax=ax, color=genre_colors)

        plt.ylabel('Contagem')
        plt.title(f'Dia {cluster+1}\nGêneros Musicais')
        plt.xticks(rotation=45)
        st.pyplot(fig)
