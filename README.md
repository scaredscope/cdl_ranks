# CoD Team Ranking System

## Elo Summary
The difference in the ratings between two players serves as a predictor of the outcome of a match.
Two players with equal ratings who play against each other are expected to score an equal number of wins.
A player whose rating is 100 points greater than his (or her) opponent's is expected to score 64%,
if the difference is 200 points, then the expected score for the stronger player is 76%.

A player's Elo rating is represented by a number which increases or decreases depending on the outcome of games between rated players.
After every game, the winning player takes points from the losing one.
The difference between the ratings of the winner and loser determines the total number of points gained or lost after a game.
In a series of games between a high-rated player and a low-rated player, the high-rated player is expected to score more wins.
If the high-rated player wins, then only a few rating points will be taken from the low-rated player.
However, if the lower-rated player scores an upset win, many rating points will be transferred.
The lower-rated player will also gain a few points from the higher rated player in the event of a draw.
This means that this rating system is self-correcting. Players whose ratings are too low should, in the long run,
do better than the rating system predicts and thus gain rating points until the ratings reflect their true playing strength

## Glicko Summary
Glickman's principal contribution to measurement is "ratings reliability", called RD, for ratings deviation.

The RD measures the accuracy of a player's rating, with one RD being equal to one standard deviation.
For example, a player with a rating of 1500 and an RD of 50 has a real strength between 1400 and 1600
(two standard deviations from 1500) with 95% confidence. Twice the RD is added and subtracted from their
rating to calculate this range. After a game, the amount the rating changes depends on the RD: the change
is smaller when the player's RD is low (since their rating is already considered accurate), and also when
their opponent's RD is high (since the opponent's true rating is not well known, so little information is
being gained). The RD itself decreases after playing a game, but it will increase slowly over time of inactivity.


## Our Contribution 
Our goal is to implement a live system that would rate player and team performance throughout tournaments and leagues.
The Elo and Glicko rating systems both had shortcomings when it came to representing live performance ratings
of players in a game such as Call of Duty. So there the task began, to create an accurate, live, team based rating system.

First, analyzing Elo. The way this rating system works is that two players have a certain amount of point
typically between 0 and 3000. If one player beats another then they take a certain amount of points from that
player depending on the rating difference. For example if a 1600 rated player beats a 1500 rated player they’ll
take away some arbitrary number, let's say 30. The new ratings would be 1470, and 1630 respectively.
The problem with this is that ratings move too fast and a players can exploint or ‘farm’ wins off lower rated players for easy points.
Elo is fast an easy to do with a calculator and a pencil and but many of the numbers used are completely arbitrary and have no meaning.

Secondly, Glicko, a rating system from the 90’s, uses a different more complex system of ratings and deviations.
Similar to how the bell curve function of IQ behaves. Glicko represents players and calculates ratings
by factoring in confidence intervals. A new player may have a rating of 1500, but because they’ve never
played before their confidence interval would be very wide. For example, a player with a rating of 1500
and an RD of 100 has a real strength between 1300 and 1700 (two standard deviations from 1500) with 95% confidence.
Whereas a player who has played hundreds of games May have an RD of 30. Overall Glicko has been a huge improvement
over the Elo system, but there were still some shortcomings that can be broken down into three distinct problems:

1. It’s designed to be updated after a large collection of games. 
2. It only calculates ratings for players in 1v1 matchups not those in teams
3. The system can’t take into account the performance (or score) of a team beyond ‘Winning’ or ‘Losing’ a specific match.

### Problem 1 
The most straight forward of all the problems.
In order to have a system that could be applied after every game a bit of maneuvering of the glicko system was required.
Unrolling summations removed iterative steps used for calculating the multiple games, essentially transforming it to
update scores after only 1 game. This was a key part in creating a ‘Live’ rating system that I wanted for the users.

### Problem 2
Loop through the two teams and save each players rankings using the average Rating and Rating Deviation of the other team.
Then when done using these saved rankings and update each player. This Fix only matters when players are moving around to 
different teams all the time. In scenarios where players play for the same team for long periods of time this addition is not neccessary

### Problem 3
The Cumulative distribution function of binomial probability.
Problem was the function wasn’t solved for the right variable...
