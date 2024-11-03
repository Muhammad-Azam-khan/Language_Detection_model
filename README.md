# Language Detection Model

## Overview
This project involves developing a language detection model that classifies text data into various languages. The dataset consists of 22,000 entries covering 22 unique languages, aiming to accurately identify the language of the given text.

## Dataset
The dataset comprises two columns:
- **Text**: Contains the text data in various languages.
- **Language**: Indicates the corresponding language for each text entry.

### Unique Languages
The dataset includes the following languages:
- Arabic
- Chinese
- Dutch
- English
- Estonian
- French
- Hindi
- Indonesian
- Japanese
- Korean
- Latin
- Persian
- Portuguese
- Pushto
- Romanian
- Russian
- Spanish
- Swedish
- Tamil
- Thai
- Turkish
- Urdu

## Classification Report
The following classification report summarizes the model's performance:

| Language   | Precision | Recall | F1-Score | Support |
|------------|-----------|--------|----------|---------|
| Arabic     | 1.00      | 1.00   | 1.00     | 299     |
| Chinese    | 0.95      | 0.56   | 0.70     | 300     |
| Dutch      | 0.99      | 0.99   | 0.99     | 299     |
| English    | 0.73      | 1.00   | 0.84     | 300     |
| Estonian   | 1.00      | 0.98   | 0.99     | 300     |
| French     | 0.98      | 1.00   | 0.99     | 297     |
| Hindi      | 1.00      | 0.97   | 0.98     | 297     |
| Indonesian | 0.99      | 0.98   | 0.99     | 292     |
| Japanese   | 0.69      | 0.88   | 0.77     | 300     |
| Korean     | 1.00      | 0.97   | 0.99     | 300     |
| Latin      | 1.00      | 0.92   | 0.96     | 286     |
| Persian    | 1.00      | 0.99   | 1.00     | 300     |
| Portuguese | 1.00      | 0.98   | 0.99     | 299     |
| Pushto     | 1.00      | 0.94   | 0.97     | 298     |
| Romanian   | 0.98      | 0.99   | 0.98     | 300     |
| Russian    | 0.99      | 0.99   | 0.99     | 300     |
| Spanish    | 0.99      | 0.98   | 0.98     | 299     |
| Swedish    | 0.99      | 1.00   | 1.00     | 298     |
| Tamil      | 1.00      | 0.99   | 0.99     | 294     |
| Thai       | 1.00      | 0.99   | 0.99     | 300     |
| Turkish    | 0.99      | 0.99   | 0.99     | 300     |
| Urdu       | 1.00      | 0.98   | 0.99     | 300     |

### Overall Metrics
- **Accuracy**: 96%
- **Macro Avg Precision**: 0.97
- **Macro Avg Recall**: 0.96
- **Macro Avg F1-Score**: 0.96
- **Weighted Avg Precision**: 0.97
- **Weighted Avg Recall**: 0.96
- **Weighted Avg F1-Score**: 0.96

## Insights
- **High Performers**: Languages like Arabic, Dutch, Estonian, Korean, and Persian show excellent precision and recall.
- **Moderate Performers**: Chinese and Japanese exhibit lower recall and precision, indicating areas for improvement.
- **Balanced Results**: The model maintains strong overall performance, suggesting reliability in language detection.

## Recommendations for Improvement
- Investigate specific patterns causing misclassifications, particularly for Chinese and Japanese.
- Enhance model tuning or data augmentation strategies to improve performance on English.

## Conclusion
The language detection model demonstrates high accuracy and robustness across diverse languages, making it suitable for various applications such as multilingual content analysis, customer support, and localization efforts.


## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

