
# libs for ROC
library("pROC")
library("ggplot2")
library("car")
library("profileR")
library("dplyr")
library("tidyr")

# libs for logit
library("car")
library("lme4")


# orienting vars
parentDir <- "~/Projects/cal_abstract/"
dataDir <- paste0(parentDir, "pilot_data")
outDir <- parentDir


### --- Step 1: Make data frame
#
# Read each subj data, extract 
#   relevant info, add to master


# start master df
df_master <- as.data.frame(matrix(NA, nrow=1, ncol=11))
colnames(df_master) <- c("Subj","Block","Type","Stim","Corr","Trial","Resp","RT","Succ","TrialType","TrialTypeInt")

# get list of participant data
dataList <- list.files(dataDir, pattern = "*.csv")

# extract relevant data for each participant,
#   write to master
for(dataFile in dataList){
  
  # dataFile <- dataList[1]
  df_raw <- read.delim(paste0(dataDir, "/", dataFile), header = T, sep = ",")
  subj <- gsub("_.*", "", dataFile)
  
  # Get relevant block1 info
  df_block1 <- cbind(
    df_raw$Block1Type, 
    df_raw$Block1Stim, 
    df_raw$Block1Corr, 
    df_raw$Block1_loop.thisN, 
    df_raw$key_resp1.keys,
    df_raw$key_resp1.rt,
    df_raw$key_resp1.corr
  )
  df_block1 <- na.exclude(df_block1)
  df_block1 <- as.data.frame(df_block1)
  colnames(df_block1) <- c("Type","Stim","Corr","Trial","Resp","RT","Succ")
  
  # add trial type counters
  #   so we can compare across trials of 
  #   different conditions
  df_block1$TrialType <- NA
  df_block1$TrialTypeInt <- NA
  ind_f1 <- which(df_block1$Type == "Fix1")
  ind_f2 <- which(df_block1$Type == "Fix2")
  ind_c <- which(df_block1$Type == "Cond")
  for(ind in 1:length(ind_f1)){
    df_block1[ind_f1[ind],]$TrialType <- paste0("Fix1-",ind)
    df_block1[ind_f1[ind],]$TrialTypeInt <- ind
    df_block1[ind_f2[ind],]$TrialType <- paste0("Fix2-",ind)
    df_block1[ind_f2[ind],]$TrialTypeInt <- ind
    df_block1[ind_c[ind],]$TrialType <- paste0("Cond-",ind)
    df_block1[ind_c[ind],]$TrialTypeInt <- ind
  }
  
  # repeat for block2
  df_block2 <- cbind(
    df_raw$Block2Type, 
    df_raw$Block2Stim, 
    df_raw$Block2Corr, 
    df_raw$Block2_loop.thisN, 
    df_raw$key_resp2.keys,
    df_raw$key_resp2.rt,
    df_raw$key_resp2.corr
  )
  df_block2 <- na.exclude(df_block2)
  df_block2 <- as.data.frame(df_block2)
  colnames(df_block2) <- c("Type","Stim","Corr","Trial","Resp","RT","Succ")
  
  df_block2$TrialType <- NA
  df_block2$TrialTypeInt <- NA
  ind_f1 <- which(df_block2$Type == "Fix1")
  ind_f2 <- which(df_block2$Type == "Fix2")
  ind_c <- which(df_block2$Type == "Cond")
  for(ind in 1:length(ind_f1)){
    df_block2[ind_f1[ind],]$TrialType <- paste0("Fix1-",ind)
    df_block2[ind_f1[ind],]$TrialTypeInt <- ind
    df_block2[ind_f2[ind],]$TrialType <- paste0("Fix2-",ind)
    df_block2[ind_f2[ind],]$TrialTypeInt <- ind
    df_block2[ind_c[ind],]$TrialType <- paste0("Cond-",ind)
    df_block2[ind_c[ind],]$TrialTypeInt <- ind
  }
  
  # block3
  df_block3 <- cbind(
    df_raw$Block3Type, 
    df_raw$Block3Stim, 
    df_raw$Block3Corr, 
    df_raw$Block3_loop.thisN, 
    df_raw$key_resp3.keys,
    df_raw$key_resp3.rt,
    df_raw$key_resp3.corr
  )
  df_block3 <- na.exclude(df_block3)
  df_block3 <- as.data.frame(df_block3)
  colnames(df_block3) <- c("Type","Stim","Corr","Trial","Resp","RT","Succ")
  
  df_block3$TrialType <- NA
  df_block3$TrialTypeInt <- NA
  ind_f1 <- which(df_block3$Type == "Fix1")
  ind_f2 <- which(df_block3$Type == "Fix2")
  ind_c <- which(df_block3$Type == "Cond")
  for(ind in 1:length(ind_f1)){
    df_block3[ind_f1[ind],]$TrialType <- paste0("Fix1-",ind)
    df_block3[ind_f1[ind],]$TrialTypeInt <- ind
    df_block3[ind_f2[ind],]$TrialType <- paste0("Fix2-",ind)
    df_block3[ind_f2[ind],]$TrialTypeInt <- ind
    df_block3[ind_c[ind],]$TrialType <- paste0("Cond-",ind)
    df_block3[ind_c[ind],]$TrialTypeInt <- ind
  }

  # make subj data frame
  df_subj <- as.data.frame(matrix(NA,nrow=dim(df_block1)[1]*3, ncol=dim(df_block1)[2]+2))
  colnames(df_subj) <- c("Subj", "Block", colnames(df_block1))
  df_subj$Subj <- subj
  df_subj$Block <- c(rep("Block1", dim(df_block1)[1]), rep("Block2", dim(df_block2)[1]), rep("Block3", dim(df_block3)[1]))
  df_subj[,3:11] <- rbind(df_block1, df_block2, df_block3)
  
  # write to master
  df_master <- rbind(df_master, df_subj)
}

# clean master
df_master <- na.omit(df_master)
row.names(df_master) <- 1:dim(df_master)[1]


### --- Step 2: Logistic Regression
#
# Convert df to proper format,
#   do repeated measures logit.
#
# Plot average probabilities


df_logit <- df_master

# determine location of factors
ind_f1 <- grep("Fix1", df_logit$Type)
ind_f2 <- grep("Fix2", df_logit$Type)
ind_c <- grep("Cond", df_logit$Type)

ind_b1 <- grep("Block1", df_logit$Block)
ind_b2 <- grep("Block2", df_logit$Block)
ind_b3 <- grep("Block3", df_logit$Block)

# make factors
df_logit[ind_f1,]$Type <- 1
df_logit[ind_f2,]$Type <- 2
df_logit[ind_c,]$Type <- 3

df_logit[ind_b1,]$Block <- 1
df_logit[ind_b2,]$Block <- 2
df_logit[ind_b3,]$Block <- 3

# convert to proper format
df_logit$Type <- factor(df_logit$Type)
df_logit$Block <- factor(df_logit$Block)
df_logit$Trial <- as.numeric(df_logit$Trial)
df_logit$Succ <- as.numeric(df_logit$Succ)

# logistic regression 
fit <- glmer(Succ ~ TrialTypeInt + Type*Block + (1|Subj), data=df_logit, family = binomial())
summary(fit)
plot(fit)

# make prediction df for plots
df_pred <- as.data.frame(df_logit[,c(1:3,11)])
df_pred$Preds <- plogis(predict(fit, newdata=df_pred))

# get lists
numSubj <- length(unique(df_pred$Subj))
blockList <- unique(df_pred$Block)
typeList <- unique(df_pred$Type)
trialList <- unique(df_pred$TrialTypeInt)

# make plotable df with average proportions
#   long form
df_plot <- as.data.frame(matrix(NA,nrow=dim(df_pred)[1]/numSubj,ncol=4))
colnames(df_plot) <- c("Block", "Type", "Trial", "Prob")
df_plot$Block <- c(rep("Block1",length(trialList)*length(typeList)), rep("Block2",length(trialList)*length(typeList)), rep("Block3",length(trialList)*length(typeList)))
df_plot$Type <- c(rep(c(rep("Fix1",length(trialList)), rep("Fix2",length(trialList)), rep("Cond",length(trialList))),length(blockList)))
df_plot$Trial <- c(rep(1:length(trialList), length(blockList) * length(typeList)))

for(block in blockList){
  for(type in typeList){
    
    if(type == 1){
      h_type <- "Fix1"
    }else if(type == 2){
      h_type <- "Fix2"
    }else if(type == 3){
     h_type <- "Cond" 
    }
    
    for(trial in trialList){
      
      # find locations of desired predictions, location
      #   of output, and pull mean
      ind_src <- which(df_pred$Block == block & df_pred$Type == type & df_pred$TrialTypeInt == trial)
      ind_out <- which(df_plot$Block == paste0("Block",block) & df_plot$Type == h_type & df_plot$Trial == trial)
      df_plot[ind_out,]$Prob <- round(mean(df_pred[ind_src,]$Preds),4)
    }
  }
}


# plots
ggplot(df_plot[which(df_plot$Block == "Block1"),]) +
  geom_line(aes(x=Trial, y=Prob, colour = Type, group = Type)) +
  geom_point(mapping = aes(x=Trial, y=Prob, color=Type),size=0.3) +
  ggtitle("Learning Curve: Block1")

ggplot(df_plot[which(df_plot$Block == "Block2"),]) +
  geom_line(aes(x=Trial, y=Prob, colour = Type, group = Type)) +
  geom_point(mapping = aes(x=Trial, y=Prob, color=Type),size=0.3) +
  ggtitle("Learning Curve: Block2")

ggplot(df_plot[which(df_plot$Block == "Block3"),]) +
  geom_line(aes(x=Trial, y=Prob, colour = Type, group = Type)) +
  geom_point(mapping = aes(x=Trial, y=Prob, color=Type),size=0.3) +
  ggtitle("Learning Curve: Block3")


### --- Step 3: ROC curves
#
# Plot distribution of AUCs
#
# Make ROC curves for type


df_roc <- df_master

# get lists
subjList <- unique(df_roc$Subj)
blockList <- unique(df_roc$Block)
typeList <- sort(unique(df_roc$Type))

# start long auc df
df_auc <- as.data.frame(matrix(NA,nrow=length(subjList)*length(blockList)*length(typeList),ncol=4))
colnames(df_auc) <- c("Subj", "Block", "Type", "AUC")
df_auc$Subj <- rep(subjList, length(blockList)*length(typeList))
df_auc$Block <- c(rep("Block1", length(subjList)*length(typeList)), rep("Block2", length(subjList)*length(typeList)), rep("Block3", length(subjList)*length(typeList)))
df_auc$Type <- c(rep(c(rep("Fix1", length(subjList)), rep("Fix2", length(subjList)), rep("Cond", length(subjList))), length(blockList)))

# get AUC for e/subj/block/type
for(type in typeList){
  for(block in blockList){
    for(subj in subjList){
      
      # subset data
      h_df <- df_roc[which(df_roc$Subj == subj & df_roc$Type == type & df_roc$Block == block),]
      
      # account for perfect performance,
      #   how do they even?!
      if(length(unique(h_df$Succ)) == 1){
        h_df[1,]$Succ <- 0
      }
      
      # get AUC
      h_roc <- roc(h_df$Succ, h_df$TrialTypeInt)
      h_auc <- round(auc(h_roc),4)
      
      # find row, write auc
      h_ind <- which(df_auc$Subj == subj & df_auc$Block == block & df_auc$Type == type)
      df_auc[h_ind,]$AUC <- h_auc
    }
  }
}

# plot
ee <- ggplot(df_auc, aes(x = Block, y = AUC))
ee2 <- ee+geom_boxplot(aes(fill=Type))
ee2 + facet_wrap(~Type)


# ROC: Fix1
type <- "Fix1"
df_type_b1 <- df_roc[which(df_roc$Block == "Block1" & df_roc$Type == type),]
df_type_b2 <- df_roc[which(df_roc$Block == "Block2" & df_roc$Type == type),]
df_type_b3 <- df_roc[which(df_roc$Block == "Block3" & df_roc$Type == type),]

roc_b1 <- roc(df_type_b1$Succ, df_type_b1$TrialTypeInt)
roc_b2 <- roc(df_type_b2$Succ, df_type_b2$TrialTypeInt)
roc_b3 <- roc(df_type_b3$Succ, df_type_b3$TrialTypeInt)

e <- ggroc(list(block1=roc_b1, block2=roc_b2, block3=roc_b3)) + ggtitle(paste0("ROC: ",type))
e1 <- e + xlab("FPR") + ylab("TPR")
e1

# ROC: Fix2
type <- "Fix2"
df_type_b1 <- df_roc[which(df_roc$Block == "Block1" & df_roc$Type == type),]
df_type_b2 <- df_roc[which(df_roc$Block == "Block2" & df_roc$Type == type),]
df_type_b3 <- df_roc[which(df_roc$Block == "Block3" & df_roc$Type == type),]

roc_b1 <- roc(df_type_b1$Succ, df_type_b1$TrialTypeInt)
roc_b2 <- roc(df_type_b2$Succ, df_type_b2$TrialTypeInt)
roc_b3 <- roc(df_type_b3$Succ, df_type_b3$TrialTypeInt)

e <- ggroc(list(block1=roc_b1, block2=roc_b2, block3=roc_b3)) + ggtitle(paste0("ROC: ",type))
e1 <- e + xlab("FPR") + ylab("TPR")
e1

# ROC: Cond
type <- "Cond"
df_type_b1 <- df_roc[which(df_roc$Block == "Block1" & df_roc$Type == type),]
df_type_b2 <- df_roc[which(df_roc$Block == "Block2" & df_roc$Type == type),]
df_type_b3 <- df_roc[which(df_roc$Block == "Block3" & df_roc$Type == type),]

roc_b1 <- roc(df_type_b1$Succ, df_type_b1$TrialTypeInt)
roc_b2 <- roc(df_type_b2$Succ, df_type_b2$TrialTypeInt)
roc_b3 <- roc(df_type_b3$Succ, df_type_b3$TrialTypeInt)

e <- ggroc(list(block1=roc_b1, block2=roc_b2, block3=roc_b3)) + ggtitle(paste0("ROC: ",type))
e1 <- e + xlab("FPR") + ylab("TPR")
e1



