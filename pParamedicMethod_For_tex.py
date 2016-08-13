###############################################
#Python program to read a tex file and output
#a modified version according to the Paramedic Method:
#	1. Bold prepositions
#	2. Emphasize the 'to be' verbs
#	3. Underline common nominalizations
#
# Add these lines to the tex source after running and then 
# recompile the pdf to see the changes (requires the tiks package)
##############################################

def CheckForPreposition(word):
	preplist = ["at","in","on","of","to","about","around","below","above",
	"from","into","near","since","through","against","after","outside"]
	new_word = word
	for prep in preplist:
		#print "prep: ", prep, " word: ", word
		if word == prep:
			#print "word: ", word
			new_word = "\\textcolor{red}{\\textbf{"+word+"}}"
			#print "new word: ", new_word
			break
	return new_word

def CheckForToBeVerb(word):
	verblist = ["am","is","are","was","were"]
	new_word = word
	for verb in verblist:
		if word == verb:
			new_word = "\\textcolor{orange}{\emph{"+word+"}}"
			break
	return new_word

def CheckForNominalization(word):
	nomlist =["discovery","movement","resistance","reaction","failure","refusal",
	"carelessness","difficulty",
	"elegance","applicability","intensity","evaluation","derivation","conclusion",
	"demonstration","analysis","indication","study"]
	new_word = word
	for nom in nomlist:
		if word == nom:
			new_word = "\\textcolor{purple}{\underline{"+word+"}}"
			break
	return new_word

def CheckForPunctuation(word):

	punclist=[".",",",";",":"]
	new_word=word
	pflag=False
	for punc in punclist:
		if word.endswith(punc):
			pflag=True
			new_word=word[-1:]
			break
	return pflag

def StripPunctuation(word):
	new_word=""
	n_char = len(word)
	for i in xrange(n_char-1):
		new_word+=word[i]
	#print" stripping punctuation: \n"
	#print "word: ", word, "\n"
	#print "new word: ", new_word
	#exit 
	return new_word

#open the original tex file
ifile = open('CTNS_draft18.tex', 'r')
#open the output file
ofile = open('Draft_parm.tex', 'w')
for line in ifile:
	for word in line.split():
		punc=""
		puncflag=False
		puncflag=CheckForPunctuation(word)
		
			
		if puncflag:
			i=len(word)
			punc=word[i-1]
			word=StripPunctuation(word)
		if not (word.startswith("\\")):
			word=CheckForPreposition(word)
			#print "word is: ", word
			word=CheckForToBeVerb(word)
			word=CheckForNominalization(word)
		if puncflag:
			word+=punc
		
		ofile.write(word+" ")
	ofile.write("\n")		

