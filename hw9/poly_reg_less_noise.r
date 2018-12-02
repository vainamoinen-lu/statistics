#question1(g)
get_data<-function()
{
    xy_data=read.csv("xy_data.csv")
    return(xy_data)
}
xy_data=get_data()

poly_regression<-function()
{
    y=xy_data$y
    x=xy_data$x
    y_poly_model<-lm(y~poly(x,2))
    print(summary(y_poly_model))
    return(y_poly_model)
}
y_poly_model=poly_regression()