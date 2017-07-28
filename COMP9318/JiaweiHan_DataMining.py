# Jiawei Han's Data Mining Concepts and Techniques 3rd Edition
# Notes taken by Yunqiu Xu



# Chapter 1 Introduction
+ Overview:
    + Why we use DM
    + What is DM
    + Components of DM: data/knowledge/techniques/applications
    + Major issues
## 1.2 What is DM
+ KDD: knowledge discovery from data
+ What we wanna do is discoverying interesting knowledge from massive data
+ The process: #P7 Fig 1.4
    + data cleaning
    + data integration
    + data selection
    + data transformation
    + data mining
    + pattern evaluation
    + knowledge presentation

## 1.3 The kind of data
+ database data
    + relational DBMS
    + ER model
    + database queries --> get relational data
+ data warehouse data
    + DW: 
        + a repository of information from miltiple sources
        + stored upder a unified schema
        + reside at a single site
    + How to create a DW: 
        #Chapter 3 & Chapter 4
        #P11 Fig1.6: framework
        + data cleaning
        + data integration
        + data transformation
        + data loading
        + periodic data refreshing
    + DW can provide inherent support for OLAP
        # P12 Fig1.7
        # https://www.zhihu.com/question/19955124
        + drill-down:
            + get more details 
            + divide Q1 to Jan/Feb/March
        + roll-up: 
            + do some summary
            + combine NewYork/Chicago to USA
        + slice: 
            + keep some dimentions in particular value
        + dice:
            + keep some dimentions in particular range
        + pivot: 
            + flatten multiple dimentions in a table
+ transactional data
    + each record in a transactional database captures a transaction
        + a customer purchase
        + a flight booking
        + a users click on a web page
    + transaction: includes a trans_ID and a list of items
    + transactional DB:
        # P13 Fig 1.8 
        + have additional tables, which contain other information related to the transactions
        + item descroption
        + info about the salesperson/branch 

## 1.4 The kind of knowledge
+ DM functionalities
    + characterization / discrimination
    + frequent patterns / associations / correlations
    + classification / regression
    + clustering analysis
    + outlier analysis

+ These tasks can be classified into 2 cates: 
    + descriptive: 
        + characterize properties of the data 
        + put them in a target data set
    + predictive
        + perform induction on current data
        + make predictions
### 1.4.1 Characterization and Discrimination
+ Class/concept descriptions: 
    + describe individual classes into summarized/precise terms
+ data characterization: summarize the data of the target class in general terms
    + how to do it: SQL query
    + statistical measures # Chapter 2
    + OLAP roll-up #1.3
    + data warehousing: #Chapter 4 and Chapter 5
    + attribute-oriented induction #Chapter 4
+ data discrimination:  compare the target class with contrasting classes
    + comparison target class data those from multiple contrasting classes

### 1.4.2 Mining Frequent Patterns, Associations, and Correlations
+ Frequent patterns
    + frequent itemsets
        + often appear together
        + milk and bread
    + frequent subsequences
        + buy laptop first
        + then digital camera
        + then memory card
    + frequent substructures 
        + combination of itemsets and subsequences

+ Association analysis:
    + see the example #P17
    + X is a var representing a customer
    + confidence(certainty): P(X|Y), the conditional probability
    + support: P(X,Y), joint possibility
    + e.g. "computer -> software[1%, 50%]"
        + the possibility of buy them together is 1%
        + if buy computer, 50% will buy software as well

+ details will be discussed in #Chapter 6 and 7

### 1.4.3 Classification and Regression for Predictive Analysis
+ ML: build model from training data, then make prediction from testing data
+ details will be discussed in #Chapter 8 and 9
+ This book will not discuss regression

### 1.4.4 CLuster Analysis
+ Unsupervised learning
+ details will be discussed in #Chapter 10 and 11

### 1.4.5 Outlier Analysis(anomoly mining)
+ How to detect them:
    + use statistical tests, assume a distribution or probability model
    + use distance measures
    + density-based methods
+ details will be discussed in #Chapter 12

### 1.4.6 Pattern selection
+ What pattern is interesting
    + easily understood by humans
    + valid on new or test data with high certainty
    + potentially useful
    + novel
+ Objective measures:
    + support(X -> Y) = P(X U Y)
    + confidence(X -> Y) = P(Y | X)
    + accuracy: how many of them is correctly classified
    + coverage: the percentage of data to which a rule applies
+ Subjective measures: based on user beliefs in the data
    + find patterns interesting if the patterns are unexpected(contra the belief)

## 1.5 The kind of techniques
+ Techniques can be seen in #P23 Fig 1.11

## 1.6 Applications

## 1.7 Major issues
+ Mining methodology
+ User interaction
+ Efficiency and scalability
+ Diversity of data types
+ Data mining and society

## 1.8 Summary
+ Necessary is the mother of invention
+ Difinition of DM
+ Interestingness
+ The dimensions of DM: data/knowledge/techniques/applications
+ Data warehouse/OLAP
+ Functionalities

---------------------------------------
## Chapter 1 Exercises
1. Some concept of DM
+ DM will use ML to build model, and some non-ML methods can also be used in DM

2. The similarities and differences between database and data warehouse

3. The concept and example of functionalities

4. The applications of functionalities

5. The differences and similarities between those functionalities

6. Fraudulence detection: give methods to detect outliers
---------------------------------------

# Chapter 2 Getting to Know Your Data
+ Overview
    + Various attribute types
    + Use statistical methods to learn more about attributes values
    + Data cleaning
    + Visualization
    + Measures of data proximiity

## 2.1 Data Objects and Attribute Types
+ Attribute: Discrete VS Continuous
    + Norminal
    + Binary
    + Ordinal
    + Numeric
        + Interval-Scaled Attributes
        + Ratio-Scaled Attributes

## 2.2 Basic Statistical Descriptions of Data
+ It is important to have an overall picture of data

###2.2.1 Measures of central tendency
+ Mean
+ Median
+ Mode
+ Midrange

###2.2.2 Common data dispersion
+ Range 
+ Quartiles
+ Variance
+ SD
+ Interquartile Range

## 2.3 Virsualization

## 2.4 Measuring Data Similarity and Dissimilarity

### 2.4.1 Data Matrix VS Dissimilarity Matrix
+ Data Matrix: store the data objects
    + n * p: n objects, p attributes
    + every row is an object 
    + every column is an attribute
+ Dissimilarity Matrix: store dissimilarity values for pairs of objects
    + we can see this at #p68
    + n * n: d(i,j) is the dissimilarity of object i and object j

+ some properties:
    + d(i,i) in [0,1]
    + d(i,i) = 0
    + d(i,j) = d(j,i)
    + sim(i,j) = 1 - d(i,j) #p68 2.10

### 2.4.2 Dissimilarity: Nominal Attributes 
+ E.G. map color in (red, yellow, green, pink, blue)
+ Compute the dissimilarity: d(i,j) = (p-m)/p #p69
    + m: number of matches
    + p: total numbers of attributes
+ Compute the similarity: sim(i,j) = 1 - d(i,j) = m/p

### 2.4.3 Dissimilarity: Binary Attributes
+ Contingency Table: #p70
+ Dissimilarity: d(i,j) = (r+s) / (q+r+s+t)
+ for asymmetric binary attributes: d(i,j) = (r+s) / (q+r+s)

### 2.4.4 Dissimilarity: Numeric Attributes
+ Minkowski Distance
    + Euclidean Distance: h = 2
    + Manhattan Distance: h = 1
    + Non-negativity / Indentity / Symmetry / Triangle inequality

### 2.4.5 Dissimilarity: Ordinal Attributes
### 2.4.6 Combination
### 2.4.7 Similarities for long/sparse data vectors
## 2.5 Summary
+ What is a data object
+ Different knid of attributes
+ Basic statistical descriptions
+ Data Visualization
+ Similarity and Dissimilarity

---------------------------------------
## Chapter 2 Exercises

1. Compute the mean / median / mode / midrange / Q1 / Q3
    + five-number summary
    + boxplot
    + quantile-quantile plot different from quantile plot
    #p90 example 2.14

2. How to compute the dissimilarity:
    + Norminal
    + Asymmetric binary
    + Numeric
    + Term-frequency

3. give 2 objects:
    + Euclidean
    + Manhattan
    + Minkowski, q = 3
    + supremum distance

---------------------------------------

# Chapter 3 Data Preprocessing
## 3.1 What is data preprocessing
+ Data quality: accuracy/ completeness/ consistency
+ Major tasks:
    + Data cleaning
    + Data integration
    + Data reduction
    + Data transformation
+ #P87 Fig 3.1

## 3.2 Data Cleaning
### 3.2.1 Missing Values
+ Ignore the tuple
+ Fill in missing value manually
+ Use a global constant to fill in the missing value
+ Use a measure of central tendency of the attribute to fill in
+ Use the measure of all samples in same class as the given tuple
+ Use the most probable value
### 3.2.2 Noisy Data
+ Binning 
    + create some buckets, then smooth by bin means/medians
    + We can see the example ar #P90 fig 3.2
+ Regression
+ Outlier analysis
### 3.2.3 Data Cleaning as a Process
+ ... # P91-93 ignored

## 3.3 Data Integration
+ Merging data from multiple data stores
+ Reduce redundancies and inconsistencies
+ Improve the accuracy and speed
### 3.3.1 Entity Identification Problem
+ Def.: How can equivalent real-world entities from multiple data sources be matched up?
+ E.G.: For example, how can the data analyst or the computer be sure that customer id in one database and cust number in another refer to the same attribute? 

### 3.3.2 Redundancy and Correlation Analysis
+ Redundant: can be derived from another attribute
+ How to detect redundancies: correlation analysis
    + measure how strongly one implies another
+ 2 kinds of test:
    + Norminal: X^2 test
    + Numeric: correlation coefficient and covariance
+ chi-square Correlation Test for Nominal Data #P95
    + compute the expected frequency first
    + then compute the chi-square
+ Correlation Coefficient for Numeric Data #P96 3.3
+ Covariance of Numeric Data #P97
    + compute the mean value E(A), E(B)
    + then compute the covariance of A and B
    + Cov(A,B) = E(A * B) - E(A)*E(B)
### 3.3.3 Tuple duplication
### 3.3.4 Detection and resolution of data value conflicts

## 3.4 Data Reduction
+ reduce the volume, maintains the integrity of original data
+ strategies:
    + Dimensionality reduction: reduce the number of random variables
        + wavelet transforms
        + PCA
        + Attribute subset selection
    + Numerosity reduction: replace the original data volume by smaller forms of data
        + parametric: regression / log-linear
        + non-parametric: histograms / clustering / sampling / cube aggregation
    + Data compression: transform the form of original data
### 3.4.1 Wavelet Transforms - dimension reduction
+ discrete wavelet transform (DWT) is a linear signal processing technique #P100
+ We can also consider DFT here(discrete Fourier transform)

### 3.4.2 PCA - dimension reduction
+ We have learnt this at coursera
+ The procedure can be seen at #P102

### 3.4.3 Attribute Subset Selection - dimension reduction
+ Remove irrelevent or redundant attributes
+ Forward / Backward / Decision Tree: greedy

### 3.4.4 regression / log-linear - parametric data reduciton

### 3.4.5 Histograms - non-parametric data reduciton
+ Create buckets --> ranges
+ Equal-width
+ Equal-frequency

### 3.4.6 Clustering
+ We can see clustering methods at #Chapter 10 and Chapter 11 

### 3.4.7 Sampling
# Example: p109 Fig 3.9
+ 4 kinds of sampling
    + SRSWOR: simple random sample without replacement
    + SRSWR: simple random sample with replacement
    + Cluster sample
    + Stratified sample
+ Advantage: the cost of obtaining a sample is proportional to the size of the sample, s, as opposed to N , the data set size
    + complexity: sublinear to the data size
+ sampling is most commonly used to estimate the answer to an aggregate query

### 3.4.8 Data Cube Aggregation
# Chapter 4 Data Warehousing
# Chapter 5 Data Cube Technology
+ What is data cube: it stores multidimensional aggregated information 
+ Data cubes provide fast access to precomputed, summarized data
+ Base cuboid: cube created at the lowest abstraction level
+ Apex cuboid: cube created at the highest abstraction level

## 3.5 Data Transformation and Data Discretization
+ Make resulting mining process more efficient
+ Make patterns easier to understand
### 3.5.1 How to perform data transformation
+ Smoothing
+ Attribute construction
+ Aggregation
+ Normalization
+ Discretization: interval/conceptual labels
+ Concept hierarchy generation for nominal data

### 3.5.2 Normalization
+ Min-max normalization #p114 equa 3.8
+ z-score normalization
+ Decimal scaling

### 3.5.3 Binning

### 3.5.4 Histogram Analysis

### 3.5.5 CLuster, Decision Tree and Correlation Analysis

### 3.5.6 Concept Hierarchy Generation for Nominal Data
+ #P119 Fig 3.13

## 3.6 Summary
+ Data quality: 
    + accuracy
    + completeness
    + consistency
    + timeliness
    + believability
    + interpretability
+ Data cleaning: 
    + discrepancy detecting 
    + data transformation
+ Data integration:
    + Dimensionality reduction
    + Numerosity reduction
    + Data compression
+ Data transformation:
    + Normalization
    + Data Discretization
    + Concept Hierarchy Generation

---------------------------------------
## Chapter 3 Exercises
1. Something about data quality
2. how to handle missing value
3. Give some data:
    + smoothing by means
    + how to determine outliers
    + List other methods for data smoothing
4. How to perform data integration
5. Value ranges of different normalization methods
6. Use of different normalization methods

7. Give some data
    + equal-frequency (equal-depth) partitioning
    + equal-width partitioning
    + clustering
8. Summarize subset selection:
    + Forward
    + Backward
    + Combination
9. Sampling
    + SRSWOR
    + SRSWR
    + Cluster sampling
    + Stratified sampling

---------------------------------------

# Chapter 4 Data Warehousing and OLAP
## 4.1 DW: Basic Concepts
### 4.1.1 What is DW
+ Def.: A data warehouse is a subject-oriented, integrated, time-variant, and nonvolatile collection of data in support of management’s decision making process
    + It is a semantically consistent data store that serves as a physical implementation of a decision support data model
    + It stores the information an enterprise needs to make strategic decisions.
+ Key features of DW:
    + subject-oriented: 
        + DW focuses on the modeling and analysis of data for decision makers
        + DW provide a simple and concise view of particular subject issues by excluding data that are not useful in the decision support process
    + integrated
        + integrating multiple heterogeneous sources
        + data cleaning and data integration are applied
    + time-variant
        + every element contains a time element(e.g. timestamp)
    + nonvolatile
        + DW is just a physically separate store of data, which is transformed from the application data found in the operational environment
        + DW does not require transaction processing, recovery, and concurrency control mechanisms
        + DW only requires "initial loading of data" and "access of data"

+ What is data warehousing: the process of constructing and using data warehouses

+ How to construct a DW:
    + data cleaning
    + data integration
    + data consolidation

+ Why dont use "query-driven approach": 
    + requires complex information filtering and integration processes
    + competes with local sites for processing resources

### 4.1.2 Operational Database Systems versus Data Warehouses
+ Online operational database systems
    + OLTP: online transaction processing systems
    + Major task: perform online transaction and query processing
    + Cover: day-to-day operations
+ Data warehouse systems:
    + OLAP: online analytical processing systems
    + serve users or knowledge workers in the role of data analysis and decision making
    + organize and present data in various formats

+ Comparation between OLTP and OLAP:
    + Users and system orientation:
        + OLTP: customer-oriented, used for transaction and query processing
        + OLAP: market-oriented, used for data analysis
    + Data contents:
        + OLTP: manages current data,  too detailed
        + OLAP: massive historic data, easier to make decision
    + Database design: 
        + OLTP: ER model, application-oriented database design
        + OLAP: star / snowflake model, subject-oriented database design
    + View: 
        + OLTP: current data
        + OLAP: multiple versions of database schema, data from different organizations, stored on multiple storage media
    + Access patterns:
        + OLTP: short, atomic transactions, needs concurrency control and recovery mechanisms
        + OLAP: read-only operations
    # P130 Table 4.1

### 4.1.3 Why we use separate data warehouse
# See P129
+ Help permote the high performance of both systems
+ Processing OLAP queries(Complex) in operational databases would substantially degrade the performance of operational tasks
+ OLAP can not use concurrency control and recovery mechanisms
+ the separation of operational databases from data warehouses is based on the different structures, contents, and uses of the data in these two systems.
+ TREND: the separation between OLTP and OLAP is decreasing

### 4.1.4 Architecture of DW - Multitier
Data -> Data warehouse server -> OLAP server -> Front-end tools

## 4.2 Data Cube and OLAP operations
### 4.2.1 Data Cube -> Multidimensional Data Model
+ Dimensions -> dimension table
    + a dimension table for item may contain the attributes item name, brand, and type
+ Facts(numeric measures) -> fact table
    + The fact table contains the names of the facts, or measures, as well as keys to each of the related dimension tables.
# We can see 2-D 3-D 4-D examples at P137-138
+ apex -> 1-D -> 2-D -> 3-D -> 4-D #p139 Fig 4.5

### 4.2.2 Schemas for Data Cubes
+ star schema #p140
    + a large central table (fact table): no redundancy
    + a set of smaller tables(dimension tables): one for each dimension

+ snowflake schema: make it further
    + a variant of star schema
    + some dimension tables are normalized
    + further splitting data into additional tables
    + Difference from star schema: dimension tables of the snowflake model may be kept in normalized form to reduce redundancies
    + Note that normalization will affect the performance -> snowflake is not so popular

+ fact constellation schema #p143 fig4.8
    + two fact tables
    + has five dimensions

### 4.2.3 Dimensions: The Role of Concept Hierarchies
+ concept hierarchy: 
    + a sequence of mappings from a set of low-level concepts to higher-level, more general concepts
    + city -> province -> country

+ schema hierarchy VS set-grouping hierarchy

### 4.2.4 Measures: Categorization and Computation
+ distributive
+ algebraic
+ holistic

### 4.2.5 Typical OLAP Operations
+ Roll-up:
+ Drill-down:
+ Slice and dice:
+ Pivot(rotate)
# See P147 Fig4.12

## 4.3 DW Design and Usage
### 4.3.1 Let's See a Business Analysis Framework First
+ 4 views regarding a data warehouse design:
    + top-down view: allows the selection of relevant information which is necessary for the data warehouse
    + data source view
        + exposes the information
        + document the data at various levels of detail and accuracy
        + model the data in traditional techniques(e.g. E-R)
    + data warehouse view
        + fact tables and dimension tables
        + represent the data stored in DW
    + business query view
        + data perspective from end-user viewpoint

### 4.3.2 Data Warehouse Design Process
+ Approaches to build a data warehouse:
    + top-down:
        + start with overall design and planning
        + cases: tech is mature, problem is clear
    + bottom-up:
        + starts with experiments and prototypes
        + useful: early stage of modeling
        + less expense, can evaluate benefits before making commitments
    + combined approach

+ Process to build a data warehouse:
    + Choose a business process to model
    + Choose the business process grain
    + Choose the dimensions that will apply to each fact table record
        + E.G. time, item, customer, supplier
    + Choose the measures that will populate each fact table record.
        + E.G. numeric additive quantities, dollars_sold...

### 4.3.3 DW Usage(Application) for Information Processing
+ Information processing
+ Analytical processing
+ Data Mining

### 4.4.4 From OLAP to Multidimensional Data Mining
+ Why we use multidimensional data mining:
    + High quality of data in data warehouses
    + Available information processing infractructure surrounding data warehouses
    + OLAP-based exploration of multidimensional data
    + Online selection of data mining functons

## 4.4 DW Implementation
### 4.4.1 How to compute data cube efficiently
+ When we use SQL, we can achieve aggregations via "group by"
    + no group-by: 0-D(apex)
    + one group-by: 1-D
+ A data cube is a lattice of cuboids
+ An example
    + you maybe want to analyze the data via:
        + "Compute the sum of sales, grouping by city and item."
        + "Compute the sum of sales, grouping by city."
        + "Compute the sum of sales, grouping by item."
    + 3 dimensions: city, item, year
    + measure: sales_in_dollare
    + the total number of cuboids(group-bys): 8 #p194 fig 4.14
    + Base cuboid: 
        + all dimensions
        + sales of any combination of dimensions
        + the least generalized (most specific) of the cuboids
    + Apex cuboid: 
        + group-by is empty
        + the total sum of all sales
        + the most generalized (least specific) of the cuboids

+ Partial Materialization: Selected Computation of Cuboids
    + No Materialization
    + Full Materialization
    + Partial Materialization

### 4.4.2 How OLAP data can be indexed: Bitmap Index and Join Index
+ Bitmap Indexing: allows quick searching in data cubes
    + read this: http://www.360doc.com/content/14/0508/15/11965070_375805586.shtml
    + #P198 Fig4.15
    + Useful when:
        + columns with countable values(e.g. sex, district)
        + static data, when updating is used frequently it can not be used
+ Join Indexing: useful in relational database query processing
    + #P199 Fig4.16 and Fig4.17

### 4.4.3 How OLAP queries are processed efficiently
+ Determine which operations should be performed on the available cuboids
+ Determine to which materialized cuboid(s) the relevant operations should be applied
# see p200 example 4.9 -> cuboid 3

### 4.4.4 Different types of DW servers for OLAP processing
+ ROLAP: Relational

+ MOLAP: Multidimensional

+ HOLAP: Hybrid


## 4.5 Data Generalization by Attribute-oriented Induction
Is data cube technology sufficient to accomplish all kinds of concept description tasks for large data sets
+ Complex data types and aggregation
+ User control versus automation
+ ignored # P166- 178

## 4.6 Summary
+ What is DW: a subject-oriented, integrated, time-variant, and nonvolatile data collection
+ three-tier architecture:
    + warehouse database server
    + OLAP server
    + client

+ back-end tools and utilities: data extraction, data cleaning, data transformation, loading, refreshing, and warehouse management.

+ Data warehouse metadata
+ Multidimensional data model -> data cube -> facts and dimensions
+ data cube -> a lattice of cuboids
+ Concept Hierarchies
+ Perform OLAP using multidimensional model
    + OLAP operations: roll-up/ drill-down/ slice-and-dice/ pivot
    + OLAP operations can be performed efficiently via data cube structure
+ OLAP servers: ROLAP/MOLAP/HOLAP
+ Full materialization -> all cuboids -> curse of Dimensionality -> partial materialization
+ indexing : bitmap / join
+ Data Generalization
    + data cube-based data aggregation
    + attribute-oriented induction
+ Concept description is the most basic form of descriptive data mining
    + characterization: summarizes and describes a data collection -> target class
    + comparison: summarizes and distinguishes one data collection -> contrasting class
+ attribute-oriented induction:
    + data focusing
    + data generalization by attribute removal or attribute generalization
    + count and aggregate value accumulation
    + attribute generalization control
    + generalization data visualization

---------------------------------------
## 4.7 Exercises
1. Why update-driven approach is more preferable than query-driven approach

2. Make comparations:
    + snowflake schema/ fact constellation/ starnet query model
    + data cleaning/ data transformation/ refresh
    + discovery-driven cube/ multifeature cube/ virtual warehouse

3. Some questions aboue data warehouse

4. ROLAP/ MOLAP/ HOLAP: 
    + difinition
    + how the functions/operations be performed

5. number of cells in data cube
6. information processing / analytical processing / data mining
7. Why we need OLAP mining
---------------------------------------

# P190
# Chapter 5 Data Cube Technoligy
+ Methods for data cube computation
+ Methods for multidimensional data analysis

## 5.1 Preliminary concepts for cube computation


## 5.2 Methods for data cube computation


## 5.3 Cube-based query processing


## 5.4 Various ways to perform multidimensional data analysis using data cubes

## 5.5 Summary
+ Data cube computation and exploration is important
+ A data cube consists of a lattice of cuboids
    + Full materialization
    + Partial materialization
        + Iceberg cube: only store those with an aggregate value above some threshold
        + Shell fragments: only some cuboids with less dimensions are computed
+ Data cube computation methods:
    + MultiWay array aggregation:
        + Computing: meterializing full data cubes
        + Computation: sparse-array-based, bottom-up, shared
    + BUC:
        + Computing: iceberg cubes
        + Computation: exploring ordering and sorting for efficient top-down computation
    + Star-Cubing:
        + Computing: iceberg cubes
        + Computation: integrating top-down and bottom-up computation using a star-tree structure
    + Shell-fragment cubing:
        + supports high-dimensional OLAP
        + precomputing only the partitioned cube shell fragments

+ Multidimensional data mining in cube space
+ Techniques for processing advanced queries
    + Sampling cubes
    + Ranking cubes
+ Three approaches to multidimensional data analysis with data cubes
    + Prediction cubes
    + Multifeature cubes
    + Exception-based, discovery-driven exploration

---------------------------------------
## 5.6 Chapter 6 Exercises


---------------------------------------

# Chapter 6 Mining Frequent Patterns, Associations and Correlations

## 6.1 Basic Concepts
+ Sth we learned before:
    + support(A->B) = P(A U B)
    + confidence(A->B) = P(B | A)
    + strong: rules satisfies both minimum support threshold and minimum confidence threshold
    + frequency(support count): occurence frequency of an itemset, i.e. number of transactions that contains this itemset 
    + support is "relative support", and frequency is "aboslute support"
    + frequent itemset: if the relative support of this itemset satisfies prespecified minimum support threshold
    + confidence(A->B) = P(B|A) = support(A U B) / support(A) = frequency(A U B) / frequency(A)

+ Association rule mining can be viewed as 2 steps:
    + Find all frequent itemsets #6.2.1 Apriori
    + Generate strong association rules from frequent itemsets #6.2.2

+ A challenge in mining frequent itemsets: too many of itemsets
    + C(100,1) + C(100,2) + ... + C(100,100)
    + So we introduce "closed frequent itemset" and "maximal frequent itemset"
    + closed itemset X in data set D: if there exists no proper super-itemset Y(X belongs to Y and not equal to Y) that Y has the same frequency as X in D   
    + closed frequent itemset X in D: X is both closed and frequent in D
    + maximal frequent itemset X in D: X is frequent, no Y is frequent
    # see p248 example 6.2

## 6.2 How to Mine Frequent Itemset
### 6.2.1 Apriori -> basic algorithm for finding frequent itemsets -> Confined Candidate Generation
+ ref: 
    + http://blog.csdn.net/lizhengnanhua/article/details/9061755
    + ML in Action
+ Apriori property: All nonempty subsets of a frequent itemset must also be frequent.
+ From L(k-1) to L(k) --> join & prune(use property)
# See p251 Fig 6.2 and Example 6.3
+ From L2 to C3: Based on the Apriori property that all subsets of a frequent itemset must also be frequent, we can determine that the four latter candidates cannot possibly be frequent.

+ The persudo code can be seen at p253

### 6.2.2 Generating Association Rules from Frequent Itemsets
+ Procedure:
    + For each frequent itemset l, generate all nonempty subsets of l
    + For every nonempty subset s of l, output the rule "s -> (l − s)" if frequency(l)/frequency(s) > min_conf_threshold
    #see p254 example 6.4

### 6.2.3 Improving the Efficiency of Apriori
+ Apriori算法的缺点：
    + 由frequent itemset k-1 进行自连接生成的 candidate frequent itemset k数量巨大
    + 在验证candidate frequent itemset k时需要对整个数据库进行扫描，非常耗时
+ Method to optimize Apriori:
    + Hash-based techinique: hashing itemsets into corresponding buckets
    + Transaction reduction: reducing the number of transactions scanned in future iterations
    + Partitioning: partitioning the data to find candidate itemsets
    + Sampling: mining on a subset of the given data
    + Dynamic itemset counting (adding candidate itemsets at different points during a scan)

### 6.2.4 Frequent Pattern-Growth for Mining Frequent Itemsets
*** 'Still Have Some Questions' ***
+ FP-growth is based on Apriori but more efficient
    + Build FP-Tree
    + Mine frequent itemset from FP-Tree
+ By using FP-growth, we only scan database twice.其中第1次扫描获得当个项目的频率，去掉不符合支持度要求的项,并对剩下的项排序。第2遍扫描是建立一颗FP-Tree(frequent-patten tree)
+ Procedure:
    #http://blog.sina.com.cn/s/blog_68ffc7a40100uebg.html
    #http://www.cnblogs.com/zhangchaoyang/articles/2198946.html
    + 1st scan: similar to Apriori, get the set of frequent items(1-itemsets) and their frequencies
    + let minimum support count = 2
    + sort the frequent items in descending order, E.G. L = {{I2:7}, {I1:6}, {I3:6}, {I4:2}, {I5:2}}
    + Construct the FP-tree, the 2nd scan is here # p257 
    + Mining via FP-tree #table 6.2

### 6.2.5 Mining Frequent Itemsets Using the Vertical Data Format

### 6.2.6 Mining Closed and Max Patterns
+ search for closed frequent itemsets directly during the mining process -> need to make pruning
    + Item Merging
    + Sub-itemset pruning
    + Item skipping

## 6.3 Pattern Evaluation -> Which Patterns Are Interesting
### 6.3.1 Even Strongs Can Be Misleading
### 6.3.2 From Association Analysis to Correlation Analysis
+ A -> B [support, confidence, correlation]
+ Correlation Measures:
    + Lift
    + X^2
+ Lift:
    + lift(A,B) = P(A U B) / P(A)P(B)
    + if lift(A,B) = 1 -> independent -> no correlation
    + if lift(A,B) < 1 -> negatively correlated -> the occurrence of one likely leads to the absence of the other one
    + if lift(A,B) > 1 -> positively correlated -> the occurrence of one implies the occurrence of the other
+ X^2 #similar to 3.3.2

### 6.3.3 Comparison of Pattern Evaluation Measures
+ whether a measure is null-invariant:
    + A measure is null-invariant if its value is free from
the influence of null-transactions
    + the transactions that do not contain any of the itemsets being examined
+ Some other measure approaches: #p268
    + all_confidence
    + max_confidence
    + Kulczynski
    + cosine
+ Conpared with lift and X^2, these four are null-invariant
+ Suggested: "Kulczynski" together with "imbalance ratio"

## 6.4 Summary
+ frequent patterns, associations, and correlation relationships
+ Association rule mining:
    + Finding frequent itemsets from which strong association rules in the form of A -> B are generated
    + theses rules satisfy minimum confidence threshold
    + correlation rules
+ Frequent itemset mining
    + Apriori
    + FP-growth
    + vertical data format(Eclat)
+ support-confidence framework
    + whether a measure is null-invariant
    + measures: lift, X^2, max_confidence, ...

---------------------------------------
## 6.5 Chapter 6 Exercises


---------------------------------------

# Chapter 7 Advanced Pattern Matching
# Read the road map p280

---------------------------------------
# Chapter 8 Classification: Basic Concepts
+ In this chapter:
    + Decision Tree Classifier
    + Bayesian Classifier
    + Rule-based Classifier
    + How to evaluate them
## 8.1 Basic Concepts
## 8.2 Decision Tree Induction
+ Greedy:
    + ID3
    + C4.5
    + CART
+ Attributee Selection Measures
    + Information Gain: ID3
    + Gain Ratio
    + Gini Index
+ Tree Pruning
    + prepruning #hard to determine when to halt 
    + postpruning #suggested

## 8.3 Bayes Classification Methods

## 8.4 Rule-Based Classification
+ http://www.cnblogs.com/zengzhihua/p/5458373.html
+ http://blog.csdn.net/dq_dm/article/details/38345753

## 8.5 Model Evaluation and Selection
+ See Stanford Statistics I
### 8.5.1 Metrics for Evaluating Classifier Performance
+ #P365 Fig8.13 Different kind of measures
+ Revise TP / TN / FP / FN 
+ Recall = TP / P

### 8.5.2 Holdout Method and Random Subsampling
### 8.5.3 Cross-Validation
+ K-fold
+ LOOCV
+ K = 5-10

### 8.5.4 Bootstrap
### 8.5.5 Model Selection Using Statistical Tests of Significance

### 8.5.6 Comparing Classifiers Based on Cost-Benefit and ROC Curves
+ ROC:
    + x-axis: FP/(FP+TN)
    + y-axis: TP/(TP+FN)

## 8.6 Techniques to Improve Classification Accuracy
+ ensemble methods
    + Bagging
    + Boosting
    + RF
### 8.6.2 Bagging 
+ Procedure #P380 Fig8.23
    + Bootstrap
    + Get subresults from all bags
    + Make vote

### 8.6.3 Boosting and AdaBoost
+ Boosting: 
    + weights are also assigned to each training tuple
    + k classifiers are learned iteratively
    + after each classifier, we increase the weight for those mis-classified samples
    + finally, combines the vote of all classifiers, and the weight is based on the accuracy

+ AdaBoost: #P382 Fig8.24
    + D -> d training samples
    + k -> rounds we want to iterate
    + Initially, give each sample equal weight 1/d
    + For each round i:
        + sample samples from D to form Di
        + each sample''s chance to be chosen is based on its weight
        + Generate model Mi from Di
        + Get Mi''s weight from its error rate
        + in Mi, if a sample is mis-classified -> increase its weight, otherwise -> decrease its weight
+ Error rate of Model i:
    error(Mi) = sum(wj * err(Xj)), j = 1 to d
+ The weight of Model i:
    log[(1-error(Mi))/error(Mi)]

### 8.6.4 Random Forests
+ Similar to bagging, the difference is using random attributes
+ Double random:
    + samples
    + attributes

### 8.6.5 How to improve the classification accuracy
## 8.7 Summary
+ What is classification
+ Dicision tree induction:
    + ID3, C4.5, CART
    + Tree pruning
+ Naive Bayesian classification
+ Rule-based classifier
+ Confusion matrix
    + accuracy
    + sensitivity(recall)
    + specificity
    + precision
    + F
+ How to partition lebeled data to training set and testing set:
    + Holdout
    + Random sampling
    + Cross-Validation
    + Bootstrap
+ Significance tests and ROC curves are useful tools for model selection.
+ Ensemble methods:
    + Bagging
    + Boosting
    + Random Forests
+ Class imbalance problem:
    + oversampling
    + undersampling
    + threshold moving
    + ensemble techniques

---------------------------------------
## 8.8 Chapter 8 Exercises

---------------------------------------
# Chapter 9 Classification: Advanced Methods
# p393
+ Overview
    + Bayesian belief networks
    + Neural Network: Backpropagation
    + SVM
    + Classification using frequent patterns #similar to chapter 6 and 7
    + Instance-based methods of classification
        + nearest-neighbor classifiers
        + case-based reasoning classifiers

## 9.8 Summary
+ Bayesian belief networks allow class conditional independencies to be defined between subsets of variables
+ Backpropagation
+ SVM
+ classification based on frequent patterns:
    + associative classification
    + discriminant frequent pattern based classification
+ eager learners and lazy learners(instance-based)
    + nearest-neighbor classifiers
    + instance-based methods of classification
+ genetic algorithms
+ multiclass classification
+ Semi-supervised classification is useful when large amounts of unlabeled data exist
+ Active learning is a form of supervised learning that is also suitable for situations where data are abundant, yet the class labels are scarce or expensive to obtain.
+ Transfer learning aims to extract the knowledge from one or more source tasks and apply the knowledge to a target task
---------------------------------------
## 9.9 Chapter 9 Exercises
---------------------------------------

# Chapter 10 Cluster Analysis: Basic Concepts and Methods
## 10.1 What is Cluster Analysis
+ clustering is a form of learning by observation, rather than learning by examples -> unsupervised learning

+ requirments of clustering in data mining
    + Scalability
    + Ability to deal with different types of attributes
    + Discovery of clusters with arbitrary shape
    + Requirments for domain knowledge to determine input parameters
    + Ability to deal with noisy data
    + Incremental clustering and insensitivity to input order
    + Capability of clustering high-dimensionality data
    + Constraint-based clustering
    + Interpretability and usability

+ Basic Clustering Methods: #p450 fig10.1
    + Partitioning methods: distance based partitioning
    + Hierarchial methods: 
        + agglomerative(bottom-up) -> merge
        + divisive(top-down) -> split
    + Density-based methods: continue growing a given cluster as long as the density in the “neighborhood” exceeds some threshold
    + Grid-based methods

## 10.2 Partitioning Methods
### 10.2.1 k-Means -> centroid-based method
+ We have seen this algorithm several time

### 10.2.2 k-Medoids -> object-based method
+ We can see a drawback of k-means at p454
+ Instead of taking the mean value of the objects in a cluster as a reference point, we can pick actual objects to represent the clusters, using one representative object per cluster.
+ partitioning method: minimizing the sum of the dissimilarities between each object p and its corresponding
representative object
+ PAM: Partitioning Around Medoids
    + similar to k-means
    + we consider whether replacing a representative object by a non-representative one will improve the quality
    + Iteration will continue until the quality can not be improved by any replacement
    + Measure of quality: average dissimilarity between an object and its cluster''s representative object
## 10.3 Hierarchical Methods
+ grouping data objects into a hierarchy or “tree” of clusters
+ see Stanford Statistics I
### 10.3.1 Agglomerative VS Divisive
# p460 fig10.6 and fig10.7
+ agglomerative: bottom-up
+ divisive: top-down

### 10.3.2 Distance Measures
+ Minimum/Maximum/Mean/Average distance #p461

### 10.3.3 Multiphase Hierarchical Clustering Using Clustering Feature Trees
+ omitted
+ Balanced Iterative Reducing and Clustering using Hierarchies (BIRCH)

### 10.3.4 Chameleon: Multiphase Hierarchical Clustering Using Dynamic Modeling
+ omitted

### 10.3.5 Probabilistic Hierarchical Clustering
+ omitted

## 10.4 Density-Based Methods
+ partitioning and Hierarchical: only spherical-shaped clusters
+ DBSCAN/OPTICE/DENCLUE
### 10.4.1 DBSCAN: Density-Based Clustering Based on Connected Regions with High Density
+ http://www.cnblogs.com/chaosimple/archive/2013/07/01/3164775.html
+ DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
+ Procedure:
    + 输入: 包含n个对象的数据库，半径e，最少数目MinPts;
    + 输出:所有生成的簇，达到密度要求
    + MinPts:minimum number of points required
in the neighborhood of a core object
    + Ε邻域：给定对象半径为Ε内的区域称为该对象的Ε邻域；
    + 核心对象：如果给定对象Ε领域内的样本点数大于等于MinPts，则称该对象为核心对象；
    + Repeat
        + 从数据库中抽出一个未处理的点；
        + IF抽出的点是核心点 THEN 找出所有从该点密度可达的对象，形成一个簇；
        + ELSE 抽出的点是边缘点(非核心对象)，跳出本次循环，寻找下一个点；
        + UNTIL 所有的点都被处理。
+ DBSCAN对用户定义的参数很敏感，细微的不同都可能导致差别很大的结果，而参数的选择无规律可循，只能靠经验确定。

### 10.4.2 OPTICS: Ordering Points to Identify the Clustering Structure
### 10.4.3 DENCLUE: Clustering Based on Density Distribution Functions

## 10.5 Grid-Based Methods
## 10.6 Evolution of Clustering

## 10.7 Summary
+ What is a cluster
+ partitioning method: k-Means/k-Medoids/CLARANS
+ hierarchical method: agglomerative (bottom-up) or divisive (top-down)
+ density-based method: DBSCAN/DENCLUE/OPTICS
+ grid-based method
+ clustering evolution

---------------------------------------
## 10.8 Chapter 10 Exercises

---------------------------------------
