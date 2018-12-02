
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
return(y_x)
}
yx_regr=linear_regression()

scatter_plot<-function(plot_file)
{
    png(file=plot_file)
    plot(xy_data$x,xy_data$y,xlab='x',ylab='y',main='scatter point')
    abline(yx_regr)
    abline(-1,0.5,lty=2,col='red')
    legend('topright',legend=c('sample regression','population regression'),lty=c(1,2),col=c('black','red'))
    dev.off()
}
scatter_plot('scatter_plot_d.png')
