import filter_unis

file1 = open('uni_list.txt', 'r')
Lines = file1.readlines()

files = {
    "1" : "use_ocaml.txt",
    "2" : "uses_little_ocaml.txt",
    "3" : "used_ocaml.txt",
    "4" : "mentions_ocaml.txt",
    "5" : "false_positive.txt",
}

# last done -> line 60
def filter_lines():

    global Lines

    Lines = Lines[(Lines.index("https://www.4icu.org/reviews/5759.htm\n")+1):]


# filter_lines()


for line in Lines:

    f = filter_unis.has_results(line.strip(), files)

    file = open(f, 'a')
    file.write(line)
    file.close()
