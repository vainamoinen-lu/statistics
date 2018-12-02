x<-rnorm(100)
eps<-rnorm(100,0,1)
y<- -1+0.5*x+eps
tmp_frame <- data.frame(x=x,y=y)
write.csv(tmp_frame,"xy_data.csv")