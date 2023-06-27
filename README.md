# Last 100+ years Bangladesh-India-Nepal-Myanmar(BINM) region's Earthquake Data Analysis
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
2. The lowest recorded earthquake in the last hundred-plus years in this Bangladesh-India-Nepal_Myanmar region was 5 in magnitude which took place in multiple regions of BINM, But mostly in India and India-Bangladesh border region.
3. The greatest number of earthqquakes took place in India (49 in total)
4. The lowest number of earthquakes took place in Bhutan and MyanmarBangladesh border region (Both 1).
5. In the Bangladesh region, There were respectively 22, 7, & 1 earthquakes in Bangladesh-India border region, bangladesh and Bangladesh-Myanmar border region.
6. In BINM region, earthquakes mostly took place in February, September & December. All 7 in number and all in India.
7. In Bangladesh region, earthquakes mostly took place in November in India-Bangladesh border region. 4 in quantity.
8. In BINM region, maximum number of earthquakes took place in November. 13 in total.
9. In Bangladesh region, maximum number of earthquakes took place in July & November Both 5 in quantity.
10. In BINM region, Earthquakes mostly took place around 20.00 GMT, All in India.
11. In Bangladesh region, Earthquakes mostly took place around 7.00 GMT & 11.00 GMt, All in India-Bangladesh border region.
12. In BINM region, Earthquakes mostly took place in 2nd day of the month, 6 in total.
13. In Bangladesh region, Earthquakes mostly took place in 7th day of the month, 3 in total.
14. Location-wise, In BINM region Earthquakes mostly took place in India-Bangladesh border region (22), then Assam (21) and then Myanmar-India border region (17).
15. Country-wise, In the BINM region, The name of the countries and the number of total earthquakes since 1918 are India (49), Myanmar (14), Bangladesh (7) & Bhutan (1).
