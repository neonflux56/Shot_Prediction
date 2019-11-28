## NBA Shot Analysis

**TO DO**
1. Shot prediction task - Will the player make his shot based on some features (Deep learning model + Logistic Regression model)
2. Shot prediction task - More evaluation using various metrics and explanations regarding which metrics were better
3. Recommendation task - Who is the best defender against a certain player(Recommend the best defender on any particular player. Choose a player, check stats of player against that defender and suggest best defenders based on position.)

**UNDER PROGRESS**


**COMPLETED**
1. Test the hot hand hypothesis, does a player’s shooting percentage improve as they make more and more shots. Generated plots for the 17 players with the best hot hands.
2. Test the hypothesis of the clutch gene, is it true some players are significantly better than others at scoring, in terms of points and efficiency in end of game situations

**DATA**
1. shot_logs_assignment.csv contains the latest dataset with data being used for all tasks
Started by first creating a folder and downloading the two datasets into it
Players_1.csv  - That all personal information regarding the player - name, age, college etc etc
Shot_logs.csv - Main dataset that contains every shot attempted over the course of the 2014-15 NBA season(Last two months missing). 

**USEFUL STATISTICS REGARDING THE DATA**
1. 281 offensive players only in total
2. Some major players don't contain shot logs corresponding to them. Games start from novemeber goes through march.


**USEFUL LINKS AND RESOURCES**
1. https://www.kaggle.com/drgilermo/the-fear-factor
2. https://www.kaggle.com/jasonatthinkful/analysis-of-the-hot-hand-phenomenon

**REPORT**
1. Initial Hypotheses: Assumptions about the NBA regarding players that we plan to test 
2. Literature Review: Need to find potential papers discussing this(unlikely) or other more professional blog posts/kagglers
3. Data collection and cleaning : Explanation of the two datasets, what all we are doing to combine the two datasets and make certain columns more easily accessible as features in the data
4. Plots/Analysis of the data
5. Models made using the data
6. Evaluations of the model using various metrics
7. Conclusions of hypotheses
