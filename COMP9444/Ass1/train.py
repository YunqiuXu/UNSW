import tensorflow as tf
import hw1 as qfns
import time
from datetime import datetime
from tensorflow.examples.tutorials.mnist import input_data

#options: "onelayer", "twolayer", "conv"
# network = "none"
# network = "onelayer"
# network = "twolayer"
network = "conv"


def accuracy(sess, dataset, batch_size, X, Y, accuracy_op):
    # compute number of batches for given batch_size
    num_test_batches = dataset.num_examples // batch_size

    overall_accuracy = 0.0
    for i in range(num_test_batches):
        batch = mnist.test.next_batch(batch_size)
        accuracy_batch = \
            sess.run(accuracy_op, feed_dict={X: batch[0], Y: batch[1]})
        overall_accuracy += accuracy_batch

    return overall_accuracy/num_test_batches

def variable_summaries(var, name):
  """Attach a lot of summaries to a Tensor (for TensorBoard visualization)."""
  with tf.name_scope(name+'_summaries'):
    mean = tf.reduce_mean(var)
    tf.summary.scalar('mean', mean)
    with tf.name_scope('stddev'):
      stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
    tf.summary.scalar('stddev', stddev)
    tf.summary.scalar('max', tf.reduce_max(var))
    tf.summary.scalar('min', tf.reduce_min(var))
    tf.summary.histogram('histogram', var)

def train(sess, mnist, n_training_epochs, batch_size,
          summaries_op, accuracy_summary_op, train_writer, test_writer,
          X, Y, train_op, loss_op, accuracy_op):
    # compute number of batches for given batch_size
    num_train_batches = mnist.train.num_examples // batch_size

    # record starting time
    train_start = time.time()

    # Run through the entire dataset n_training_epochs times
    for i in range(n_training_epochs):
        # Initialise statistics
        training_loss = 0
        epoch_start = time.time()

        # Run the SGD train op for each minibatch
        for _ in range(num_train_batches):
            batch = mnist.train.next_batch(batch_size)
            trainstep_result, batch_loss, summary = \
                qfns.train_step(sess, batch, X, Y, train_op, loss_op, summaries_op)
            train_writer.add_summary(summary, i)
            training_loss += batch_loss

        # Timing and statistics
        epoch_duration = round(time.time() - epoch_start, 2)
        ave_train_loss = training_loss / num_train_batches

        # Get accuracy
        train_accuracy = \
            accuracy(sess, mnist.train, batch_size, X, Y, accuracy_op)
        test_accuracy = \
            accuracy(sess, mnist.test, batch_size, X, Y, accuracy_op)

        # log accuracy at the current epoch on training and test sets
        train_acc_summary = sess.run(accuracy_summary_op,
                               feed_dict={accuracy_placeholder: train_accuracy})
        train_writer.add_summary(train_acc_summary, i)
        test_acc_summary = sess.run(accuracy_summary_op,
                                feed_dict={accuracy_placeholder: test_accuracy})
        test_writer.add_summary(test_acc_summary, i)
        [writer.flush() for writer in [train_writer, test_writer]]

        train_duration = round(time.time() - train_start, 2)
        # Output to montior training
        print('Epoch {0}, Training Loss: {1}, Test accuracy: {2}, \
time: {3}s, total time: {4}s'.format(i, ave_train_loss,
                                     test_accuracy, epoch_duration,
                                     train_duration))
    print('Total training time: {0}s'.format(train_duration))
    print('Confusion Matrix:')
    true_class=tf.argmax(Y, 1)
    predicted_class=tf.argmax(preds_op, 1)
    cm=tf.confusion_matrix(predicted_class,true_class)
    print(sess.run(cm, feed_dict={X: mnist.test.images,
                                  Y: mnist.test.labels}))

def get_accuracy_op(preds_op, Y):
    with tf.name_scope('accuracy_ops'):
        correct_preds_op = tf.equal(tf.argmax(preds_op, 1), tf.argmax(Y, 1))
        # the tf.cast sets True to 1.0, and False to 0.0. With N predictions, of
        # which M are correct, the mean will be M/N, i.e. the accuracy
        accuracy_op = tf.reduce_mean(tf.cast(correct_preds_op, tf.float32))
    return accuracy_op


if __name__ == "__main__":
    # hyperparameters
    learning_rate = 0.001
    batch_size = 128
    n_training_epochs = 20

    # load data
    mnist = input_data.read_data_sets('data/mnist', one_hot=True)

    # Input (X) and Target (Y) placeholders, they will be fed with a batch of
    # input and target values resepectively, from the training and test sets
    X = qfns.input_placeholder()
    Y = qfns.target_placeholder()

    # Create the tensorflow computational graph for our model
    if network == "onelayer":
        w, b, logits_op, preds_op, xentropy_op, loss_op = qfns.onelayer(X, Y)
        [variable_summaries(v, name) for (v, name) in zip((w, b), ("w", "b"))]
        tf.summary.histogram('pre_activations', logits_op)
    elif network == "twolayer":
        w1, b1, w2, b2, logits_op, preds_op, xentropy_op, loss_op = \
            qfns.twolayer(X, Y)
        [variable_summaries(v, name) for (v, name) in
            zip((w1, b1, w2, b2), ("w1", "b1", "w2", "b2"))]
        tf.summary.histogram('pre_activations', logits_op)
    elif network == "conv":
        # standard conv layers
         conv1out, conv2out, w, b, logits_op, preds_op, xentropy_op, loss_op = \
         qfns.convnet(tf.reshape(X, [-1, 28, 28, 1]), Y)
         [variable_summaries(v, name) for (v, name) in ((w,"w"), (b,"b"))]
         tf.summary.histogram('pre_activations', logits_op)
    #elif network == "rollyourown":
       ## You can define your own conv net here and play around with it
    else:
        raise ValueError("Incorrect network string in line 7")

    # The training op performs a step of stochastic gradient descent on a minibatch
    # optimizer = tf.train.GradientDescentOptimizer # vanilla SGD
    # optimizer = tf.train.MomentumOptimizer # SGD with momentum
    optimizer = tf.train.AdamOptimizer  # ADAM - widely used optimiser (ref: http://arxiv.org/abs/1412.6980)
    train_op = optimizer(learning_rate).minimize(loss_op)

    # Prediction and accuracy ops
    accuracy_op = get_accuracy_op(preds_op, Y)

    # TensorBoard for visualisation
    # Merge all the summaries and write them out to /tmp/mnist_logs (by default)
    summaries_op = tf.summary.merge_all()

    # Separate accuracy summary so we can use train and test sets
    accuracy_placeholder = tf.placeholder(shape=[], dtype=tf.float32)
    accuracy_summary_op = tf.summary.scalar("accuracy", accuracy_placeholder)

    # When run, the init_op initialises any tensorflow variables
    # hint: weights and biases in our case
    init_op = tf.global_variables_initializer()

    # Get started
    sess = tf.Session()
    sess.run(init_op)

    # Initialise TensorBoard Summary writers
    dtstr = "{:%b_%d_%H-%M-%S}".format(datetime.now())
    train_writer = tf.summary.FileWriter('./summaries/'+dtstr+'/train', sess.graph)
    test_writer  = tf.summary.FileWriter('./summaries/'+dtstr+'/test')

    # Train
    print('Starting Training...')
    train(sess, mnist, n_training_epochs, batch_size,
          summaries_op, accuracy_summary_op, train_writer, test_writer,
          X, Y, train_op, loss_op, accuracy_op)
    print('Training Complete')

    # Clean up
    sess.close()
