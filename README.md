# surfs_up

## Purpose
W.Avy is planning to open a surf and ice cream shope in Oahu. However, he would like more temperature data for the months of June and Decemeber in Oahu before he makes his final decision.

## Overview

- Temperature statistics for June.

- Temperature statistics for December.

## Analysis

The data provided to us is in sqlite format. For us to read the data, we would need to create an engine with sqlalchemy and then reflect the database. After that we would need to createa a session for our engine in order to query for our data.

![des](https://github.com/QQrex/surfs_up/blob/main/Resources/Dep%2C%20engine%2C%20session.PNG)
> Cell 1 - Import depedencies.
> 
> Cell 2 - Create engine and reflect database.
> 
> Cell 3 - Create a session to our database.

[June]

Next, we will import the extract method from sqlalchemy to filter for the month of June from our data.

![tfj](https://github.com/QQrex/surfs_up/blob/main/Resources/temp%20from%20june.PNG)

Once we have queried for our June data, we will need to create a June DataFrame using pandas.

![junedf](https://github.com/QQrex/surfs_up/blob/main/Resources/june%20df.PNG)

Finally, to get that temperature statistics for June, we can simply just use the .describe() method on our June DataFrame.

![junestats](https://github.com/QQrex/surfs_up/blob/main/Resources/June%20stats.PNG)

[December]

For the month of December we will extract the data like we did for June.

![tfd](https://github.com/QQrex/surfs_up/blob/main/Resources/temp%20for%20dec.PNG)

Load the data into a DataFrame.

![decdf](https://github.com/QQrex/surfs_up/blob/main/Resources/dec%20df.PNG)

Use .describe() to get the statistics for Decemeber.

![decstats](https://github.com/QQrex/surfs_up/blob/main/Resources/dec%20stats.PNG)

## Results

- Average temperature in June are in the mid 70s.
- 
- Average temperature in December are in the low 70s.
- 
- Decemeber may also experience temperatures as high 50s to low 60s.

## Summary

Looking at the statisical break down of June and Decemeber, we may want to advise W. Avy his surf and ice cream shop may experience lower customers due to slightly lower temperatures. However, to fully understand the extent of slow business during winter, we may want to look at average temperature during all the winter months (Nov, Dec, Jan and Feb), before he makes a decision if it is a good idea to open a surf and ice cream shop year round. In addition to temperature, it may be wise to look at statistical precipitation data for the winter months as well.
