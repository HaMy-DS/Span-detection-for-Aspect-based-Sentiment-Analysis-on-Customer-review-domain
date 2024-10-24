# Span Detection for Aspect-based Sentiment Analysis on Customer Review Domain

*This is an academic project based on paper: https://arxiv.org/abs/2110.07833*

## Introduction

With the growth of e-commerce platforms and online shopping, product reviews in text form have become increasingly diverse. Most customers read these reviews to check if a product meets their needs in aspects like durability, compactness, or service quality. Since a product may have hundreds or thousands of reviews, it’s difficult and time-consuming for customers to read and evaluate multiple options on their own.
To automate this process, in this project, we will implement Aspect-Based Sentiment Analysis (ABSA) on user feedback using the UIT-ViSD4SA dataset.

### Aspect-Based Sentiment Analysis (ABSA)

Aspect-Based Sentiment Analysis (ABSA) is a task in natural language processing focused on analyzing and evaluating user sentiments toward specific aspects within a text. Key definitions in ABSA include:

- **Aspect**: An object, feature, or attribute of a product, service, event, or other entity in the text being analyzed. In the UIT-ViSD4SA dataset, aspects include: GENERAL, PERFORMANCE, BATTERY, SER&ACC, CAMERA, DESIGN, FEATURES, SCREEN, PRICE, STORAGE.

- **Sentiment Analysis**: The process of analyzing and evaluating user sentiments in a text, categorized as positive (POSITIVE), negative (NEGATIVE), or neutral (NEUTRAL).

- **Span**: A key concept for identifying aspects and opinions in the text, represented as a (start, end) index pair. "Start" indicates the beginning of the aspect or opinion, while "end" marks the conclusion. Spans are usually determined by locating keywords or terms related to aspects or opinions in the text.


Accurately identifying spans for aspects and opinions is crucial in ABSA as it directly impacts the accuracy of sentiment analysis and predictions.

***Aspect-Based Sentiment Analysis (ABSA)*** refers to the process of analyzing and evaluating user sentiments toward specific aspects within a text.

<p align="center">
<img width="660" alt="{490FBA69-9F45-4A48-83D3-7F0712D823D0}" src="https://github.com/user-attachments/assets/727639e0-84e4-4b55-9b6b-e8c445d6a468">
</p>

Our process for solving this problem is as follows. First, we preprocess the data before feeding it into the models. Then, we apply Transformer models such as PhoBERT, BERT, XML-RoBERTa, and BiLSTM to predict aspects, sentiments, and aspects combined with sentiments, and compare the performance across these models.

## Results

<p align="center">
  <img width="600" alt="{E7151A2B-E81C-4551-8E2B-9A99BB83C9ED}" src="https://github.com/user-attachments/assets/ae24cd00-eb9a-461c-a4d5-3ab0c51ccdbb">
</p>

<p align="center">
  <img width="600" alt="{A9444A70-75F0-4D10-A0F6-F3837C201D6E}" src="https://github.com/user-attachments/assets/fc85d24f-8ede-4ad4-af2e-4db0c3149b18">
</p>

<p align="center">
<img width="600" alt="{616EDCEC-4785-4E31-82C2-7954A55A95D8}" src="https://github.com/user-attachments/assets/8256ff53-2e2f-43c3-b658-87042a620b46">
</p>



From the results, PhoBERT-Large performs best across all three span extraction tasks, while BiLSTM performs the worst. However, in the Sentiment task, BiLSTM's results are nearly identical to mBERT's due to the fewer labels involved (2 labels for B, I * 3 emotion labels + O + ENDPAD). In contrast, the aspect extraction task has 22 labels, and the combined aspect and emotion extraction task has 62 labels. The combined task shows very low performance (below 5%) due to the large number of labels. Additionally, BiLSTM, which encodes words without context, struggles with Vietnamese, where many words have multiple meanings, leading to its consistently low results.
