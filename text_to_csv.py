# Made by Alysa Solomon
# Designed to help Illinois State University's Sociology and Anthropology Depatments
# takes text files from JSTOR to a CSV file
import pandas as pd

def create_data_frame():
    df = pd.DataFrame()
    # JSTOR Files have an ISSN, URL, Abstract, Author, Journal, Number, Pages, Publisher, Title, urlDate, Volume, and Year
    look_for = [["ISSN", False], ["URL", False], ["abstract", False], ["author", False], ["journal", False],["number", False],["pages", False],["publisher", False],["title", False],["urldate", False],["volume", False],["year", False]]
    file_path = input("File Path: ")
    data = {}
    with open(file_path, "r", encoding="utf-8") as file:    
        count = 0

        lines = file.readlines()

        for row in lines:
            word = look_for[count][0] + " = {"
            endIndex = row.find("}")
            index = row.find(word)
            if index != -1:
                index = index + len(look_for[count][0] + " = {")
                if (df.empty):
                    data.update({look_for[count][0]: [row[index:endIndex]]})
                else:
                    data.update({look_for[count][0]: row[index:endIndex]})
                # try:
                #     data.get(word)
                #     data.update({word: row[index:endIndex]})
                # except:
                #     data.update({word: [row[index:endIndex]]})
                look_for[count][1] = True
                count += 1
            
            if count >= len(look_for):
                count = 0
                try:
                    df.loc[len(df)] = data
                except ValueError:
                    df = pd.DataFrame(data)
            # print("Word:",word,"Count:",count)

        # print(df)
        pass
    return df


# there are 6 text files
# df0 = create_data_frame()

dataframe_list = [create_data_frame() for _ in range(6)]
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