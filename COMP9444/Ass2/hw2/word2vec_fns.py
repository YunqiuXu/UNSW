import tensorflow as tf
import numpy as np
import collections

data_index = 0

def generate_batch(data, batch_size, skip_window):
    """
    Generates a mini-batch of training data for the training CBOW
    embedding model.
    :param data (numpy.ndarray(dtype=int, shape=(corpus_size,)): holds the
        training corpus, with words encoded as an integer
    :param batch_size (int): size of the batch to generate
    :param skip_window (int): number of words to both left and right that form
        the context window for the target word.
    Batch is a vector of shape (batch_size, 2*skip_window), with each entry for the batch containing all the context words, with the corresponding label being the word in the middle of the context
    """
    global data_index    
    batch = [] # np.ndarray(shape=(batch_size), dtype=np.int32)
    labels = [] # np.ndarray(shape=(batch_size, 1), dtype=np.int32)
    span = 2 * skip_window + 1  # [ skip_window target skip_window ]
    
    buffer = collections.deque(maxlen=span)
    if data_index + span > len(data):
        data_index = 0
    buffer.extend(data[data_index:data_index + span])
    data_index += span
    
    for i in range(batch_size):
        # get contents except the center word
        contents = [buffer[i] for i in range(len(buffer)) if i != skip_window]
        # collect content in batch
        batch.append(contents)
        # collect center word in labels
        labels.append(buffer[skip_window])
        
        if data_index == len(data):
            # reached the end of the data, start again
            buffer.extend(data[:span])
            data_index = span
        else:
            # slide the window forward one word (n.b. buffer = deque(maxlen=span))
            buffer.append(data[data_index])
            data_index += 1
    
    # transform batch and labels into numpy array
    # the shape of batch should be (batch_size, 2 * skip_window)
    # the shape of labels should be (batch_size, 1)
    batch = np.array(batch, dtype=np.int32)
    labels = np.array(labels, dtype=np.int32).reshape((batch_size, 1))

    # Backtrack a little bit to avoid skipping words in the end of a batch
    data_index = (data_index - span) % len(data)
    return batch, labels

# there's more than one word in the context we just take the mean (average) of the embeddings for all context words
# tf.reduce_mean(?, axis=?), axis = 0 
# e.g. for [[0,1,2],[3,4,5]], (2,3)
#   no axis --> 2, the avg of all
#   axis = 0 --> [1, 2, 3], the avg of each col
#   axis = 1 --> [1, 4], the avg of each row
def get_mean_context_embeds(embeddings, train_inputs):
    """
    :param embeddings (tf.Variable(shape=(vocabulary_size, embedding_size)) e.g. 50000 * 100
    :param train_inputs (tf.placeholder(shape=(batch_size, 2*skip_window)) , each item in batch is a seq with length 2*skip_window
    returns:
        `mean_context_embeds`: the mean of the embeddings for all context words for each entry in the batch
        shape (batch_size, embedding_size)
    """
    # cpu is recommended to avoid out of memory errors, if you don't
    # have a high capacity GPU
    with tf.device('/cpu:0'):
        embed = tf.nn.embedding_lookup(embeddings, train_inputs)
        mean_context_embeds = tf.reduce_mean(embed, axis = 1)

    return mean_context_embeds
