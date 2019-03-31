import numpy as np


##
## @brief      function_description
##
## @param      filename  The filename
##
## @return     description_of_the_return_value
##
def readfile(filename):
	csvfile = open(filename, "r")
	
	if not csvfile:
		print "error"
		return -1
	
	rows = []
	for row in csvfile:
		if row[0] != '#' : # linhas que comecam com # sao comentarios
			row = row.strip() # removes white space around non white space
			cols = row.split(',') # splits by any white space
			cols = [(col.strip()) for col in cols if (col != '' or col != '\t')]
			rows.append(cols)

	csvfile.close()
	return rows


##
## @brief      Reads for perceptron.
##
## @param      filename  The filename
## @param      dataType  The data type
##
## @return     description_of_the_return_value
##
def readForPerceptron(filename, dataType):
	content = readfile(filename)
	features = np.asarray(content, dtype=dataType)

	# classifications for each feature entry/vector/array
	# np.asarray modifies array on place.
	featuresClassifications = np.array(features[:, -1])

	# changes the classification for the bias entry to 1
	features[:, -1] = 1
	return features, featuresClassifications
	
		