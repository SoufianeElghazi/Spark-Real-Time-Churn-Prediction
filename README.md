
<h1 style='color:#4c4893' align='center'>
    Projet d'Analyse Big Data : Prédiction de la Churn dans les Télécommunications en Temp réel.
</h1>

<div style="background-color:white; color:black; font-size:15px; font-family:Verdana; padding:10px; border: 5px solid black;font-weight:bold;">
De nos jours ,La gestion efficace du désabonnement est cruciale pour les opérateurs de télécommunications, car elle peut avoir un impact significatif sur leurs revenus et leur réputation. Les efforts visant à comprendre les besoins des clients, à anticiper leurs attentes et à offrir des solutions adaptées contribuent à renforcer la fidélité des clients, réduisant ainsi les taux de désabonnement.
</div><br>

<div style="text-align:center;height:70;">
    <img src="https://media.licdn.com/dms/image/C5612AQG0Gilk9mJpxw/article-cover_image-shrink_720_1280/0/1621963349834?e=2147483647&v=beta&t=S-3_jI-4xWu14OSyh7RJg93TQmLc_QWTZAW5Gd_aL8s" width=700 alt="image1">
</div><br>

<div style="background-color:white; color:black; font-size:15px; font-family:Verdana; padding:10px; border: 5px solid black;font-weight:bold;">
Pour cela , ce Projet vise a créer un modèle de prédictions de désabonnement des clients afin que les opérateurs gère auparavent les tentatives de désabonnement et d'améliorer la satisfaction des clients pour les fédiliser .
</div><br>

<div style="background-color:white; color:black; font-size:15px; font-family:Verdana; padding:10px; border: 5px solid black;font-weight:bold;">
Nous avons developper un modèle de prédiction des churn de télécome en utilisant Pyspark le Notebook qui contient l'EDA et la construction de modèle (Random Forest) se situe dans le dossier <span style="color:orangered;">SPARK_ML/ </span>
</div><br>

<div style="background-color:white; color:black; font-size:15px; font-family:Verdana; padding:10px; border: 5px solid black;font-weight:bold;">
Ensuite , nous avons exploiter ce modèle pour nous générer des prédictions sur un flux des données qui arrive en temps réel vers <span style="color:black;">Spark structred Streaming</span> passant par <span style="color:cyan;">kafka </span> comme service de messagerie puis stocker les résultats dans <span style="color:blue;">Snowflake </span>  qui est un datawharhouse dans le cloud afin de créer un dashboard avec <span style="color:orange;">Power Bi</span> qui va nous permettre de visualiser en temps réel les données .</span> 
</div><br>

<div style="background-color:white; color:black; font-size:15px; font-family:Verdana; padding:10px; border: 5px solid black;font-weight:bold;">
Par la suite nous avons ajouter une partie de l'analyse de graphe avec la composante <span style="color:red;">GraphX</span> de Spark comme bonus sur un jeu de données de data center en visant analyser les importances des départements selon les appels qui ont un niveau de satisfactions elevé . 
</div><br>


<div style="background-color:white; color:black; font-size:15px; font-family:Verdana; padding:10px; border: 5px solid black;font-weight:bold;">
Dans ce Répértoir vous allez trouver les éléments suivants:
<ul>
    <li><span style="color:purple">SPARK_GraphX:</span><span style="color:black"> La partie d'analyse de graphe</span></li>
    <li><span style="color:purple">SPARK_Streaming_Pipeline</span><span style="color:black"> Ce dossier contient la partie de Pipeline et Spark Structred Streaming </span>
    <li><span style="color:purple">SPARK_ML:</span><span style="color:black"> Ce dossier contient la partie de l'analyse exploratoir , la segmentation et la classification en utilisant spark mllib .</span></li>
    <li><span style="color:purple">Presentation:</span><span style="color:black">Ce dossier contient la présentation pptx</span></li>
</ul>
</div>

<h1 style='color:yellow' align='center'>
    Fin
</h1>



