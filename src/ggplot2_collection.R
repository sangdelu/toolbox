library(ggplot2)
library(gridExtra)

# scatter plot
ggplot(canada_meta, aes(x=Stroma.content, y=C1.MES)) + geom_point(size=2)

# line plot
ggplot(rare, aes(x=read_number,color=sample, y=genus_number)) + 
  #facet_wrap(~state) +
  geom_line() +
  labs(y = "Detected genuses", x = "Sample") +
  theme(legend.position = "right")

# Modify legend titles
p + labs(fill = "Dose (mg)")

# Add main titles
p + ggtitle("title")


# scatter plot with correlation coefficient and regression line
c1 <- ggscatter(canada_meta, y = "C1.MES", x = "Stroma.content",
                add = "reg.line", conf.int = TRUE, color = sub_col[1],
                cor.coef = TRUE, cor.method = "pearson",
                ylab = "C1.MES", xlab = "Tumor content")

c2 <- ggscatter(canada_meta, y = "C2.IMM", x = "Stroma.content",
                add = "reg.line", conf.int = TRUE, color = sub_col[2],
                cor.coef = TRUE, cor.method = "pearson",
                ylab = "C2.IMM", xlab = "Tumor content")
c4 <- ggscatter(canada_meta, y = "C4.DIF", x = "Stroma.content",
                add = "reg.line", conf.int = TRUE, color = sub_col[3],
                cor.coef = TRUE, cor.method = "pearson",
                ylab = "C4.DIF", xlab = "Tumor content")
c5 <- ggscatter(canada_meta, y = "C5.PRO", x = "Stroma.content",
                add = "reg.line", conf.int = TRUE, color = sub_col[4],
                cor.coef = TRUE, cor.method = "pearson",
                ylab = "C5.PRO", xlab = "Tumor content")
# Multiple plots in one huge plot
grid.arrange(c1,c2,c4,c5,nrow=2,ncol=2)
grid.arrange(grobs = list(step_one,step_two),
             widths = c(2,2.5),
             layout_matrix = rbind(c(1, 2)))


# Change point shapes and colors by groups
ggplot(iris, aes(Sepal.Length, Sepal.Width)) +
  geom_point(aes(shape = Species, color = Species), size = 3) +
  scale_shape_manual(values = c(5, 16, 17)) +
  scale_color_manual(values = c("#00AFBB", "#E7B800", "#FC4E07"))+
  theme_minimal() +
  theme(legend.position = "top")
# Heatmap
# order y labs
ggplot(df,aes(x=test_sample,y=reorder(ylab,Top_N_features),fill=positive_predict_ratio)) +
  geom_tile(colour="white") +
  # change fill color
  scale_fill_gradient2(low = '#0571b0', mid = "white", high = '#ca0020',midpoint=0.5) +
  # remove grey background
  theme(panel.background = element_blank()) +
  labs(y = "Single feature", x = "test_sample") 

# change text size
theme(axis.text.x = element_text(angle = 90, 
                                  size = 8))
