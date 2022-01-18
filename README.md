# Dogecoin Project
### Pellissippi State High School Coding Competition
### Objective: Create an application that predicts the price of Dogecoin (DOGE)

## Participants
Farragut High School Team 3- Ivy Enyenihi, Grace Feng, Ridhima Singh, Tom Williamson

## Data
* Dogecoin hisorical prices: https://finance.yahoo.com/quote/DOGE-USD/history?p=DOGE-USD
* Prediction model: https://www.youtube.com/watch?v=d5oT8KeGouw

## Prediction Model
To create our project, we used Facebook prophet, which has a fit method that allowed us to make predictions through its API machine learning. We applied this method to the Dogecoin data that contained the opening, closing, high, and lows prices for that day. This was done in Google Colaboratory using Python, and the data from the model was saved and transferred to the user interface developed in Visual Studio Code. 

## User Interface
A user-feiendly interface was developed using Visual Studio Code. Upon being given a starting date in the format YYYY-MM-DD, the program output its projection for Gogecoin values in the week following the date input in the form of a graph. The x-axis represents the days elapsed since the date input, and the y-axis represents the projected value of dogecoin in US Dollars.

# Tweets Analysis
We also found and recorded every instance Elon Musk tweeted and analyzed Dogecoin prices around those days. Although we found that on days Elon Musk tweets, Dogecoin’s opening price the next day falls by $.001 on average, or .1 ¢, this result was not consistent at all every time he tweeted, since it is just an average of all the fluctuations. As a result, since there was no significant effect of Musk’s tweets on the next day’s Dogecoin value, we did not incorporate this portion into our interface.
