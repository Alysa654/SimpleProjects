# Made by Alysa Solomon
# Designed to help Illinois State University's Sociology and Anthropology Depatments
# takes text files from JSTOR to a CSV file
import pandas as pd
import rispy

def create_data_frame(path_file):
    df = pd.DataFrame()
    # JSTOR Files have an ISSN, URL, Abstract, Author, Journal, Number, Pages, Publisher, Title, urlDate, Volume, and Year
    look_for = ["ISSN", "URL", "abstract", "author", "journal","number","pages","publisher","title","urldate","volume","year"]

    # data = {"ISSN":"", "URL":"", "abstract":"", "author":"", "journal":"","number":"","pages":"","publisher":"","title":"","urldate":"","volume":"","year":""}
    with open(path_file, "r", encoding="utf-8") as file:    
        entries = rispy.load(file)
        isFirst = True
        for entry in entries:
            if isFirst:
                temp_dic = {}
                for key in entry.keys():
                    temp_dic.update({key:[entry[key]]})
                    pass
                df = pd.DataFrame(temp_dic)
                isFirst = False
            else:
                df.loc[len(df)] = entry

        pass
    return df


# there are 6 text files
# df0 = create_data_frame()
file_list = ["C:\\Users\\DragonAro\\Desktop\\TEXT FILE FOR JSTOR\\citations.ris","C:\\Users\\DragonAro\\Desktop\\TEXT FILE FOR JSTOR\\citations1.ris","C:\\Users\\DragonAro\\Desktop\\TEXT FILE FOR JSTOR\\citations2.ris","C:\\Users\\DragonAro\\Desktop\\TEXT FILE FOR JSTOR\\citations3.ris","C:\\Users\\DragonAro\\Desktop\\TEXT FILE FOR JSTOR\\citations4.ris","C:\\Users\\DragonAro\\Desktop\\TEXT FILE FOR JSTOR\\citations5.ris"]
dataframe_list = [create_data_frame(file_list[x]) for x in range(6)]
# df = create_data_frame(file_list[0])

# print(dataframe_list)
# df = pd.DataFrame

df = pd.concat(dataframe_list)
df = df.sort_values(by="title")

df.to_csv("JSTOR.csv", index=False)
df.to_excel("JSTOR.xlsx")

print(df)