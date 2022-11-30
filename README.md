The process to find which universities currently teach ocaml was done in the following way:

1. I used the "FindOCamlUnis/uni_results.py" script to automatically scrape the website "https://www.4icu.org/us/a-z/" and get a list of universities that mentions OCaml in any page in its domain.

	Although the script works all by itself from time to time the website asks to do a captcha to prove it's not a robot, this can be resolved by hand by looking at what the script is doing every now and then (method used) or by using high quality proxies.

	This resulted in a list of 292 different universities uni_list.txt.

2. From this list I used another script ("FilterOCamlUnis/iter_unis.py") to sort the universities in five text files:

		- uses_ocaml.txt          -> uses ocaml in a class
		- uses_little_ocaml.txt   -> uses ocaml in a few lessons (maybe as a comparison between two languages)
		- used_ocaml.txt          -> used to use ocaml in old courses (maybe the professor changed or they started using another language)
		- mentions_ocaml.txt      -> mentions ocaml maybe in a paper or as a possible language that a student can choose from a bunch of other languages to do a special assignment
		- false_positive.txt      -> false positives

3.  Finally, from the uses_ocaml.txt file I tried to find the most updated courses where ocaml is taught in each university from that file by hand with the help of the site mentioned above, resulting in info.csv

