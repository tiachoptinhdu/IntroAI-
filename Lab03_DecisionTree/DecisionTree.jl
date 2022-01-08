using CSV 
using DataFrames
using Random
function split_df(df, ratio)
    #Split into two dataframe 
    num = ratio*length(df[:,1]) 
    num = trunc(Int, num)
    return df[1:num, :], df[num+1: length(df[:,1]), :]
 end

 function entropy(list)
    # entropy function use to calculate entropy of list 
    # Input: list     
    # Output: corespond entropy
    # Example: [0,0,0,1,1,1] -> 1 ; ["senota", "senota"] -> 1
    num = length(list) # Number of element in list 
    counts = Dict() #Dictionaries saved frequency of value in list
    for value in list
        counts[value] = get(counts, value, 0) + 1
    end
    result = 0
    for item in counts
        key, value = item 
        p =  value/num # Get probability 
        result -= p * log2(p) 
    end 
    result
end

function Arcmin_T_entropy(X, y, col) 
    #This function find threshold to minimize entropy to split base on feaurute_to_split equilant to maximum information gain
    # Input: X, y and your chosen column 
    # Output: (The best threshold for this column) and (corresponding minimum entropy)
    feature_values = Set(X[!, col])
    total_entropy = 0
    T = 0 #Best threshold
    min = 3 # min value in sum of 2 child entropy
    for threshold in feature_values
        filter_left = X[!, col] .<= threshold
        filter_right = X[!, col] .> threshold
        sum_entropy_node = (sum(filter_left)*entropy(y[filter_left])+sum(filter_right)*entropy(y[filter_right]))/length(y) 
        if sum_entropy_node < min
            min = sum_entropy_node
            T = threshold
        end
    end
    return T, min
end

function Find_Node(X, y) 
    #Input: dataframe X and y 
    #Output: column and threshold 
    # Find (column and correspond threshold) for the best split
    col_name = nothing
    threshold = 0
    min_entropy = entropy(y)
    for col in names(X)
        T, entro = Arcmin_T_entropy(X, y, col)
        if entro < min_entropy
            threshold = T
            min_entropy = entro
            col_name = col
        end
    end
    return col_name, threshold
end

function DecisionTree_Fit(X, y)
    # Input: train dataframe with (X, y) column, y_col is the name of column
    # Output decision tree model 
    tree = Dict()
    col, T = Find_Node(X, y)
    if col === nothing
        value = y[1]
        return value
    end
    index = X[!, col] .<= T
    X_left = X[index, :]
    y_left = y[index, :]

    index = X[!, col] .> T
    X_right = X[index, :]
    y_right = y[index, :]
    
    
    tree["data"] = (col, T) # data save name of column to split and correspond threshold
    tree["left"] = DecisionTree_Fit(X_left, y_left)
    tree["right"] = DecisionTree_Fit(X_right, y_right)
    
    return tree
end

function predict(tree, X)
    # Input: tree, X (X is value of one row)
    # Output: result of predict 
    # Only predict one row in data frame
    node = tree
    if isa(node, Dict) == false
        return node
    end
    col, T = node["data"]
    if X[col] <= T
        predict(node["left"], X)
    else
        predict(node["right"], X)
    end
    
end 

function DecisionTree_Predict(tree, df)
    #Input: Model tree and df of X
    #Output: Predict Result
    result = []
    node = tree
    for i in 1:length(df[:,1])
        push!(result, predict(node, df[i,:]))
    end
    return result
end


#############################################
#############################################
##############MAIN FUNCTION##################
#############################################
#############################################

#Read and split dataframe into train and test
# Dataset IRIS.csv from Kaggle 
df = CSV.File("IRIS.csv") |> DataFrame
df = DataFrame(shuffle(eachrow(df)))
train , test = split_df(df, 0.666666666666666666666)


# Split dataset (X_train, y_train) and (X_test, y_test)
X_train = train[:, 1:4]
y_train = train[:, 5]
X_test = test[:, 1:4]
y_test = test[:, 5]

#The main function inclue: Fit in train and Predict in test
tree = DecisionTree_Fit(X_train, y_train)
result = DecisionTree_Predict(tree, X_train)
println("Train accuracy")
println(sum( result .== y_train)/length(y_train) *100)

result = DecisionTree_Predict(tree, test)
println("Test accuracy")
println(sum( result .== y_test)/length(y_test) *100)

