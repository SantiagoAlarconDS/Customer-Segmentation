# Market Segmentation for Internet Services in San Juan Bautista Parish, San Cristóbal Municipality, Táchira State

This readme file provides an overview of a market segmentation research project for my BBA, conducted for internet services in the San Juan Bautista Parish, located in the San Cristóbal Municipality, Táchira State. The objective of this study was to identify distinct segments within the local market to meet the specific needs and preferences of each segment.

## Results
This market segmentation study provides several business benefits for internet service providers operating in the San Juan Bautista Parish:

1. **Enhanced Customer Understanding:** Gain a comprehensive understanding of the diverse customer segments within the market, enabling targeted and personalized services for the 3 obtained segments.
2. **Improved Marketing Effectiveness:** Develop and implement tailored marketing strategies for each segment, maximizing the impact of promotional efforts and increasing customer acquisition and retention rates.
3. **Competitive Advantage:** By catering to the specific needs and preferences of each segment, businesses can differentiate themselves from competitors and strengthen their market position.
4. **Resource Optimization:** Allocate resources more efficiently by focusing on the most promising market segments, reducing wastage and improving overall business efficiency.
   

* **For a more comprehensive analysis of the obtained results, please consult the attached document "analysis.docx" Additionally, kindly note that this summary provides an overview of the original research paper conducted in Spanish, available as "spanish_analysis.docx"**

## Objectives Statement
The main objective of this market segmentation study was to establish a segmentation of the market for internet services in the San Juan Bautista Parish. The specific objectives included:
1. Designing a representative sample to operationalize the market segmentation.
2. Identifying market segments based on data obtained from the sample in the San Juan Bautista Parish.
 Specifying the characteristics of each identified segment in relation to internet services.

## Challenges
The challenges faced during this study included:
1. Gathering accurate and reliable data on the demographics, socioeconomic status, and behavior of consumers in the San Juan Bautista Parish.
2. Analyzing the dirty data to identify meaningful and distinct market segments.
3. Developing marketing strategies that effectively catered to the unique needs and preferences of each identified segment.

# Dataset Description

The dataset contains information collected from a survey conducted by myself to gather insights about internet service preferences and satisfaction among participants. It includes the following columns:

- **Age Range:** The age of the survey participants.
- **Gender:** The gender of the survey participants.
- **Occupation:** The occupation of the survey participants.
- **Household Size:** Captures the total number of people living in the respondents' houses, including themselves.
- **Consideration of Household Needs:** 1 if the participants consider or would consider the needs of other household members when acquiring an internet service, 0 otherwise.
- **Rating of Internet Service Features:** Rates the importance of various features of the internet service at the time of acquisition. (The order of the features reflects their importance, where the first elements are the most important.)
- **Internet Usage:** Captures the amount of time respondents use the internet daily.
- **Internet Service Providers:** Represents specific internet service providers available to the respondents.
- **Internet Provider:** Specifies the internet service provider chosen by the respondents.
- **Budget Range:** Represents the range within which respondents allocate their budget for the internet service (Cantv, Vnet, Wisplay, NetUno, Inter, Cable Norte and Infinitics).
- **Ideal Price Range:** Captures respondents' opinion on the ideal price range for the internet service.
- **Satisfaction with the Service:** Indicates respondents' satisfaction level with their internet provider.
- **Service Factors:** Represents different factors related to the internet service (Price, Customer Service and Support, Speed, Uninterrupted Signal Service, Payment Methods).
- **Willingness to Continue with Increased Price:** 1 if the participants would be willing to continue with the internet service provider if the price increased, 0 otherwise.
- **Recommendation Source:** Represents different sources through which respondents discovered about the internet service provider (Through the recommendation of someone you know, Internet, Social Media (Named on the dataset as Social Media Coms), Television, Radio, Billboards, Posters or Stickers outdoors, Newspapers or magazines), providing insights into the effectiveness of various marketing channels.

To provide more valuable insights new columns were created to simplify the information and add more value to the analysis. These columns included:

- **Price Matches:** It was the combination of the column "Budget Range" and the column "Ideal Price Range" If the responses to these questions matched, a value of “Match” was assigned. Otherwise, “Not Match” was entered.
- **Best**: This column was derived from the column "Rating of Internet Service Features" where the characteristic in the first place was extracted as the most important.
- **Best2**: Using the same basis as the previous column, the second most important characteristic was extracted.
- **Least**: Similarly, using the column "Rating of Internet Service Features" the least important characteristic, in this case the last one was extracted.



## Methodology
The following methodology was adopted to address the research objectives and challenges:
1. Literature Review: Conducted an extensive review of existing literature on market segmentation and internet services to establish a solid theoretical framework.
2. Sample Design: Determined the sample size and designed the participant selection process. Employed probabilistic sampling techniques to ensure representativeness.
3. Data Collection: Administered surveys to residents of the San Juan Bautista Parish to collect relevant information on their demographics, socioeconomic status, and behavior regarding internet services.
4. Data Analysis: Analyzed the collected data using statistical and multivariate analysis techniques, such as cluster analysis, factor analysis, and discriminant analysis, to identify distinct market segments.
5. Segment Identification: Based on the data analysis results, identified and described the different market segments present in the San Juan Bautista Parish, grouping them according to common characteristics and behaviors related to internet services.
6. Segment Specification: Detailed the demographic, socioeconomic, geographic, and psychographic characteristics of each identified segment, as well as their specific needs, preferences, and behaviors regarding internet services.
7. Business Benefit: Provided recommendations and insights to internet service providers on how to adapt their services and marketing strategies to meet the needs of each identified segment, thereby enhancing their competitiveness and market positioning.

## Analysis Techniques
The following analysis techniques were employed in this study:
1. Demographic Analysis: Examined demographic data such as age, gender, occupation, etc., to gain insights into the composition of each segment.
2. Socioeconomic Analysis: Analyzed socioeconomic factors, including current and ideal expenditure on internet services, to understand the needs and preferences of each segment.
3. Communication Channel Analysis: Identified the most effective communication channels to reach each segment, such as social media, traditional media, word-of-mouth, etc.
4. Positioning and Loyalty Analysis: Assessed the satisfaction and loyalty of each segment towards internet services, as well as the relative positioning of different service providers in the market.
5. Consumption Habits Identification: Analyzed the consumption habits of each segment, including internet usage frequency, preferred services, common uses of the internet, etc., to tailor services and marketing strategies accordingly.

## Installation guide

Please read [install.md](install.md) for details on how to set up this project.

## Project Organization

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── install.md         <- Detailed instructions to set up this project.
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis
    │
    ├── .here              <- File that will stop the search if none of the other criteria
    │                         apply when searching head of project.
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .)
    │                         so customer_segmentation can be imported.
    │
    └── customer_segmentation               <- Source code for use in this project.
        ├── __init__.py    <- Makes customer_segmentation a Python module.
        │
        ├── data           <- Scripts to download or generate data.
        │   ├── __init__.py
        │   ├── clean_raw.ipynb
        │   ├── processed
        │   │   ├── processed.pkl       
        │   │   ├── spanish.pkl
        │   │   └── k_means_pca.pkl
        │   └── raw
        │       └── raw_data.xlsx
        │
        ├── utils          <- Scripts to help with common tasks.
        │   ├── __init__.py
        │   ├── encoding.py 
        │   ├── pandas_extension.py 
        │   └── paths.py   <- Helper functions to relative file referencing across project.
        │
        ├── visualization  <- Scripts to create exploratory and results oriented 
        │   └── visualize.ipynb
        │
        └── k_means.ipynb 

---
Project based on the [cookiecutter conda data science project template](https://github.com/jvelezmagic/cookiecutter-conda-data-science).
