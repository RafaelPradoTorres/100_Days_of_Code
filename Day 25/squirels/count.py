import pandas

squirrel_data = pandas.read_csv("Squirrel_Data.csv")
fur_color_list = squirrel_data["Primary Fur Color"].to_list()
print(fur_color_list)
gray_count = fur_color_list.count("Gray")
cinnamon_count = fur_color_list.count("Cinnamon")
black_count = fur_color_list.count("Black")

data_dict= {
    "Fur color": ["gray", "cinnamon", "black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")