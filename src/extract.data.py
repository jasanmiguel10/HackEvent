import sys


with open(sys.argv[1]) as doc:
#       count_correct= 0        there are 117 127 correct
#       count_incorrect = 0     there are 8310 inccorect
        for row in doc:
                div = row.split(',')
                if(len(div)==11):
                        url_image = div[2]
                        #print ('{'+'\''+'url\':'+'\''+str(url_image)+'\''+'}')
                        print(url_image)
