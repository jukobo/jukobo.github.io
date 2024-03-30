*Updated: {% assign copenhagen_time = site.time | date: "%d-%m-%Y %H:%M:%S" | date: "%s" | plus: 3600 | date: "%d-%m-%Y %H:%M:%S" %}{{ copenhagen_time }}*


__Introduction (I)__\
The data that we are working with in this project is *Police Department Incident Reports: Historical 2003 to May 2018*, which is provided by the City and County of San Francisco. The data is about historical reported crimes in San Francisco. It contains 35 columns, each providing essential infomation about the observation, such as time, position and categori of the crime. In this project, we will be focusing on the crime category prostitution and explore how this crime has developed over time and in the different districts of San Francisco. We will only examine data from January 1st, 2003, to December 31st, 2017.


__Trends and patterns of prostitution incidents (II)__\
_Short intro_

![One time-series / bar chart](/A2/plot1.png)
_Figure 1: Illustration of the distribution of time and days across the years of reported prostitution incidents._

In the first plot of the subplot in _figure 1_, a comprehensive overview of the crime trend from 2003 to 2017 is presented. It can be seen, that the prostitution rate peaked in 2003 and again in 2007, from where it steadily declined until 2015.\
Looking closer at the subplot, Thursdays emerged as the day with the highest frequency of crimes, totaling 3630 incidents, whereas Sundays witnessed the fewest, with only 1059 reported crimes, see table 1.

| Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday |
|--------|---------|-----------|----------|--------|----------|--------|
|  1123  |   3003  | 3291      | 3630     | 2776   | 1571     | 1059   |

_Table 1: Total amount of prostitution crimes on the different weekdays._

The data reveals a varying pattern in prostitution incidents over the years. Initially, there is a relatively low frequency of such offenses on Saturdays during the first four years. However, a significant increase is observed in 2007 and 2008, with peak levels reached in 2014, before returning to levels akin to those seen between 2003 and 2006 by the end of the period.\
Interestingly, weekdays, particularly Tuesday, Wednesday, and Thursday, presented disproportionately high numbers of prostitution-related incidents. In 2016, a conspicuous shift is observed, with Thursday emerging as the predominant weekday for criminal activities, marking a more dominant departure from previous patterns.

The second subplot in _figure 1_ shows a distinct pattern regarding the timing of the prostitution crimes during the days of the week. 
The data illustrates that prostitution incidents are most prevalent around midnight and during the late night hours, suggesting a correlation between the cover of overnighting out of town and the occurrence of such offenses. Conversely, there is a notable decrease in incidents during the morning and daytime hours.\
A noteworthy observation is the apparent increase in crimes during the weekend compared to weekdays, which contrasts with the findings of the first plot. However, upon closer examination and check with table 1, it becomes evident that this apparent discrepancy is not accurate.


__Geographical analysis of reported prostitution incidents (III)__
"Now that we have gained a better understanding of the distribution and trends of reported prostitution incidents, it would be interesting to see in which districts these incidents occur.
The plot to the left shows that the region park is the district with the least reported cases of prostitution as there only have been recorded 18 cases. Mission is the region where the highest number of reported cases of prostitution as 2773 cases have been reported here. It is however necessary to keep in mind that these number tells nothing of the density of the crime.

As Mission is a larger region than Tenderloin it is fair to assume that more more people live here. According to [THE STANDARD BASED ON THE CITY OF SF’S ANALYSIS NEIGHBORHOODS], there is an estimated 103.059 population in the district Mission. Please note that this source divides SF into 41 regions, so our estimate for the population of the district Mission, is the sum of the population of three districts, which all together cover the district Mission. The district Tenderloin has an estimated population of 31.118 citizens. Sunset/Parkside (which is a subdistrict of TARAVAL) is the most populous neighbourhood in the city with a population of 81.209 citizens.

To give a better answer to which districts troubles the most with prostitution, one could look at the reported incident relative to either the number of citizens or area of the district to create a better basis of comparison.

As the data presented by THE STANDARD used another division of the map, the data is not directly compatible with the SF crime data we have been provided with. We have therefore calculated the area of each district given the longitude and latitude of points surounding each district. Firstly the longitude and the latitude where converted to Cartesian coordinates, whereafter the shoelace formula to calculate the area of the polygon was applied. It would be better to calculate the density of the crime based on the number of citizens, as assuming that the population density over all distances is equal is a misleading assumption.

The plot to the right shows the rate of reported cases of prostitution per $'km^2'$ of each district. Here it is seen that Tenderloin now has a higher rate of reported cases of prostitution per $km^2$ than Mission. This shows that Tenderloin is the district that was troubled the most with prostitution when looking at reported cases of prostitution per area. 

[THE STANDARD BASED ON THE CITY OF SF’S ANALYSIS NEIGHBORHOODS]: https://sfstandard.com/2022/12/08/san-francisco-neighborhood-new-census-data-maps/

<div style="display: flex; justify-content: space-between;">
    <div>
        <embed 
                     type="text/html" 
                     src="/A2/plot21.html"
                     width="550"
                     height="600"
                     >
    </div>
    <div>
        <embed 
                     type="text/html" 
                     src="/A2/plot22.html"
                     width="550"
                     height="600"
                     >
    </div>
</div>
_Figure 2: Overview of Reported Prostitution Cases by Districts_


__Insights into Prostitution Incident Patterns Across San Francisco Districts (IV)__

Finally, to gain a better insight into prostitution in each of San Francisco's police districts, we have created a jitter plot illustrating prostitution incidents, see _figure 3_. Each point represents an incident over the 14 years, with the x-axis showing the time of occurrence and the y-axis indicating the day of the week. These plots provide us with an understanding of trends and variations over time and across different districts. Additionally, a legend on the right side of the plot assists in identifying the police districts represented by different colors.

<embed 
       type="text/html" 
       src="/bokeh_prostitution.html"
       width="1100"
       height="350">
_Figure 3: Jitterplot over the prostitution incidents for each police department._

Looking at the different districts, we observe that there are clearly more incidents during the evening and night hours compared to the daytime in most districts. Additionally, we notice a distinct pattern where weekdays, particularly Tuesday, Wednesday, and Thursday, has the highest density of incidents. These observations are just like those found in the first figure above, but here we see that almost each district also has this distribution. It can therefore be concluded that it is not an outlier responsible for the overall distribution, but a tendency for all districts.

When examining each district individually, it becomes evident that Mission, Northern, and Tenderloin are among the districts with the highest number of incidents, while the Park district has so few that they can be easily counted.

Furthermore, it is apparent that in some of the districts, a significant number of incidents occur around 12:00, as seen in Taraval. This could be attributed to a delay in reporting, where cases are collected over time and eventually logged into the system all at once at noon. This results in an incorrect pattern in the data and can be considered a human error.



__Contributions of the group members__

| Part | s214704 | s214725 | s204112 |
|------|---------|---------|---------|
| I    | 33%     | 33%     | 33%     |
| II   | 40%     | 30%     | 30%     |
| III  | 30%     | 30%     | 40%     |
| IV   | 30%     | 40%     | 30%     |
