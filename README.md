# Real Estate Market Analysis of Itapema-SC

The data_clean.py file is responsible for cleaning and organizing the database, it must be run first.

The files questionone.py, questionfour.py and questionfive.py generate the graphs and tables used to answer the questions posed in the data analysis section of the challenge.

The real_estate_consulting_report.pdf file brings the requested report about the problems faced, solutions found, comments about the challenge and possible improvements in the code.

Therefore, the real_estate_consulting_report.pdf file, intended to be the answer to the challenge, was set up in such a way that it had a relevant storytelling for the decision maker to understand the reasoning adopted for the analyzes carried out.

Code execution procedure:

  1. Place the files available on the link: https://drive.google.com/drive/folders/1ioYOrQobxsGSC-m2V2fJslcALCh2eFnN. Inside the “data” folder next to the “clean” folder.
  
  2. Run the data_clean.py file. The execution time of this file is long, due to a function that transforms the latitudes and longitudes in a column with the neighborhood of the properties. For testing purposes I suggest reducing the size of the dataframes. Three new dataframes will be generated inside the “data/clean” folder. (df_details.csv, df_merge.csv and df_vivareal.csv)
  
  3. Run the files questionone.py, questionfour.py and questionfive.py. Regardless of the order between them, but they must be executed after the data_clean.py file.

The third step serves only to generate the information (graphs and tables) found in the real_estate_consulting_report.pdf file.

It is worth noting that the files contained in the 'data/clean' folder are the result of the data_clean.py file. And the files inside the 'data/clean/one' and 'data/clean/five' folders are the result of the questionone.py and questionfive.py files, respectively.
