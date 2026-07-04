# Made by Alysa Solomon
# Designed to help Illinois State University's Sociology and Anthropology Depatments
# takes text files from JSTOR to a CSV file
import pandas as pd

def create_data_frame(path_file):
    df = pd.DataFrame()
    # JSTOR Files have an ISSN, URL, Abstract, Author, Journal, Number, Pages, Publisher, Title, urlDate, Volume, and Year
    # TODO: fix look for  list to list of strings, also change file path take an input from caller function
    look_for = ["ISSN", "URL", "abstract", "author", "journal","number","pages","publisher","title","urldate","volume","year"]
    file_path = path_file
    data = {}
    with open(file_path, "r", encoding="utf-8") as file:    
        count = 0

        lines = file.readlines()
        print("file length", len(lines))
        row = ""
        for row in lines:
            word = look_for[count] + " = {"
            endIndex = row.find("}")
            index = row.find(word)
            if index != -1:
                index = index + len(look_for[count] + " = {")
                if (df.empty):
                    data.update({look_for[count]: [row[index:endIndex]]})
                else:
                    data.update({look_for[count]: row[index:endIndex]})
                # try:
                #     data.get(word)
                #     data.update({word: row[index:endIndex]})
                # except:
                #     data.update({word: [row[index:endIndex]]})
                # look_for[count]
                count += 1
            
            if count >= len(look_for):
                count = 0
                try:
                    df.loc[len(df)] = data
                except ValueError:
                    df = pd.DataFrame(data)
            # print("Word:",word,"Count:",count)

        # print(df)
        print("dataframe length",len(df))
        pass
    return df


# there are 6 text files
# df0 = create_data_frame()
file_list = ["C:\\Users\\DragonAro\\Desktop\\TEXT FILE FOR JSTOR\\citations.txt","C:\\Users\\DragonAro\\Desktop\\TEXT FILE FOR JSTOR\\citations1.txt","C:\\Users\\DragonAro\\Desktop\\TEXT FILE FOR JSTOR\\citations2.txt","C:\\Users\\DragonAro\\Desktop\\TEXT FILE FOR JSTOR\\citations3.txt","C:\\Users\\DragonAro\\Desktop\\TEXT FILE FOR JSTOR\\citations4.txt","C:\\Users\\DragonAro\\Desktop\\TEXT FILE FOR JSTOR\\citations5.txt"]
dataframe_list = [create_data_frame(file_list[x]) for x in range(6)]
# df1 = create_data_frame()
# df2 = create_data_frame()
# df3 = create_data_frame()
# df4 = create_data_frame()
# df5 = create_data_frame()
# df6 = create_data_frame()

# print(dataframe_list)
# df = pd.DataFrame

df = pd.concat(dataframe_list)
df = df.sort_values(by="title")

df.to_csv("JSTOR.csv", index=False)
df.to_excel("JSTOR.xlsx")

# print(df)