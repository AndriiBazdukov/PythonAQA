class TxtToHtml:
    @staticmethod
    def txt_to_html(path):
        with open(path, 'r') as file:
            header = file.readline().strip().split(',')
            print("<data>")
            for line in file:
                values = line.strip().split(',')
                print("\t<pearson>")
                for field, value in zip(header, values):
                    html = f"\t\t<{field}>{value}</{field}>"
                    print(html)
                print("\t</pearson>")
            print("</data>")


if __name__ == "__main__":
    TxtToHtml.txt_to_html("txt_file.txt")
