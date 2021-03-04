
# libs for ROC
library("pROC")
library("ggplot2")
library("car")
library("profileR")
library("dplyr")
library("tidyr")

# libs for logit
library("lme4")


# orienting vars
parentDir <- "~/Projects/cal_abstract/"
dataDir <- paste0(parentDir, "pilot_data/")
outDir <- paste0(parentDir, "analyses/")



### --- Step 1: Make data frame
#
# Read each subj data, extract 
#   relevant info, add to master
#
# Writes analyses/Master_dataframe.csv

func_makeDF <- function(){
  
  # start master df
  df_master <- as.data.frame(matrix(NA, nrow=1, ncol=11))
  colnames(df_master) <- c("Subj","Block","Type","Stim","Corr","Trial","Resp","RT","Succ","TrialType","TrialTypeInt")
  
  # get list of participant data
  dataList <- list.files(dataDir, pattern = "*.csv")
  
  # extract relevant data for each participant,
  #   write to master
  for(dataFile in dataList){
    
    # dataFile <- dataList[1]
    df_raw <- read.delim(paste0(dataDir, dataFile), header = T, sep = ",")
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
    df_subj$Block <- c(
      rep("Block1", dim(df_block1)[1]), 
      rep("Block2", dim(df_block2)[1]), 
      rep("Block3", dim(df_block3)[1]))
    df_subj[,3:11] <- rbind(df_block1, df_block2, df_block3)
    
    # write to master
    df_master <- rbind(df_master, df_subj)
  }
  
  # clean master
  df_master <- na.omit(df_master)
  row.names(df_master) <- 1:dim(df_master)[1]
  
  # write master
  writeOut <- paste0(outDir, "Master_dataframe.csv")
  write.csv(df_master, file=writeOut, quote=F, row.names = F)
}
func_makeDF()



### --- Step 2: Logistic Regression
#
# Convert df to proper format,
#   do repeated measures logit.
#
# Plot average probabilities
#
# Write analyses/Stats_logit.txt
#
# TODO: update to write out graphs to analyses
#   does df_pred$Preds <- plogis(predict(fit, newdata=df_pred)) need type=response?

func_doLogit <- function(){
  
  df_all <- read.csv(paste0(outDir, "Master_dataframe.csv"))
  
  # determine location of factors
  ind_f1 <- grep("Fix1", df_all$Type)
  ind_f2 <- grep("Fix2", df_all$Type)
  ind_c <- grep("Cond", df_all$Type)
  
  ind_b1 <- grep("Block1", df_all$Block)
  ind_b2 <- grep("Block2", df_all$Block)
  ind_b3 <- grep("Block3", df_all$Block)
  
  # make factors
  df_all[ind_f1,]$Type <- 1
  df_all[ind_f2,]$Type <- 2
  df_all[ind_c,]$Type <- 3
  
  df_all[ind_b1,]$Block <- 1
  df_all[ind_b2,]$Block <- 2
  df_all[ind_b3,]$Block <- 3
  
  # convert to proper format
  df_all$Type <- factor(df_all$Type)
  df_all$Block <- factor(df_all$Block)
  df_all$Trial <- as.numeric(df_all$Trial)
  df_all$Succ <- as.numeric(df_all$Succ)
  
  # logistic regression 
  fit <- glmer(Succ ~ TrialTypeInt + Type*Block + (1|Subj), data=df_all, family = binomial())
  # summary(fit)
  outFile <- paste0(outDir, "Stats_logit.txt")
  capture.output(summary(fit), file = outFile)

  # make prediction df for plots
  df_pred <- as.data.frame(df_all[,c(1:3,11)])
  # df_pred$Preds <- plogis(predict(fit, newdata=df_pred))
  df_pred$Preds <- plogis(predict(fit, newdata=df_pred, type="response"))
  
  # get lists
  numSubj <- length(unique(df_pred$Subj))
  blockList <- unique(df_pred$Block)
  typeList <- unique(df_pred$Type)
  trialList <- unique(df_pred$TrialTypeInt)
  
  # make plotable df with average proportions
  #   long form
  df_plot <- as.data.frame(matrix(NA,nrow=dim(df_pred)[1]/numSubj,ncol=4))
  colnames(df_plot) <- c("Block", "Type", "Trial", "Prob")
  
  df_plot$Block <- c(
    rep("Block1",length(trialList)*length(typeList)), 
    rep("Block2",length(trialList)*length(typeList)), 
    rep("Block3",length(trialList)*length(typeList)))
  
  df_plot$Type <- c(
    rep(c(
      rep("Fix1",length(trialList)), 
      rep("Fix2",length(trialList)), 
      rep("Cond",length(trialList))),
      length(blockList)))
  
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
      
      # find locations of desired predictions, location
      #   of output, and pull mean
      for(trial in trialList){
        ind_src <- which(df_pred$Block == block & df_pred$Type == type & df_pred$TrialTypeInt == trial)
        ind_out <- which(
          df_plot$Block == paste0("Block",block) & 
          df_plot$Type == h_type & 
          df_plot$Trial == trial)
        df_plot[ind_out,]$Prob <- round(mean(df_pred[ind_src,]$Preds),4)
      }
    }
  }
  return(df_plot)
}
df_plot <- func_doLogit()

# plots
ggplot(df_plot[which(df_plot$Block == "Block1"),]) +
  geom_line(aes(x=Trial, y=Prob, colour = Type, group = Type)) +
  geom_point(mapping = aes(x=Trial, y=Prob, color=Type),size=0.3) +
  ggtitle("Learning Curves for Block1 Trial Types")

ggplot(df_plot[which(df_plot$Block == "Block2"),]) +
  geom_line(aes(x=Trial, y=Prob, colour = Type, group = Type)) +
  geom_point(mapping = aes(x=Trial, y=Prob, color=Type),size=0.3) +
  ggtitle("Learning Curves for Block2 Trial Types")

ggplot(df_plot[which(df_plot$Block == "Block3"),]) +
  geom_line(aes(x=Trial, y=Prob, colour = Type, group = Type)) +
  geom_point(mapping = aes(x=Trial, y=Prob, color=Type),size=0.3) +
  ggtitle("Learning Curves for Block3 Trial Types")



### --- Step 3: AUC curves
#
# Plot distribution of AUCs
#
# Writes analyses/Table_AUC.csv

func_auc <- function(){
  
  df_all <- read.csv(paste0(outDir, "Master_dataframe.csv"))
  
  # get lists
  subjList <- unique(df_all$Subj)
  blockList <- unique(df_all$Block)
  typeList <- sort(unique(df_all$Type))
  
  # start long auc df
  df_auc <- as.data.frame(matrix(NA,nrow=length(subjList)*length(blockList)*length(typeList),ncol=4))
  colnames(df_auc) <- c("Subj", "Block", "Type", "AUC")
  
  df_auc$Subj <- rep(subjList, length(blockList)*length(typeList))
  
  df_auc$Block <- c(
    rep("Block1", length(subjList)*length(typeList)), 
    rep("Block2", length(subjList)*length(typeList)), 
    rep("Block3", length(subjList)*length(typeList)))
  
  df_auc$Type <- c(
    rep(c(
      rep("Fix1", length(subjList)), 
      rep("Fix2", length(subjList)), 
      rep("Cond", length(subjList))), 
      length(blockList)))
  
  # get AUC for e/subj/block/type
  for(type in typeList){
    for(block in blockList){
      for(subj in subjList){
        
        # subset data
        h_df <- df_all[which(df_all$Subj == subj & df_all$Type == type & df_all$Block == block),]
        
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
  
  # write
  writeOut <- paste0(outDir, "Table_AUC.csv")
  write.csv(df_auc, file=writeOut, quote=F, row.names = F)
  return(df_auc)
}
df_plot <- func_auc()

# plot
ee <- ggplot(df_plot, aes(x = Block, y = AUC))
ee2 <- ee+geom_boxplot(aes(fill=Type))
ee2 + facet_wrap(~Type) + ggtitle("Boxplots of AUCs")



### --- Step 4: ROC plots
#
# Aggregate ROC values across
#   subjects, plot out

df_all <- read.csv(paste0(outDir, "Master_dataframe.csv"))

# Fix1
type <- "Fix1"
df_type_b1 <- df_all[which(df_all$Block == "Block1" & df_all$Type == type),]
df_type_b2 <- df_all[which(df_all$Block == "Block2" & df_all$Type == type),]
df_type_b3 <- df_all[which(df_all$Block == "Block3" & df_all$Type == type),]

roc_b1 <- roc(df_type_b1$Succ, df_type_b1$TrialTypeInt)
roc_b2 <- roc(df_type_b2$Succ, df_type_b2$TrialTypeInt)
roc_b3 <- roc(df_type_b3$Succ, df_type_b3$TrialTypeInt)

e <- ggroc(list(block1=roc_b1, block2=roc_b2, block3=roc_b3)) + 
  ggtitle(paste0("ROC Curves for Type: ",type))
e1 <- e + xlab("FPR") + ylab("TPR")
e1

# Fix2
type <- "Fix2"
df_type_b1 <- df_all[which(df_all$Block == "Block1" & df_all$Type == type),]
df_type_b2 <- df_all[which(df_all$Block == "Block2" & df_all$Type == type),]
df_type_b3 <- df_all[which(df_all$Block == "Block3" & df_all$Type == type),]

roc_b1 <- roc(df_type_b1$Succ, df_type_b1$TrialTypeInt)
roc_b2 <- roc(df_type_b2$Succ, df_type_b2$TrialTypeInt)
roc_b3 <- roc(df_type_b3$Succ, df_type_b3$TrialTypeInt)

e <- ggroc(list(block1=roc_b1, block2=roc_b2, block3=roc_b3)) + 
  ggtitle(paste0("ROC Curves for Type: ",type))
e1 <- e + xlab("FPR") + ylab("TPR")
e1

# Cond
type <- "Cond"
df_type_b1 <- df_all[which(df_all$Block == "Block1" & df_all$Type == type),]
df_type_b2 <- df_all[which(df_all$Block == "Block2" & df_all$Type == type),]
df_type_b3 <- df_all[which(df_all$Block == "Block3" & df_all$Type == type),]

roc_b1 <- roc(df_type_b1$Succ, df_type_b1$TrialTypeInt)
roc_b2 <- roc(df_type_b2$Succ, df_type_b2$TrialTypeInt)
roc_b3 <- roc(df_type_b3$Succ, df_type_b3$TrialTypeInt)

e <- ggroc(list(block1=roc_b1, block2=roc_b2, block3=roc_b3)) + 
  ggtitle(paste0("ROC Curves for Type: ",type))
e1 <- e + xlab("FPR") + ylab("TPR")
e1



### --- Step 5: d-prime scores
#
# Get d' for Fixed trials
#   Targ = Fix1, Lure = Fix2
#
# Whether L/R is Hit/CR is randomized
#   by subject
#
# Writes analyses/Table_d-prime.csv
#
# TODO test for stat differences between
#   blocks, add sig stars to graph

func_dprime <- function(){
  df_all <- read.csv(paste0(outDir, "Master_dataframe.csv"))
  
  # get hit rates for each block/subj
  blockList <- unique(df_all$Block)
  subjList <- unique(df_all$Subj)
  
  # start output df
  df_dprime <- as.data.frame(matrix(NA, nrow=length(subjList)*length(blockList), ncol=3))
  colnames(df_dprime) <- c("Subj", "Block", "dp")
  df_dprime$Subj <- subjList
  df_dprime$Block <- c(
    rep("Block1", length(subjList)), 
    rep("Block2", length(subjList)), 
    rep("Block3", length(subjList)))
  
  for(block in blockList){
    for(subj in subjList){
      
      # subset df
      df_fix1 <- df_all[which(
        df_all$Block == block & 
          df_all$Subj == subj &
          df_all$Type == "Fix1"),]
      
      df_fix2 <- df_all[which(
        df_all$Block == block & 
          df_all$Subj == subj &
          df_all$Type == "Fix2"),]
      
      # get responses
      num_hit <- as.numeric(length(which(df_fix1$Succ == 1)))
      num_miss <- as.numeric(length(which(df_fix1$Succ == 0)))
      num_cr <- as.numeric(length(which(df_fix2$Succ == 1)))
      num_fa <- as.numeric(length(which(df_fix2$Succ == 0)))
      
      # deal with im/perfect performance
      for(beh in c("hit", "miss", "cr", "fa")){
        if(get(paste0("num_",beh)) == 0){
          assign(paste0("num_",beh), 1)
        }
      }
      
      # proportions, z, d-prime
      pHit <- num_hit / (num_hit + num_miss)
      pFA <- num_fa / (num_fa + num_cr)
      zHit <- round(qnorm(pHit),3)
      zFA <- round(qnorm(pFA),3)
      d_prime <- zHit - zFA
      
      # write out
      ind_out <- which(df_dprime$Subj == subj & df_dprime$Block == block)
      df_dprime[ind_out,]$dp <- d_prime
    }
  }
  
  writeOut <- paste0(outDir, "Table_d-prime.csv")
  write.csv(df_dprime, file=writeOut, quote=F, row.names = F)
  return(df_dprime)
}
df_plot <- func_dprime()

ee <- ggplot(df_plot, aes(x = Block, y = dp))
ee2 <- ee+geom_boxplot(aes(fill=dp))
ee2 + ggtitle("Boxplots of D-prime Scores for Fixed Trials") + ylab("d'")







