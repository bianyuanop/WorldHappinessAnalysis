# World Happiness Analysis

## Data Sources

Sustainable Development Goals: https://www.kaggle.com/datasets/theworldbank/sustainable-development-goals

World Happiness: 	https://www.kaggle.com/datasets/unsdsn/world-happiness

Local copies of these datasets can be found in the `dataset` folder. The `developed_countries.csv` dataset is based on the IMF's 2018 World Economic Outlook report, which can be downloaded from here: https://www.imf.org/~/media/Files/Publications/WEO/2018/October/English/main-report/Text.ashx?la=en 

## How to run the project

1. Create an environment with the project's dependencies by running `conda env create --name noclue --file=environments.yml` from the project folder

2. `conda activate noclue`

3. Run the cells in `processing_all_datasets.ipynb` first to generate the necessary datasets

4. Either one of these notebooks can be executed:
  - To see the Dystopia residual analysis, run the contents of `dystopia_redisual_analysis.ipynb`
  - To see urbanization indicator and happiness score predictions with FPNN and LSTM, run the contents of `modeling.ipynb`
