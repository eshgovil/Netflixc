#Ashwin Hari
#04/24/17

library("softImpute")

#Load Training Data
setwd("C:\\Users\\ahari\\Documents\\Caltech\\Spring 2017\\CS156b\\um")
D = scan('X_train_2.dta', what = list(numeric(), numeric(), numeric()))

#Create Incomplete Matrix
D_inc = Incomplete(D[[1]], D[[2]], D[[3]])

#Scale Matrix
D_inc_sc = biScale(D_inc,col.scale=FALSE,row.scale=FALSE)

#Soft-Impute
S = softImpute(D_inc_sc,rank.max=100,lambda=0.04,trace=TRUE,type="als")

#De-bias
S_db = deBias(D_inc_sc, S)


#Impute ("Predict")
Qual = scan('qual.dta', what = list(integer(), integer(), integer()))
pred_SI_42_als = impute(S, Qual[[1]], Qual[[2]], unscale = TRUE)

#Save Prediction
write.table(pred_SI_10, file="pred_SI_10.dta", row.names=FALSE, col.names=FALSE)