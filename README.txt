Prerequisites:
Must have Python, Jupyter (for reading and executing IPython Notebooks), Scrapy Web_Crawling Framework and Scikit-Learn installed.

Steps:
Part 1: Crawl the website and get the forum threads
1. Create a project using the below command:
scrapy startproject cs410fedforum
2. Copy the file finance_spider.py into the cs410fedforum/spiders folder
3. Go to the project’s top level directory and run:
scrapy crawl financeforums -o financetopics.json

Part 2: Training the classifier
1. Download the data directory which contains the training data for categories
2. Download the CS410FedForums-Categorization IPython notebook 
3. Copy the json file financetopics.json from Part 1 above to the same path as the CS410FedForums-Categorization IPython notebook
4. In the CS410FedForums-Categorization IPython notebook, replace the path of the data directory in the first parameter of load_files on this line:
docs_to_train = sklearn.datasets.load_files("C:\Users\gayat\ipythonnotebooks\data", description=None, categories=None, load_content=True, shuffle=True, 
                                            encoding='utf-8', decode_error='strict', random_state=0)
5. In the CS410FedForums-Categorization IPython notebook, replace the path in this line with wherever you want the output file to be created:
filename="C:\Users\gayat\ipythonnotebooks\categorization_output.txt"
6. Run the CS410FedForums-Categorization IPython notebook.

Part 3: Creating the Topic Map
1. Download the NMF_LDA_TopicMap IPython notebook.
2. Copy the json file financetopics.json from Part 1 above to the same path as the NMF_LDA_TopicMap IPython notebook.
3. In the NMF_LDA_TopicMap IPython notebook, replace the path in this line with wherever you want the output file to be created:
filename="C:\Users\gayat\ipythonnotebooks\output.txt"
4. Run the NMF_LDA_TopicMap IPython notebook

Part 4: Visualization of the data
The json file from Part 1 above was used to create a quick visualization of top trending forum threads by views, replies and dates. This visualization is available here:
https://public.tableau.com/profile/gayatri.balakrishnan#!/vizhome/CS410FederatedForumsVisualization/MostPopularandMostViewedThreadsbyYear
https://public.tableau.com/profile/gayatri.balakrishnan#!/vizhome/CS410FederatedForumsVisualization/MostViewedThreads
https://public.tableau.com/profile/gayatri.balakrishnan#!/vizhome/CS410FederatedForumsVisualization/MostPopularThreads