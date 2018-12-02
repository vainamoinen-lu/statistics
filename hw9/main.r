
# x<-rnorm(100)
# eps<-rnorm(100,0,0.5)
# y<- -1+0.5*x+eps
get_data<-function()
{
    xy_data=read.csv("xy_data.csv")
    return(xy_data)
}
xy_data=get_data()
linear_regression<- function()
{
y_x <- lm(y~x,xy_data)
print(y_x)
}
linear_regression()

