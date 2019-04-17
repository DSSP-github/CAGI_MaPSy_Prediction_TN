README
===
A deep neural networks model for predicting the probablity of a single nucleotide variant being disrupting splicing. This model was created for the MaPSy challenge of [the Fifth Critical Assessment of Genome Interpretation (CAGI 5)] (https://genomeinterpretation.org/).


Description
===
The deep neural networks architecture was generated using [Keras] (https://keras.io/). The model was trained with a dataset of experimentally-defined exonic splicing mutation, which was provided by the challenge host. It receives a base sequence with the information of the position of mutation, and returns the probability of disrupting splicing.  
The attached source code is a simple sample to run the model.

Required
===
* [Keras] (https://keras.io/). We recommend Keras 2.2.4 since different versions may cause unexpected errors.
* The source code is written in [Python] (https://www.python.org/) (3.5.5).

Usage
===
The required input is a 170-mer base sequence with the mutated nucleotide converted as "M". It should comprise both splicing sites as the original traing data. 
(e.g. "CTGTCCCATGTCCTGTCCTCCCTTGTCCACGCCTTGCCCAGCAGCCTCTAACCTCTGCCCTGGGCTCCCCACTCCCACAGTTCTGGATGCTGATTCTGGCCACCACCATCCCCATGCCTGCCGMGTACTTCATGCCCATCTTTGTCTATGGTGAGTCTGGGGTCCTGAGG")
It is encoded to a one-hot vector where each base is converted to a five-element (i.e. "A", "C", "G", "T", and "M") vector of which only element is 1 and the others are 0.
The output is the predicted probability of the variant being exonic splicing mutation (ranging from 0 to 1).

License
===
The souce code and the model are freely available for non-commercial use.
No claim of suitability, guarantee, or any warranty whatever happens.
