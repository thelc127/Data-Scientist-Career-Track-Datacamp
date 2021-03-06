# Import the first 5 rows of the file into a DataFrame using the function pd.read_csv() and assign the result to data.
# You'll need to use the arguments nrows and header (there is no header in this file).
# Build a numpy array from the resulting DataFrame in data and assign to data_array.
# Execute print(type(data_array)) to print the datatype of data_array.
# Assign the filename: file
file = 'digits.csv'

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows = 5, header = None)

# Build a numpy array from the DataFrame: data_array
data_array = np.array(data)

# Print the datatype of data_array to the shell
print(type(data_array))