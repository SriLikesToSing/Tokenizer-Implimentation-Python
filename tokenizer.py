#tokenizer from scratch in python


def tokenizer(string):
    #best Time complexity so far
     # O(N*M)
    list = []
    whiteSpaceIndex = []

    #add indexes of white spaces located in the string to a list
    for x in range(0, len(string)):
        if string[x] == " ":
            whiteSpaceIndex.append(x)


    for x in range(1, len(whiteSpaceIndex)):
       list.append(string[whiteSpaceIndex[x-1]+1:whiteSpaceIndex[x]])


    return list


Sampletext = "We propose an architecture for VQA which utilizes recurrent layers to\ngenerate visual and textual attention. The memory characteristic of the\nproposed recurrent attention units offers a rich joint embedding of visual and\ntextual features and enables the model to reason relations between several\nparts of the image and question. Our single model outperforms the first place\nwinner on the VQA 1.0 dataset, performs within margin to the current\nstate-of-the-art ensemble model. We also experiment with replacing attention\nmechanisms in other state-of-the-art models with our implementation and show\nincreased accuracy. In both cases, our recurrent attention mechanism improves\nperformance in tasks requiring sequential or relational reasoning on the VQA\ndataset."

print(tokenizer(Sampletext))


#Sample output

'''
['propose', 'an', 'architecture', 'for', 'VQA', 'which',
'utilizes', 'recurrent', 'layers', 'to\ngenerate', 'visual', 'and', 'textual', 'attention.',
'The', 'memory', 'characteristic', 'of', 'the\nproposed', 'recurrent', 'attention',
'units', 'offers', 'a', 'rich', 'joint', 'embedding', 'of', 'visual', 'and\ntextual', 'features', 'and', 'enables', 'the', 'model',
'to', 'reason', 'relations', 'between', 'several\nparts', 'of', 'the', 'image', 'and',
'question.', 'Our', 'single', 'model', 'outperforms', 'the', 'first', 'place\nwinner', 'on', 'the',
'VQA', '1.0', 'dataset,', 'performs', 'within', 'margin', 'to', 'the', 'current\nstate-of-the-art',
'ensemble', 'model.', 'We', 'also', 'experiment', 'with', 'replacing', 'attention\nmechanisms', 'in', 'other', 'state-of-the-art', 'models', 'with', 'our', 'implementation',
'and', 'show\nincreased', 'accuracy.', 'In', 'both', 'cases,', 'our', 'recurrent', 'attention', 'mechanism', 'improves\nperformance',
'in', 'tasks', 'requiring', 'sequential', 'or', 'relational', 'reasoning', 'on', 'the']

'''

