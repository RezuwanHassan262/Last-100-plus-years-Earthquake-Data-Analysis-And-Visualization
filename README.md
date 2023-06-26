# Last-100-years-Earthquake-Data-Analysis
Here, I did some data analysis using the last 100+ years of Earthquake data covering South Asia and Bangladesh region

This was a web scraping project along with dashboard visualization on Tableau.

I scraped and extracted data from a website using Python with the help of request and BeautifulSoup libraries.
The source of the data was this [website](https://www.volcanodiscovery.com/earthquakes/bangladesh/largest.html).

This project aimed to scrape and extract data for data analysis on Earthquake data encompassing Bangladesh and other neighboring countries like India, Myanmar & Nepal. This analysis was done to get insights into the data like the magnitudes of the Earthquakes that took place over the last few years, where, occurred mostly in which month and in which region, and more.
The insights from the extracted data were later visualized using the popular data visualization tool, Tableau.


Here's the link to the Tableau Dashboard for the scraped data: Earthquake Data Tableau Dashboard [14 Sheets & 8 Dashboards](https://public.tableau.com/app/profile/md.reuzwan.hassan/viz/Last100yearsEarthquakeData-Analysis/TotalEarthquakeinBangladeshIndiaNepalMyanmarBINMsub-regionMap)


## CSV File (Data Example):

| Serial        | Date           | Day    | Month  | Year        | Time (GMT)	  | Latitude (N)  | Longitude (E) | Magnitude  | Location                           | Country              |
| ------------- |:--------------:|:-------|:------:|:-----------:|:------------:|:-------------:|:-------------:|:----------:|:----------------------------------:| --------------------:|	
| 0             |Nov 25, 2021	   |25      |November|2021	       |23:45         |22.81          |	93.5248       |6.2         |Myanmar (Burma): 19 Km SW of Falam	| Myanmar              |
| 1             |Apr 28, 2021	   |28      |April   |2021	       |2:24          |26.75          |	92.42         |6           |Northeastern India                	| India                |
| 2             |Oct 10, 2020	   |10      |October |2020	       |17:38	        |24.56	        |93.58	        |5.4	       |Myanmar-India Border Region	        |Myanmar-India Border  |
| 3	            |Aug 30, 2020	   |30      |August	 |2020	       |1:47	        |23.4098	      |92.0087	      |5.1	       |33 Km N of Khagrachhari	            |Bangladesh            |
| 4             |Aug 27, 2020	   |27      |August	 |2020	       |12:07         |23.06          |93.29          |5.3         |Myanmar-India Border Region         |Myanmar-India Border  |
| 5             |Jun 21, 2020	   |21      |June    |2020         |22:40         |23.15          |93.32          |5.5         |Myanmar-India Border Region	        |Myanmar-India Border  |


## Findings and Observations from the Dashboard

1. The highest recorded earthquake in the last hundred-plus years in this Bangladesh-India-Nepal_Myanmar region was 7.2 in magnitude on 8th July, 1918. It took place in Bangladesh.
2. The lowest recorded earthquake in the last hundred-plus years in this Bangladesh-India-Nepal_Myanmar region was 5 in magnitude which took place in multiple regions of BINM, But mostly in India and India-Bangladesh border.
3. Lowest Earthquake that took place in the last hundred years was 7.2 magnitudes in Bangladesh
4. No Earthquake ever took place in October in Bangladesh
5. Premier League of England had the most business in this transfer window with 138 incomings averaging transfer fee €21.98m per player and €3.3b in total.
6. The players age has relation with their transfer fee, market value and their movement in the market. Players within the age of (21-25) have the most demand.
7. The most popular position were Center Forward with 386 total bought of this position. 2nd were Center Back.
8. In terms of nationality Latin American players were very demanding in this transfer window. Brazil had 97 players in the transfer window signing for various clubs.
9. Europes top 5 league had two signings that stood out from the rest of them in the scatterplot. Erling Haaland (As a bargain €90m less than the market price) and Enzo Fernandez (Most overpaid with €66m paid more than the market price).


