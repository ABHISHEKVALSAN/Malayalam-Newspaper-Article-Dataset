# Malayalam-Newspaper-Article-Dataset
Project does web scraping. It scraps articles from a malayalam newspaper(janmabhumi) website to create a corpus of news articles. Also a set of queries is created and corresponding ground truth answers is retrieved by a combination of bm25 method and tf-idf method. The dataset can be useful for creating tools like stemmer, stopwords removal, lemmatizers, etc...
## DATASET

Directly download the Datset from [Dropbox](https://www.dropbox.com/s/s5d1xw20c7rxapy/DataSet.zip?dl=0)

## OR

### Execution

Open a terminal (*Ctrl+Alt+T*) and execute the given commands

```bash

git clone https://github.com/ABHISHEKVALSAN/Malayalam-Newspaper-Article-Dataset 
cd Malayalam-Newspaper-Article-Dataset
mkdir DataSet 
pip install -r requirements.txt 
python3 MalayalamScraping.py 
```

#### PS
 1. After running the last command, you'll see files being created in the DataSet directory 
 2. Lot of urls have files missing... It is usual
 3. The scraping is website specific and hence donot work for other newspaper sites.

 
### Project Requirements
 1. Python 
 2. Pip installed
 3. Internet connection

Contact me at email given below for assistance or raise an issue.

Email : abhiavk@iitk.ac.in

## Related Works

A similar repo with Telugu DataSet can be found [here](https://github.com/AnushaMotamarri/Telugu-Newspaper-Article-Dataset).
