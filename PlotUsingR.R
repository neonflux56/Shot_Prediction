
library(tidyverse)

shotlogs <- read.csv("shot_logs_assignment.csv")


shotlogs <- shotlogs %>%
  mutate(Shot_made = ifelse(SHOT_RESULT == "made",1,0))

test <- shotlogs %>%
  filter(PERIOD == 4) %>%
  group_by(player_id,player_name) %>%
  summarise(Shotsmade_proportion = sum(Shot_made)/n()) %>%
  arrange(desc(Shotsmade_proportion)) 
test <- cbind(test, rank = as.vector(seq(1,length(test$Shotsmade_proportion),1)))
Plot1 <- test %>%  
  filter(rank <= 10) %>%
  ggplot(aes(x = player_name, y = Shotsmade_proportion)) + geom_point() + labs(x = "Player",title = "Top 10 performing players in the last 12 minutes",y = "Proportion of shots on target" )


Plot1 + theme(axis.text.x = element_text(face = "bold", color = "#993333", hjust = 1,
                                             size = 8, angle = 45))




test <- shotlogs %>%
  filter(PERIOD == 1) %>%
  group_by(player_id,player_name) %>%
  summarise(Shotsmade_proportion = sum(Shot_made)/n()) %>%
  arrange(desc(Shotsmade_proportion)) 
test <- cbind(test, rank = as.vector(seq(1,length(test$Shotsmade_proportion),1)))
Plot2 <- test %>%  
  filter(rank <= 10) %>%
  ggplot(aes(x = player_name, y = Shotsmade_proportion)) + geom_point() + labs(x = "Player",title = "Top 10 performing players in the first 12 minutes",y = "Proportion of shots on target" )


Plot2 + theme(axis.text.x = element_text(face = "bold", color = "#993333", hjust = 1,
                                         size = 8, angle = 45))

